'''25 october 2025 this works on prgram_one.py and program_two.py in obsidian 'Main' along with main_long_short.py and main_template.py

https://chatgpt.com/c/68fd3220-3c48-8332-b5c5-bb603338dde7
if button is to ground will need to flip the logic
if not val and not pressed:   # pressed

elif val and pressed:         # released


for button to vcc:  DOWN HOT Zero! for button
from machine import Pin
import time

button = Pin(26, Pin.IN, Pin.PULL_DOWN)
while True:
    print(button.value())
    time.sleep(0.2)
0 when not pressed. 1 when pressed

if connected to ground then Pin.PULL_UP
and 1 when not pressed and 0 when presed
'''

import machine
import utime
import sys

# === CONFIGURATION ===
BUTTON_PIN = 26            # active HIGH button to 3.3V
LONG_PRESS_TIME_MS = 4000  # 4 seconds threshold
DEBOUNCE_MS = 50

button = machine.Pin(BUTTON_PIN, machine.Pin.IN,machine.Pin.PULL_DOWN)  # no pull-up on GPIO26, Down Hot Zero!

press_start = None
press_end = None
pressed = False

print("\nPress the button to select a program...")
print("→ Short press = program_one.py")
print("→ Long press  = program_two.py\n")

while True:
    val = button.value()

    if val and not pressed:  # button just pressed (1)
        pressed = True
        press_start = utime.ticks_ms()

    elif not val and pressed:  # button just released (0)
        press_end = utime.ticks_ms()
        pressed = False

        press_duration = utime.ticks_diff(press_end, press_start)
        press_start = None
        press_end = None

        # Handle the press type
        if press_duration < DEBOUNCE_MS:
            print("Ignored noise press.")
        elif press_duration < LONG_PRESS_TIME_MS:
            print(f"Short press detected ({press_duration/1000:.2f}s).")
            print("\nRunning program_one.py ...")
            import program_one
        else:
            print(f"Long press detected ({press_duration/1000:.2f}s).")
            print("\nRunning program_two.py ...")
            import program_two

        print("Returning to selector in 3 s...\n")
        utime.sleep(3)
        machine.reset()

    utime.sleep_ms(20)
