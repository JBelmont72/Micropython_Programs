'''
using PIO StateMachine IRQ interrupts to handle critical distance alerts is a great approach to override joystick commands when the distance becomes too short
Approach:
StateMachine for Each HC-SR04:
Use two StateMachines on the car’s Pico W.
One for the front HC-SR04 and another for the back HC-SR04.
Generate IRQ on Critical Distance:
Configure each StateMachine to trigger an IRQ (interrupt request) when the measured distance is below a critical threshold (e.g., 10 cm).
The IRQ handler can send an emergency MQTT message to the joystick-controlling Pico W to stop or change direction.
Override Joystick Commands:
In the main loop, check for a critical distance flag set by the IRQ.
If triggered, ignore joystick commands and apply emergency braking or reversal to avoid collision.
Step 1: Enable StateMachine IRQs
Add irq(handler=callback_function) to the StateMachine.
The callback_function gets called when the distance condition is met. Step 2: Define the IRQ Callback
The callback sends an MQTT message or sets a flag to stop the motors.
Step 3: Override Joystick in Main Loop
Check the critical distance flag.
Ignore joystick input if the flag is set and respond with emergency action.
Critical distance IRQs interrupt normal operation.
Immediate MQTT message alerts joystick controller.
Smoothly overrides joystick commands to prevent collisions.
Consider these options: Add a cooldown period after critical distance detection.
    Send distance data periodically to the joystick controller.
'''
import rp2
from machine import Pin
import time
from umqtt.simple import MQTTClient

# MQTT configuration
MQTT_BROKER = "192.168.1.xxx"  # Replace with your broker's IP address
CLIENT_ID = "car"               # Unique ID for this client
TOPIC_ALERT = "car/alert"       # Topic to send critical alerts

# Create and connect the MQTT client
mqtt_client = MQTTClient(CLIENT_ID, MQTT_BROKER)
mqtt_client.connect()

# Publish a message when critical distance is detected
mqtt_client.publish(TOPIC_ALERT, "STOP")

# Define the PIO program for ultrasonic timing
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def pulse_program():
    wrap_target()
    pull(block)               # Wait for a value to start
    mov(x, osr)              # Move the value to X (countdown timer)
    set(pins, 1)[10 - 1]     # Trigger pulse for 10µs
    set(pins, 0)             # End trigger pulse
    wait(1, pin, 0)          # Wait for echo to go HIGH (start timing)
    
    label("land")
    in_(pins, 1)             # Sample echo pin (1 cycle)
    mov(y, isr)             # Move sample to Y (1 cycle)   second clock cycle of the loop
    jmp(not_y, "moveOn")    # Break if echo goes LOW (1 cycle)  this provides the last clock cycle when                      falls out of loop
    jmp(x_dec, "land")      # Decrement X and loop (1 cycle)    third clock cycle of the loop

    label("moveOn")
    mov(isr, invert(x))     # Invert X to get the pulse length
    push()                  # Push result to FIFO
    wrap()

# Pin setup
triggerPin = Pin(11, Pin.OUT)
echoPin = Pin(12, Pin.IN)

# Initialize state machine
sm = rp2.StateMachine(0, pulse_program, freq=1000000, set_base=triggerPin, in_base=echoPin)
sm.active(1)

def get_distance():
    sm.put(0xFFFFFFFF)                          # Start the state machine with a large value
    try:
        clock_cycles=sm.get()
        # return clock_cycles
        # clock_cycles = sm.get(timeout=1000)     # Wait with a timeout (1000 ms)
    except:
        print("Timeout: No echo received")
        return None

    # Convert cycles to distance
    clock_cycles = clock_cycles * 3 / 2         # 3 cycles per loop, divide by 2 for round trip
    distance = clock_cycles * 0.0342            # Convert to cm (speed of sound in air)

    return distance

# # Main loop
# while True:
#     distance = get_distance()
#     if distance is not None:
#         print(f"Distance to Target: {distance:.2f} cm")
#     else:
#         print("Measurement failed.")
#     time.sleep(0.25)



# Critical distance threshold (in cm)
CRITICAL_DISTANCE = 10

# MQTT Setup
mqtt_client = mqtt.MQTTClient("car", "broker_ip")
mqtt_client.connect()

# IRQ flags
critical_flag = False

# StateMachine callback to handle critical distances
def distance_alert(sm):
    global critical_flag
    distance = get_distance(sm)
    if distance and distance < CRITICAL_DISTANCE:
        critical_flag = True
        mqtt_client.publish("car/alert", "STOP")
    else:
        critical_flag = False

# PIO program and pin setup (front and back HC-SR04)
triggerPin1 = Pin(11, Pin.OUT)  # Front
echoPin1 = Pin(12, Pin.IN)

triggerPin2 = Pin(13, Pin.OUT)  # Back
echoPin2 = Pin(14, Pin.IN)

sm1 = rp2.StateMachine(0, pulse_program, freq=1000000, set_base=triggerPin1, in_base=echoPin1)
sm2 = rp2.StateMachine(1, pulse_program, freq=1000000, set_base=triggerPin2, in_base=echoPin2)
# Define individual callback functions for each StateMachine ALTERNATIVE TO LAMBDA FUNCTIONS BELOW
def distance_alert_front(sm):
    distance_alert(sm1)

def distance_alert_back(sm):
    distance_alert(sm2)

# Attach the IRQs using the named functions
sm1.irq(handler=distance_alert_front)
sm2.irq(handler=distance_alert_back)



## I chose to use the non lambda callback function of the previous 6 lines  for simplification
# # Attach IRQs
# sm1.irq(handler=lambda x: distance_alert(sm1))
# sm2.irq(handler=lambda x: distance_alert(sm2))

# Activate StateMachines
sm1.active(1)
sm2.active(1)

# Main loop
while True:
    if not critical_flag:
        # Process joystick commands
        joystick_command = mqtt_client.check_msg()
        if joystick_command:
            handle_joystick(joystick_command)
    else:
        # Emergency stop or reverse
        stop_motors()
    time.sleep(0.1)
