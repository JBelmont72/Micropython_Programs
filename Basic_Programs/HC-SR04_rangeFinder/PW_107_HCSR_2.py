'''
PW_107  first HCS04 using PIO

Why Multiply by 3?
The reason for multiplying by 3 is because every iteration of the timing loop (land) takes 3 clock cycles:

in_(pins, 1) → 1 cycle
mov(y, isr) → 1 cycle
jmp(not_y, "moveOn") (or jmp(x_dec, "land")) → 1 cycle
So, for each iteration of the loop, it takes 3 cycles. When you call sm.get(), you retrieve the number of iterations the loop ran, not the actual time.
'''
# import rp2
# from machine import Pin
# import time

# @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
# def pulse_program():
#     wrap_target()
#     pull(block)
#     mov(x,osr)
#     set(pins,1)[10-1]
#     set(pins,0)
#     wait(1,pin,0)
#     label("land")
#     in_(pins,1) # 1 Cycle THese two lines were absent and program hung up
#     mov(y,isr)  # 1 Cycle
#     #mov(y,pins) # 1 clock cycle Was this Problem that the pins had to go to ISR first
#     jmp(not_y,"moveOn") #1 clock cycle
#     jmp(x_dec,"land") # 1 clock cycle
#     label("moveOn")
#     mov(isr,invert(x))
#     push()
#     wrap()
# triggerPin = Pin(1,Pin.OUT)
# echoPin = Pin(0, Pin.IN)
# sm=rp2.StateMachine(0,pulse_program, freq=1000000, set_base=triggerPin,in_base=echoPin)
# sm.active(1)
# while True:
#     sm.put(0xFFFFFFFF)
#     print("Pulse Launched")
#     clockCycles=sm.get()*3/2
#     distance=clockCycles*.0342
#     print("Distance to Target: ",distance)
#     time.sleep(.25)

####~~~~~ improved with 
# More Accurate Timing: Use a higher frequency for more precise timing, though 1 MHz is generally fine.
# Avoid Blocking: Use interrupts or a non-blocking loop to avoid stalling the program during the sm.get() call.
# Error Handling: Add a timeout to handle cases where no echo is received, preventing infinite waits.
import rp2
from machine import Pin
import time

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

# Main loop
while True:
    distance = get_distance()
    if distance is not None:
        print(f"Distance to Target: {distance:.2f} cm")
    else:
        print("Measurement failed.")
    time.sleep(0.25)


####~~~~~~
# add the passive buzzer trigger! A C major chord consists of the notes C, E, and G. Play these notes sequentially to simulate the chord use PWM

# import rp2
# from machine import Pin, PWM
# import time

# # Define the PIO program for ultrasonic timing
# @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
# def pulse_program():
#     wrap_target()
#     pull(block)
#     mov(x, osr)
#     set(pins, 1)[10 - 1]     # Trigger pulse for 10µs
#     set(pins, 0)
#     wait(1, pin, 0)

#     label("land")
#     in_(pins, 1)
#     mov(y, isr)
#     jmp(not_y, "moveOn")
#     jmp(x_dec, "land")

#     label("moveOn")
#     mov(isr, invert(x))
#     push()
#     wrap()

# # Pin setup
# triggerPin = Pin(1, Pin.OUT)
# echoPin = Pin(0, Pin.IN)
# buzzer = PWM(Pin(2))  # Buzzer connected to GPIO2

# # Initialize state machine
# sm = rp2.StateMachine(0, pulse_program, freq=1000000, set_base=triggerPin, in_base=echoPin)
# sm.active(1)

# # Note frequencies for C major chord
# notes = {"C": 261, "E": 329, "G": 392}

# def play_chord():
#     """ Play a C major chord (C, E, G) on the passive buzzer. """
#     for note, freq in notes.items():
#         buzzer.freq(freq)
#         buzzer.duty_u16(32768)  # 50% duty cycle
#         time.sleep(0.3)
#     buzzer.duty_u16(0)         # Turn off buzzer

# def get_distance():
#     sm.put(0xFFFFFFFF)
#     try:
#         clock_cycles = sm.get(timeout=1000)
#     except:
#         print("Timeout: No echo received")
#         return None

#     clock_cycles = clock_cycles * 3 / 2
#     distance = clock_cycles * 0.0342

#     return distance

# # Main loop
# while True:
#     distance = get_distance()
#     if distance is not None:
#         print(f"Distance to Target: {distance:.2f} cm")
#         if distance > 20:
#             print("Distance > 20 cm — Playing C chord")
#             play_chord()
#     else:
#         print("Measurement failed.")
#     time.sleep(0.25)
###~~~
# Buzzer Setup: Added a PWM pin for the passive buzzer.
# C Major Chord: Defined frequencies for C, E, and G notes.
# Play Chord Function: Plays each note in sequence.
# Distance Check: Triggers the buzzer when the distance is greater than 20 cm.

# Handle No Echo Response Gracefully
# If the sensor doesn’t receive an echo (e.g., due to an obstacle absorbing the sound), we should prevent incorrect readings.
# Filter Out Outliers
# Sometimes, ultrasonic sensors return occasional incorrect readings (e.g., a random large number). We can discard extreme values.
# Prevent Blocking in sm.get()
# Right now, sm.get(timeout=1000) waits up to 1 second if no data is received. A shorter timeout or retry mechanism could help.
# Ensure Valid Frequency for the Buzzer
# If the frequency value somehow goes out of range, ensure that we don’t accidentally send invalid data to the buzzer.

# import rp2
# from machine import Pin, PWM
# import time

