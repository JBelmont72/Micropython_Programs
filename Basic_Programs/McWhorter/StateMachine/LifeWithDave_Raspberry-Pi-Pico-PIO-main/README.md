# Raspberry-Pi-Pico-PIO
Files and Info regarding the PIO features of the RasPi Pico.
This is the code that was featured in Life with David, Captain PICO, The PIO Chornicles, Episode 1, Paralllel Ports
https://micropython-docs.readthedocs.io/en/latest/library/rp2.html

https://micropython-docs.readthedocs.io/en/latest/library/rp2.StateMachine.html
https://micropython-docs.readthedocs.io/en/latest/library/rp2.PIO.html

Side Set allows simultaneious output signal on side pins

delay specifies number of 


For running PIO programs, see rp2.StateMachine.
_________
https://micropython-docs.readthedocs.io/en/latest/library/rp2.html

rp2.asm_pio(*, out_init=None, set_init=None, sideset_init=None, in_shiftdir=0, out_shiftdir=0, autopush=False, autopull=False, push_thresh=32, pull_thresh=32, fifo_join=PIO.JOIN_NONE)
Assemble a PIO program.

The following parameters control the initial state of the GPIO pins, as one of PIO.IN_LOW, PIO.IN_HIGH, PIO.OUT_LOW or PIO.OUT_HIGH. If the program uses more than one pin, provide a tuple, e.g. out_init=(PIO.OUT_LOW, PIO.OUT_LOW).

out_init configures the pins used for out() instructions.
set_init configures the pins used for set() instructions. There can be at most 5.
sideset_init configures the pins used side-setting. There can be at most 5.
The following parameters are used by default, but can be overridden in StateMachine.init():

in_shiftdir is the default direction the ISR will shift, either PIO.SHIFT_LEFT or PIO.SHIFT_RIGHT.
out_shiftdir is the default direction the OSR will shift, either PIO.SHIFT_LEFT or PIO.SHIFT_RIGHT.
push_thresh is the threshold in bits before auto-push or conditional re-pushing is triggered.
pull_thresh is the threshold in bits before auto-push or conditional re-pushing is triggered.
The remaining parameters are:

autopush configures whether auto-push is enabled.
autopull configures whether auto-pull is enabled.
fifo_join configures whether the 4-word TX and RX FIFOs should be combined into a single 8-word FIFO for one direction only. The options are PIO.JOIN_NONE, PIO.JOIN_RX and PIO.JOIN_TX.

nice short tutorial
https://circuitcellar.com/resources/quickbits/rp2040-programmable-io/#:~:text=Shifts%20a%20number%20of%20bits%20from%20an%20input,if%20the%20bit%20count%20reaches%20a%20programmed%20threshold.
has two processors.  The PIO instructions are highly deterministic so it’s easy to design synchronous interfaces with precise and repeatable timing. There are two PIO modules in the device, each consisting of four state machines with dedicated RX and TX FIFOs. The four state machines share a 32-word program memory. This might not sound like much, but you can get a lot done in just a few instructions as we will see. The state machines also share a set of interrupt flags which can be used for inter-task synchronisation and/or to interrupt the MCU.
OSR FIFO pushes data into the StateMachine
Each state machine consists of an input and output shift register (called the ISR and OSR respectively), and two scratch registers (X and Y) which can be used as loop counters among other things. There is a program counter to keep track of the current program step and a clock divider and control logic. The shift registers can be programmed to shift in either direction and to optionally automatically push or pull data to or from their respective FIFOs once a specified number of bits is clocked in or out.


what i a shift register??
A shift register is a type of digital circuit using a cascade of flip-flops where the output of one flip-flop is connected to the input of the next. They share a single clock signal, which causes the data stored in the system to shift from one location to the next. By connecting the last flip-flop back to the first, the data can cycle within the shifters for extended periods, and in this configura... Wikipedia
and another source is https://www.geeksforgeeks.org/shift-registers-in-digital-logic/

Applications of Shift Registers
The shift registers are used for temporary data storage.
The shift registers are also used for data transfer and data manipulation.
The serial-in serial-out and parallel-in parallel-out shift registers are used to produce time delay to digital circuits.
The serial-in parallel-out shift register is used to convert serial data into parallel data thus they are used in communication lines where demultiplexing of a data line into several parallel lines is required.
A Parallel in Serial out shift register is used to convert parallel data to serial data.
