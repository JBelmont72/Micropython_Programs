import json
import time
from machine import ADC, Pin

# ----------------------------
# USER HARDWARE CONFIG
# ----------------------------
JOY_X_PIN = 9
JOY_Y_PIN = 6

adc_x = ADC(Pin(JOY_X_PIN))

adc_y = ADC(Pin(JOY_Y_PIN))


adc_x.atten(ADC.ATTN_11DB)
adc_y.atten(ADC.ATTN_11DB)

# ----------------------------
# STORAGE FILE
# ----------------------------
CAL_FILE = "joystick_cal.json"


def sample():
    """Return a tuple of (x, y) averaged over several readings."""
    total_x = 0
    total_y = 0
    samples = 40

    for _ in range(samples):
        total_x += adc_x.read_u16()
        total_y += adc_y.read_u16()
        time.sleep_ms(2)

    return (total_x // samples, total_y // samples)


def save_calibration(values):
    with open(CAL_FILE, "w") as f:
        json.dump(values, f)
    print("Saved calibration to", CAL_FILE)


def main():
    print("\n============================")
    print(" JOYSTICK CALIBRATION TOOL")
    print("============================\n")
    print("Instructions:")
    print("1. Leave joystick untouched. Press ENTER for CENTER reading.")
    input()
    cx, cy = sample()
    print("CENTER:", cx, cy)

    print("\nMove joystick FULL UP, hold it still, press ENTER.")
    input()
    upx, upy = sample()
    print("UP:", upx, upy)
    #print the pin GPIO numbers being used  
    print(f'JOY_X_PIN: {JOY_X_PIN} , JOY_Y_PIN: {JOY_Y_PIN}')

    print("\nMove joystick FULL DOWN, hold it still, press ENTER.")
    input()
    downx, downy = sample()
    print("DOWN:", downx, downy)

    print("\nMove joystick FULL LEFT, hold it still, press ENTER.")
    input()
    leftx, lefty = sample()
    print("LEFT:", leftx, lefty)

    print("\nMove joystick FULL RIGHT, hold it still, press ENTER.")
    input()
    rightx, righty = sample()
    print("RIGHT:", rightx, righty)

    cal = {
        "center_x": cx,
        "center_y": cy,
        "min_x": min(leftx, cx, upx, downx),
        "max_x": max(rightx, cx, upx, downx),
        "min_y": min(upy, cy, lefty, righty),
        "max_y": max(downy, cy, lefty, righty)
    }

    save_calibration(cal)

    print("\nCalibration complete!")
    print("Values saved:")
    print(cal)


main()