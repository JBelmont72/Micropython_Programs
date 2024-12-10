'''
put +++  pull push +++get
'''
import time
import rp2
from machine import Pin
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4)  ## decorator is @  and then set up the output pins!
###   @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)      ##this sets up just one pin
def inOut():
    wrap_target()
    pull()
    mov(x,osr)
    mov(y,x)
    mov(pins,y)
    mov(isr,y)
    push()
    wrap()
sm0=rp2.StateMachine(0,inOut,freq=2000,out_base=Pin(16))        ## instantiation of the pins, create an instance, freq can be 10 million/second
time.sleep(0.5)
print('Python Start Program')
txCnt=sm0.tx_fifo()     ## command gives the number of commands in the FIFO s
rxCnt=sm0.rx_fifo()
print('txCnt= ',txCnt)      ## result = o
print('rxCnt= ',rxCnt)      ## result = 0
print()

print('Add Put()')
sm0.put(0xA) ##  pulls it on the statemachine side to the OSR
txCnt=sm0.tx_fifo()
rxCnt=sm0.rx_fifo()
print('txCnt= ',txCnt)      ## result = 1   The tx fifo register is loaded but the inOut() NOT activated
print('rx_fifo()=',rxCnt)   ## result = 0  not been activated so the OSR and the whole statemachine is not activated
print(' the output is tx =1 and rx=0 because we have not acitvated the instantiated object- not pulled the trigger')
print('')  ##  important  we have not activated and thus have not even activated the inOut()    !!!
         
print('State Machine Running with active(1)')
sm0.active(1)
time.sleep(.2)
txCnt=sm0.tx_fifo()
rxCnt=sm0.rx_fifo()
print('tx_fifo()= ',sm0.tx_fifo())      ## tx_fifo()=0
print('rx_fifo()= ',sm0.rx_fifo())      ## rx_fifo()= 1
print(' pulled the trigger in the statemachine and the value is now in the rx_fifo but has not been get() by the python program')
print()
print('StateMachine Stopped')
sm0.active(0)


print()
print("Put a 0xB")
sm0.put(0xB) ##  pulls it on the statemachine side to the OSR, but the previous value 0xA is still in the rx_fifo
txCnt=sm0.tx_fifo()
rxCnt=sm0.rx_fifo()
print('txCnt= ',txCnt)      ## result = 1   The tx fifo register is loaded but the inOut() NOT activated
print('rx_fifo()=',rxCnt)   ## result = 1  not been activated so the OSR and the whole statemachine is not activated
print(' we have put a new value in the tx_fifo()  and the previous value is still in the rx_fifo()')
print('')

print(' still not activated. will put()  0xC')
sm0.put(0xC)
txCnt=sm0.tx_fifo()
rxCnt=sm0.rx_fifo()
print('tx_fifo(): ',sm0.tx_fifo())
print('rx_fifo() ',sm0.rx_fifo())
print('tx is 2 and rx is one because we have not reactivated the state Machine yet')
print()

print(' still not activated. will put()  0xD')
sm0.put(0xD)
txCnt=sm0.tx_fifo()
rxCnt=sm0.rx_fifo()
print('tx_fifo(): ',sm0.tx_fifo())
print('rx_fifo() ',sm0.rx_fifo())
print('tx is 3 and rx is one because we have not reactivated the state Machine yet')
print()

print(' still not activated. will put()  0xE')
sm0.put(0xF)
txCnt=sm0.tx_fifo()
rxCnt=sm0.rx_fifo()
print('tx_fifo(): ',sm0.tx_fifo())
print('rx_fifo() ',sm0.rx_fifo())
print('tx is 4 and rx is one because we have not reactivated the state Machine yet')
print()
print(' still not activated. will put()  0x0 will not load because there are already 4 words in the TX register')
## the program hangs up here because the tx FIFO register is full soe need a pull in order to free up a space
# sm0.put(0x0)
# txCnt=sm0.tx_fifo()
# rxCnt=sm0.rx_fifo()
# print('tx_fifo(): ',sm0.tx_fifo())
# print('rx_fifo() ',sm0.rx_fifo())
# print('tx is 4 and rx is one because we have not reactivated the state Machine yet')
# print()

