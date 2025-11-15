
I am keeping record of my review process and programs that i work on.

# 1 Nov 2025
PW lesson 11 controlling dimmable led with potentiometer
/Users/judsonbelmont/Documents/SharedFolders/Pico/Micropython_Programs/Basic_Programs/McWhorter/Pot_ADC_1.py

# 2 Nov 2025
PW lesson 12 Understanding eh RGB LED
/Users/judsonbelmont/Documents/SharedFolders/Pico/Micropython_Programs/Basic_Programs/McWhorter/RGB_1.py
### this prints the values on the same line rather than a new line each time
    def Red(potVal):
    exponent = (16/65535 )*potVal
    brightness =2** exponent
    rLed.duty_u16(int(brightness))
    # print(brightness)
    print('potVal:  {potVal}') ## various pring format options!
    print('potVal: {:5}'.format(potVal),end='\r')
    print('potVal:    %5d,   brightness:  %5d'  % (potVal, brightness),end='\r')
    sleep(.3)
    


Music _ListComprehension.py has chat link for link comprehension
/Users/judsonbelmont/Documents/SharedFolders/Pico/Micropython_Programs/music_listComprehension.py