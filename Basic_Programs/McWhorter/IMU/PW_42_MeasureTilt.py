'''

'''
from imu import MPU6050
from machine import Pin, I2C
import time
import math
i2c=I2C(0,sda=Pin(16),scl=Pin(17),freq=400000)
mpu=MPU6050(i2c)
while True:
    xAccel=round(mpu.accel.x,1)
    yAccel=round(mpu.accel.y,1)
    zAccel=round(mpu.accel.z,1)
    # print('x Accel: ',xAccel, ' G   y Accel: ',yAccel,' G  z Accel: ',zAccel )
    print('x Accel: ',xAccel, ' G   y Accel: ',yAccel,' G ' )
    zReal = zAccel * 9.81
    xReal = xAccel * 9.81
    yReal = yAccel * 9.81
    print('X Acceleration= ',abs(xReal), ' Y Acceleration= ',abs(yReal),' Z Acceleration= ',abs(zReal))
    time.sleep(.1)