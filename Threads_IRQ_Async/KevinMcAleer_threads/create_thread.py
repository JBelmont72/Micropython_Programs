# import _thread
# import utime
# param1 = 1
# param2 = 2

# def hello(param1,param2,param3=3):
#     while True:
#         print("Hello world, this is Core 1")
#         utime.sleep(1)
#         print(param1,param2,param3)
# global startTime
# _thread.start_new_thread(hello,(param1,param2),{'param3':3})
# while True:
#     try:
#         startTime= utime.ticks_us()
#         # sleep(.3)
#         print('Hi, this is core 0')
#         stopTime= utime.ticks_us()
#         deltaTime =utime.ticks_diff(stopTime,startTime)
#         print(deltaTime)
#         utime.sleep(0.01)
#     except KeyboardInterrupt:
#         print('Closing Program')
#         _thread.exit()
#         break
 
 ############ odd numbers print q 2 seconds and even numbers q 1 second
# import _thread
# import utime
# def core0_thread():
#     counter =0
#     while True:
#         print(counter)
#         counter +=2
#         utime.sleep(1)
    
# def core1_thread():
#     counter =1
#     while True:
#         print(counter)
#         counter +=2
#         utime.sleep(2)
        
# second_thread= _thread.start_new_thread(core1_thread,())
# while True:
#     try:

#         core0_thread()
#         second_thread()
    
#     except KeyboardInterrupt:
#         print('Closing Program')
#         _thread.exit()
#         break
#########
# import _thread
# import utime
# def core0_thread():
#     global run_core1
#     while run_core1==False:
#         counter =0
#         for loop in range(5):
#             print(counter)
#             counter +=2
#             utime.sleep(1)
        
#         print('core 0 waiting')
#         run_core1=True
#     while run_core1:
#         pass
# def core1_thread():
#     print('CORE1 is Waiting')
#     global run_core1
#     while run_core1==False:
#     # while not run_core1:
#         pass
#     while run_core1==True:
#         counter =1
#         for loop in range(5):
#             print(counter)
#             counter +=2
#             utime.sleep(2)
#         run_core1=False
#     # print('core 0 is waiting') 
#     # while run_core1==False:
#     #     pass  

# global run_core1
# run_core1=False

# # second_thread= _thread.start_new_thread(core1_thread,())
# # core0_thread()
# while True:
#     try:
#         _thread.start_new_thread(core1_thread,())
#         core0_thread()
#         # second_thread()
    
#     except KeyboardInterrupt:
#         print('Closing Program')
#         _thread.exit()
#         break
##########################
## from Making stuff with chris dehut

