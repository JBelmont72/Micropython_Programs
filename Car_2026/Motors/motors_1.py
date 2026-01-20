'''
Docstring for Car_2026.Motors.motors_1
'''

'''
Select a PWM Channel: There are 16 channels to choose from, numbered from 0 to 15.
Determine the PWM Frequency: It can go up to 40 MHz, but for our LED fading example, a frequency of 500 Hz should suffice.
Determine the PWM Resolution: It ranges from 1 to 16 bits. The number of discrete duty cycle levels is determined by 2resolution. For example, setting the resolution to 8 bits results in 256 discrete duty cycle levels [0–255]. On the other hand, a resolution of 16 bits provides 65,536 discrete duty cycle levels [0–65535].
Choose the GPIO Pin(s): Choose one or more GPIO pins on the ESP32 to output the PWM signal.
Attach the Pin(s) to the PWM Channel: Attach the selected pin(s) to the selected channel with the selected frequency and resolution using the ledcAttachChannel(pin, freq, resolution, channel) function.
Set the Duty Cycle: Finally, set the actual duty cycle value for a given channel using the ledcWriteChannel(channel, dutycycle) function.
'''
'''
import machine
import time

# Configuration
PWM_CHANNEL = 2               # Channel, corresponds to ESP32 PWM channels
PWM_FREQ = 500                 # Frequency in Hz
PWM_RESOLUTION = 10             # Resolution in bits
MAX_DUTY_CYCLE = (2 ** PWM_RESOLUTION) - 1  # Max duty cycle based on resolution

LED_OUTPUT_PIN = 13            # GPIO pin for LED output
DELAY_MS = 0.004               # Delay between fade increments in seconds

# Setup PWM
led_pwm = machine.PWM(machine.Pin(LED_OUTPUT_PIN), freq=PWM_FREQ, duty=0)

# Function to fade the LED up and down
def fade_led():
    # Fade up
    for duty_cycle in range(0, MAX_DUTY_CYCLE + 1):
        led_pwm.duty(duty_cycle)
        time.sleep(DELAY_MS)

    # Fade down
    for duty_cycle in range(MAX_DUTY_CYCLE, -1, -1):
        led_pwm.duty(duty_cycle)
        time.sleep(DELAY_MS)

# Main loop
while True:
    fade_led()







# ledcChannel method
import machine
import time

# Configuration
PWM_CHANNEL = 2               # Channel, corresponds to ESP32 PWM channels
PWM_FREQ = 500                 # Frequency in Hz
PWM_RESOLUTION = 8             # Resolution in bits
MAX_DUTY_CYCLE = (2 ** PWM_RESOLUTION) - 1  # Max duty cycle based on resolution

LED_OUTPUT_PIN = 13            # GPIO pin for LED output
DELAY_MS = 0.004               # Delay between fade increments in seconds

# Setup PWM
led_pwm = machine.PWM(machine.Pin(LED_OUTPUT_PIN), freq=PWM_FREQ, duty=0)

# Attach the GPIO pin to the PWM channel (using ledcAttachChannel)
led_pwm.duty(0)  # Initial duty cycle

# Function to fade the LED up and down
def fade_led():
    # Fade up
    for duty_cycle in range(0, MAX_DUTY_CYCLE + 1):
        led_pwm.duty(duty_cycle)
        time.sleep(DELAY_MS)

    # Fade down
    for duty_cycle in range(MAX_DUTY_CYCLE, -1, -1):
        led_pwm.duty(duty_cycle)
        time.sleep(DELAY_MS)

# Main loop
while True:
    fade_led()

'''



import machine
import time
import math

# Define motor control pins
PWM_PIN = 15  # Change this to your PWM pin
max_speed = 1023  # Set this based on your PWM resolution (0-1023 for 10-bit)

# Prepare PWM
motor_pwm = machine.PWM(machine.Pin(PWM_PIN), freq=1000, duty=0)

def exponential_scale(input_value, k):
    """
    Calculate the PWM value using exponential scaling.
    
    Args:
    input_value: Value in range [0, 1] or [0, 255]
    k: Exponential scaling factor
    
    Returns:
    PWM value in range [0, max_speed]
    """
    return int(max_speed * (1 - math.exp(-k * input_value)))

while True:
    # Simulate input value changing over time; replace this with your actual input source
    for input_value in range(256):  # Example: Simulate from 0 to 255
        scaled_value = exponential_scale(input_value / 255.0, k=0.1)  # Adjust 'k' as needed
        motor_pwm.duty(scaled_value)  # Set motor speed
        time.sleep(0.1)  # Sleep to create gradual change

    # Ramp down speed
    for input_value in range(255, -1, -1):
        scaled_value = exponential_scale(input_value / 255.0, k=0.1)
        motor_pwm.duty(scaled_value)
        time.sleep(0.1)  # Sleep to create gradual change
