'''combining RPI and ESP32
for esp32 i am following Sunfounder https://docs.sunfounder.com/projects/esp32-starter-kit/en/latest/micropython/basic_projects/py_ac_buz.html
for RPI i am following SunfounderKepler Kit for Raspberry Pi 

Pico.  https://docs.sunfounder.com/projects/kepler-kit/en/latest/
USE Freenove because it uses GPIOZero, https://docs.freenove.com/projects/fnk0054/en/latest/fnk0054/codes/c%26py/6_Buzzer.html
RPI.    https://docs.sunfounder.com/projects/raphael-kit/en/latest/ uses bcm  and rpi
RPI      https://docs.sunfounder.com/projects/davinci-kit/en/latest/
'''
# import sys      ## universal template this works on esp32 , 2d version below to add RPI
# #copies in #/Users/judsonbelmont/Documents/SharedFolders/ESP32/ESP32-ESPNOW/Universal_template.py
# # also copy in RPI_1 workspace
# # ---------------------------
# # Platform detection		Consolidated
# # ---------------------------
# def detect_platform():
#     try:
#         import machine  # MicroPython only
#         import os
#         uname = os.uname()
#         return {
#             "platform": "esp32",
#             "name": uname.sysname,
#             "version": uname.release,
#             "details": uname
#         }
#     except ImportError:
#         # Assume Raspberry Pi
#         import platform
#         return {
#             "platform": "raspberrypi",
#             "name": platform.system(),
#             "version": platform.release(),
#             "details": platform.uname()
#         }


# # ---------------------------
# # Platform-specific setup
# # ---------------------------
# def setup(info):
#     """
#     Initialize hardware resources here.
#     Add imports specific to each platform inside the conditions.
#     """
#     if info["platform"] == "raspberrypi":
#         from gpiozero import LED  # Import modules as needed
#         led = LED(17)             # Example: LED on GPIO17
#         return {"led": led}

#     elif info["platform"] == "esp32":
#         from machine import Pin   # Import modules as needed
#         led = Pin(2, Pin.OUT)     # Example: built-in LED
#         active_buzzer=Pin(5,Pin.OUT)
#         return {"led": led,'active_buzzer':active_buzzer}

#     return {}  # Empty resources if nothing initialized


# # ---------------------------
# # Platform-specific loop
# # ---------------------------
# def loop(info, resources):
#     """
#     Main program logic.
#     Runs inside a while True loop with nested try/except:
#       - KeyboardInterrupt cleanly breaks loop.
#       - Other runtime errors are caught and logged, loop continues.
#     """
#     import time
#     led = resources.get("led")
#     active_buzzer = resources.get('active_buzzer')

#     print(f"Starting loop on {info['platform']} (Ctrl+C to exit).")

#     while True:
#         try:
#             # ---- MAIN WORK SECTION ----
#             # Replace this LED blink example with your logic.
#             #active_buzzer.value(1) ## for the MH_FMD is active when Low
#             led.on() if info["platform"] == "raspberrypi" else led.value(1)
#             time.sleep(0.5)
#             led.off() if info["platform"] == "raspberrypi" else led.value(0)
#             time.sleep(0.5)
#             for i in range(4):
#                 print('Buzzer on')
#                 # Turn on the buzzer by setting its value to 1
#                 active_buzzer.value(1) if info['platform'] == 'esp32' else active_buzzer.value(1)
#                 # Pause for 0.2 seconds
#                 time.sleep(0.2)
#                 # Turn off the buzzer
#                 active_buzzer.value(0) if info['platform'] == 'esp32' else active_buzzer.value(1)
#                 # Pause for 0.2 seconds
#                 time.sleep(0.2)
#             # Pause for 1 second before restarting the for loop
#             #active_buzzer.value(1)## only high for to turn off the MH-FMD buzzer
#             active_buzzer.value(0)# for all other active buzzers
#             time.sleep(1)
            



#         except KeyboardInterrupt:
#             # Allows graceful exit
#             print("\nKeyboardInterrupt received. Exiting loop...")
#             break

#         except Exception as e:
#             # Catch other errors without crashing
#             print("Runtime error in loop:", e)
#             time.sleep(1)  # Optional backoff before retry


# # ---------------------------
# # Platform-specific cleanup
# # ---------------------------
# def cleanup(info, resources):
#     """
#     Release resources, close devices, deinit pins, etc.
#     """
#     if info["platform"] == "raspberrypi":
#         print("Cleaning up Raspberry Pi resources...")
#         resources.get("led") and resources["led"].close()

#     elif info["platform"] == "esp32":
#         from machine import Pin
#         print("Cleaning up ESP32 resources...")
#         if "led" in resources:
#             resources["led"].init(Pin.IN)  # Reset pin to input
#         if 'active_buzzer' in resources:
#             resources['active_buzzer'].value(0)
#             resources['active_buzzer'].init(Pin.IN)

# # ---------------------------
# # Main entry point
# # ---------------------------
# def main():
#     info = detect_platform()
#     print("Platform:", info["platform"])
#     print("System Name:", info["name"])
#     print("Version:", info["version"])
#     print("Details:", info["details"])

#     resources = setup(info)

#     try:
#         loop(info, resources)
#     finally:
#         cleanup(info, resources)
## below is attmept to add RPI for buzzer to the led

# if __name__ == "__main__":
#     main()