print('GET from Rx fifo by using a GET, the statemachine is off so only the RX_FIFO is pushed and received by the get')
myWord=sm0.get()
print('my Word= ', hex(myWord))
time.sleep(1)
txCnt=sm0.tx_fifo()
rxCnt=sm0.rx_fifo()
print('tx_fifo(): ',sm0.tx_fifo())
print('rx_fifo() ',sm0.rx_fifo())



# # ## below overloads the rx_fifo register
# print(' still not activated. will put()  0xE')
# sm0.put(0xE)
# txCnt=sm0.tx_fifo()
# rxCnt=sm0.rx_fifo()
# print('tx_fifo(): ',sm0.tx_fifo())
# print('rx_fifo() ',sm0.rx_fifo())
# print()
# print(' still not activated. will put()  0xF')
# sm0.put(0xF)
# txCnt=sm0.tx_fifo()
# rxCnt=sm0.rx_fifo()
# print('tx_fifo(): ',sm0.tx_fifo())
# print('rx_fifo() ',sm0.rx_fifo())
# print('tx is 2 and rx is one because we have not reactivated the state Machine yet')
# print()

print('State Machine Started')
sm0.active(1)
time.sleep(.2)
txCnt=sm0.tx_fifo()
rxCnt=sm0.rx_fifo()
print(sm0.tx_fifo())
print(sm0.rx_fifo())
# print(myWord)
time.sleep(.5)
sm0.active(1)
myWord=sm0.get()
print(myWord)

myWord=sm0.get()
print(myWord)
myWord =sm0.get()
print(myWord)
myWord=sm0.get()
# myWord =sm0.get()
print(myWord)
# sm0.active(0)

    
print('State Machine Stopped')
txCnt=sm0.tx_fifo()
rxCnt=sm0.rx_fifo()
print(sm0.tx_fifo())
print(sm0.rx_fifo())
# sm0.active(0)
# print('')
# print('GET from RX')  #3 the data is sitting on rx
# myWord=sm0.get()
# print('myWord ',hex(myWord))
# txCnt=sm0.tx_fifo()
# rxCnt=sm0.rx_fifo()
# print(sm0.tx_fifo())
# print(sm0.rx_fifo())
# print('')


###~~~~~~~~~~~~
# from machine import Pin
# import rp2
# from time import sleep

# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*6,out_shiftdir=rp2.PIO.SHIFT_LEFT)
# def pioProg():
#     set(x,0b0001)
#     wrap_target()
#     pull()
#     mov(y,osr)  
#     mov(x,y)
#     mov(isr,x)
#     mov(pins,y) 
#     push()
#     wrap()

# sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=Pin(16))
# sleep(.2)
# # sm0.active(1)
# a=0b0001
# sm0.put(a)
# sleep(.5)
# print('transmit FIFO: ',sm0.tx_fifo())
# print('receive FIFO: ',sm0.rx_fifo())

# print(' start statemachine, no pull yet')
# sm0.active(1)
# sleep(.2)## i needed a brief delay for the sm0 to become active
# print('Transmit FIFO: ',sm0.tx_fifo())
# print('Receive FIFO: ',sm0.rx_fifo())
# print('i added a get but no pull() in the pioProg')
# # print(sm0.get()) ## i haver to UNCOMMNET THIS to get the value out of the RX_FIFO
# sleep(.2)## i needed a brief delay for the sm0 to become active
# print('Transmit FIFO: ',sm0.tx_fifo())
# print('Receive FIFO: ',sm0.rx_fifo())

# print("here I added the push()in the pioProg")
# sleep(.2)## i needed a brief delay for the sm0 to become active
# print('Transmit FIFO: ',sm0.tx_fifo())
# print('Receive FIFO: ',sm0.rx_fifo())

# print(sm0.get())
# while True:
#     for i in range(1,128,1):
#         sm0.put(i)
#         sleep(.1)






    