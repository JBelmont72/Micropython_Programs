import machine
sda = machine.Pin(2)
scl = machine.Pin(3)
i2c = machine.I2C(1,sda=sda, scl = scl, freq = 400000)


i2c.writeto(39, '\x7C')
i2c.writeto(39, '\x2D')

i2c.writeto(39,"Hello World")

