'''
Slador has a nice explanation of PIO and neopixel but is in C language
the 5 bits from the 2 byte command  (8 through 12  which can code up to 32 digits(0-31)) are used to set 'delay' and 'side-set'

These 5 bits can be used wither to det up a delay(0-31) cycles
or a combination of side set  2  bits , and delay 3  [0-7] bits.
 for the neopixel the data in is 1.25 microseconds.  
 bit 0 is 400 nanoseconds high and 850 ns low.
 the bit 1 is 800 nanosec high and 450 nanosec low.
 sought of like PWM
ws 2812B neopixel
bus reset is greater than 50 muicroseconds




'''
