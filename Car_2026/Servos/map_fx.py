


# def map_value(x, in_min, in_max, out_min, out_max):
#     return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# # Example usage: map a sensor value from 0-4095 to 0-100
# sensor_value = 2048
# percentage = map_value(sensor_value, 0, 4095, 0, 100)

# print(percentage)
# # Output might be 50 (integer division is used here)

def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# Example usage: map a sensor value from 0-4095 to 0-100
#sensor_value = 2048
for angle in range(0,181,10):
    pwm_value = map_value(angle, 0, 180, 2500, 6800)
    print(f'Angle: {angle}, PWM Value: {pwm_value}')


print(pwm_value)