import sys      ## universal template
#copies in #/Users/judsonbelmont/Documents/SharedFolders/ESP32/ESP32-ESPNOW/Universal_template.py
# also copy in RPI_1 workspace
# ---------------------------
# Platform detection		Consolidated
# ---------------------------
def detect_platform():
    try:
        import machine  # MicroPython only
        import os
        uname = os.uname()
        return {
            "platform": "esp32",
            "name": uname.sysname,
            "version": uname.release,
            "details": uname
        }
    except ImportError:
        # Assume Raspberry Pi
        import platform
        return {
            "platform": "raspberrypi",
            "name": platform.system(),
            "version": platform.release(),
            "details": platform.uname()
        }


# ---------------------------
# Platform-specific setup
# ---------------------------
def setup(info):
    """
    Initialize hardware resources here.
    Add imports specific to each platform inside the conditions.
    """
    if info["platform"] == "raspberrypi":
        from gpiozero import LED, Buzzer  # Import modules as needed
        led = LED(17)             # Example: LED on GPIO17
        active_buzzer=Buzzer(5)
        return {"led": led,'active_buzzer':active_buzzer}

    elif info["platform"] == "esp32":
        from machine import Pin   # Import modules as needed
        led = Pin(2, Pin.OUT)     # Example: built-in LED
        active_buzzer=Pin(5,Pin.OUT)
        return {"led": led,'active_buzzer':active_buzzer}

    return {}  # Empty resources if nothing initialized


# ---------------------------
# Platform-specific loop
# ---------------------------
def loop(info, resources):
    """
    Main program logic.
    Runs inside a while True loop with nested try/except:
      - KeyboardInterrupt cleanly breaks loop.
      - Other runtime errors are caught and logged, loop continues.
    """
    import time
    led = resources.get("led")
    active_buzzer = resources.get('active_buzzer')

    print(f"Starting loop on {info['platform']} (Ctrl+C to exit).")

    while True:
        try:
            # ---- MAIN WORK SECTION ----
            # Replace this LED blink example with your logic.
            #active_buzzer.value(1) ## for the MH_FMD is active when Low
            led.on() if info["platform"] == "raspberrypi" else led.value(1)
            time.sleep(0.5)
            led.off() if info["platform"] == "raspberrypi" else led.value(0)
            time.sleep(0.5)
            for i in range(4):
                print('Buzzer on')
                # Turn on the buzzer by setting its value to 1
                active_buzzer.value(1) if info['platform'] == 'esp32' else active_buzzer.value(1)
                active_buzzer.value(1) if info['platform'] == 'raspberrypi' else active_buzzer.value(1)
                # Pause for 0.2 seconds
                time.sleep(0.2)
                # Turn off the buzzer
                active_buzzer.value(0) if info['platform'] == 'esp32' else active_buzzer.value(1)
                active_buzzer.value(0) if info['platform'] == 'raspberrypi' else active_buzzer.value(1)
                # Pause for 0.2 seconds
                time.sleep(0.2)
            # Pause for 1 second before restarting the for loop
            #active_buzzer.value(1)## only high for to turn off the MH-FMD buzzer
            active_buzzer.value(0)# for all other active buzzers
            time.sleep(1)
            



        except KeyboardInterrupt:
            # Allows graceful exit
            print("\nKeyboardInterrupt received. Exiting loop...")
            break

        except Exception as e:
            # Catch other errors without crashing
            print("Runtime error in loop:", e)
            time.sleep(1)  # Optional backoff before retry


# ---------------------------
# Platform-specific cleanup
# ---------------------------
def cleanup(info, resources):
    """
    Release resources, close devices, deinit pins, etc.
    """
    if info["platform"] == "raspberrypi":
        print("Cleaning up Raspberry Pi resources...")
        resources.get("led") and resources["led"].close()
        
        resources.get("active_buzzer") and resources["active_buzzer"].close()
        
        

    elif info["platform"] == "esp32":
        from machine import Pin
        print("Cleaning up ESP32 resources...")
        if "led" in resources:
            resources["led"].init(Pin.IN)  # Reset pin to input
        if 'active_buzzer' in resources:
            resources['active_buzzer'].value(0)
            resources['active_buzzer'].init(Pin.IN)

# ---------------------------
# Main entry point
# ---------------------------
def main():
    info = detect_platform()
    print("Platform:", info["platform"])
    print("System Name:", info["name"])
    print("Version:", info["version"])
    print("Details:", info["details"])

    resources = setup(info)

    try:
        loop(info, resources)
    finally:
        cleanup(info, resources)


if __name__ == "__main__":
    main()


## below is RPI freenove https://docs.freenove.com/projects/fnk0054/en/latest/fnk0054/codes/c%26py/6_Buzzer.html
# from gpiozero import Buzzer, Button  
# import time

# buzzer = Buzzer(12)
# button = Button(21)

# def onButtonPressed():
#     buzzer.on()
#     print("Button is pressed, buzzer turned on >>>")
    
# def onButtonReleased():
#     buzzer.off()
#     print("Button is released, buzzer turned on <<<")

# def loop():
#     button.when_pressed = onButtonPressed
#     button.when_released = onButtonReleased
#     while True :
#         time.sleep(1)
        
# def destroy():
#     buzzer.close()
#     button.close()

# if __name__ == '__main__':     # Program entrance
#     print ('Program is starting ... ')
#     try:
#         loop()
#     except KeyboardInterrupt:  # Press ctrl-c to end the program.
#         print("Ending program")
#     finally:
#         destroy()