# # Define the PIO program for ultrasonic timing
# @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
# def pulse_program():
#     wrap_target()
#     pull(block)
#     mov(x, osr)
#     set(pins, 1)[10 - 1]     # Trigger pulse for 10µs
#     set(pins, 0)
#     wait(1, pin, 0)

#     label("land")
#     in_(pins, 1)
#     mov(y, isr)
#     jmp(not_y, "moveOn")
#     jmp(x_dec, "land")

#     label("moveOn")
#     mov(isr, invert(x))
#     push()
#     wrap()

# # Pin setup
# triggerPin = Pin(1, Pin.OUT)
# echoPin = Pin(0, Pin.IN)
# buzzer = PWM(Pin(2))  # Buzzer connected to GPIO2

# # Initialize state machine
# sm = rp2.StateMachine(0, pulse_program, freq=1000000, set_base=triggerPin, in_base=echoPin)
# sm.active(1)

# # Note frequencies for C major chord
# notes = {"C": 261, "E": 329, "G": 392}

# def play_chord():
#     """ Play a C major chord (C, E, G) on the passive buzzer. """
#     for note, freq in notes.items():
#         buzzer.freq(freq)
#         buzzer.duty_u16(32768)  # 50% duty cycle
#         time.sleep(0.3)
#     buzzer.duty_u16(0)         # Turn off buzzer

# def get_distance():
#     sm.put(0xFFFFFFFF)
#     try:
#         clock_cycles = sm.get(timeout=1000)
#     except:
#         print("Timeout: No echo received")
#         return None

#     clock_cycles = clock_cycles * 3 / 2
#     distance = clock_cycles * 0.0342

#     return distance

# # Main loop
# while True:
#     distance = get_distance()
#     if distance is not None:
#         print(f"Distance to Target: {distance:.2f} cm")
#         if distance > 20:
#             print("Distance > 20 cm — Playing C chord")
#             play_chord()
#     else:
#         print("Measurement failed.")
#     time.sleep(0.25)
###~~~

# Buzzer Setup: Added a PWM pin for the passive buzzer.
# C Major Chord: Defined frequencies for C, E, and G notes.
# Play Chord Function: Plays each note in sequence.
# Distance Check: Triggers the buzzer when the distance is greater than 20 cm.
###~~~~~~~~~
# Echo Timeout for No Object Detected:
# If the object is too far or the signal is lost, the echo might never return. You already have a timeout in sm.get(), but adding a small check for very large or zero distances can catch edge cases.
# Distance Range Validation:
# The HC-SR04 sensor has a range of ~2 cm to ~400 cm. If the measured distance is outside this range, we can ignore it as invalid.
# Buzzer Safety:
# Add a failsafe to turn off the buzzer if an invalid measurement occurs.
# Here’s an updated version with those improvements:

# Add more error handling would make  program more reliable! Tighten it up. Here are a few improvements:

# 1. **Echo Timeout for No Object Detected:**  
#    If the object is too far or the signal is lost, the echo might never return. You already have a timeout in `sm.get()`, but adding a small check for very large or zero distances can catch edge cases.

# 2. **Distance Range Validation:**  
#    The HC-SR04 sensor has a range of ~2 cm to ~400 cm. If the measured distance is outside this range, we can ignore it as invalid.

# 3. **Buzzer Safety:**  
#    Add a failsafe to turn off the buzzer if an invalid measurement occurs.

# Hereis an updated version with those improvements:

# import rp2
# from machine import Pin, PWM
# import time

# # Define the PIO program for ultrasonic timing
# @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
# def pulse_program():
#     wrap_target()
#     pull(block)
#     mov(x, osr)
#     set(pins, 1)[10 - 1]     # Trigger pulse for 10µs
#     set(pins, 0)
#     wait(1, pin, 0)

#     label("land")
#     in_(pins, 1)
#     mov(y, isr)
#     jmp(not_y, "moveOn")
#     jmp(x_dec, "land")

#     label("moveOn")
#     mov(isr, invert(x))
#     push()
#     wrap()

# # Pin setup
# triggerPin = Pin(1, Pin.OUT)
# echoPin = Pin(0, Pin.IN)
# buzzer = PWM(Pin(2))  # Buzzer connected to GPIO2

# # Initialize state machine
# sm = rp2.StateMachine(0, pulse_program, freq=1000000, set_base=triggerPin, in_base=echoPin)
# sm.active(1)

# # Note frequencies for C major chord
# notes = {"C": 261, "E": 329, "G": 392}

# def play_chord():
#     """ Play a C major chord (C, E, G) on the passive buzzer. """
#     for note, freq in notes.items():
#         buzzer.freq(freq)
#         buzzer.duty_u16(32768)  # 50% duty cycle
#         time.sleep(0.3)
#     buzzer.duty_u16(0)         # Turn off buzzer

# def get_distance():
#     sm.put(0xFFFFFFFF)
#     try:
#         clock_cycles = sm.get(timeout=1000)  # Wait with timeout (1000 ms)
#     except:
#         print("Timeout: No echo received")
#         return None

#     # Convert clock cycles to distance
#     clock_cycles = clock_cycles * 3 / 2
#     distance = clock_cycles * 0.0342

#     # Validate the distance range (2 cm to 400 cm)
#     if distance < 2 or distance > 400:
#         print(f"Invalid distance: {distance:.2f} cm")
#         return None

#     return distance

# # Main loop
# while True:
#     distance = get_distance()
#     if distance is not None:
#         print(f"Distance to Target: {distance:.2f} cm")
#         if distance > 20:
#             print("Distance > 20 cm — Playing C chord")
#             play_chord()
#     else:
#         print("Measurement failed.")
#         buzzer.duty_u16(0)  # Ensure buzzer is turned off if measurement fails
    
#     time.sleep(0.25)
