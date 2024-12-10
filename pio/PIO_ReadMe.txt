

https://github.com/raspberrypi/pico-micropython-examples/tree/master
Best Reference:: chapter 3 on PIO
https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf
This has very good explanations::
https://github.com/micropython/micropython/blob/master/docs/rp2/tutorial/pio.rst
2 PIO processors/'blocks'  each with 4 statemachines
Execute from a shared instruction area.

 Each state machine is equipped with:
• Two 32-bit shift registers – either direction, any shift count
• Two 32-bit scratch registers
• 4×32-bit bus FIFO in each direction (TX/RX), reconfigurable as 8×32 in a single direction 
• Fractional clock divider (16 integer, 8 fractional bit
• Flexible GPIO mapping
• DMA interface, sustained throughput up to 1 word per clock from system DMA • IRQ flag set/clear/status
Each state machine, along with its supporting hardware, occupies approximately the same silicon area as a standard serial interface block, such as an SPI or I2C controller. 
However, PIO state machines can be configured and reconfigured dynamically to implement numerous different interfaces.



https://docs.micropython.org/en/latest/rp2/quickref.html#programmable-io-pio

Excellent source of info on PIO:
https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf

The Pico-series MicroPython introduces a new @rp2.asm_pio decorator, along with a rp2.PIO class. The definition of a PIO program, 
and the configuration of the state machine, into 2 logical parts:
• The program definition, including how many pins are used and if they are in/out pins. 
This goes in the @rp2.asm_pio definition. This is close to what the pioasm tool from the SDK would generate from a .pio file (but here it’s all defined in Python).
• The program instantiation, which sets the frequency of the state machine 
and which pins to bind to. These get set when setting a SM to run a particular program.
The aim was to allow a program to be defined once and then easily instantiated multiple times (if needed) with different GPIO. Another aim was to make it easy to do basic things without getting weighed down in too much PIO/SM configuration.

All program configuration (eg autopull) is done in the @asm_pio decorator. Only the frequency and base pins are set in the StateMachine constructor.
• [n] is used for delay, .set(n) used for sideset
• The assembler will automatically detect if sideset is used everywhere or only on a few instructions, and set the
SIDE_EN bit automatically
The idea is that for the 4 sets of pins (in, out, set, sideset, excluding jmp) that can be connected to a state machine,
there’s the following that need configuring for each set: 1. base GPIO
2. number of consecutive GPIO
3. initial GPIO direction (in or out pin)
4. initial GPIO value (high or low)
In the design of the Python API for PIO these 4 items are split into "declaration" (items 2-4) and "instantiation" (item 1). In other words, a program is written with items 2-4 fixed for that program (eg a WS2812 driver would have 1 output pin) and item 1 is free to change without changing the program (eg which pin the WS2812 is connected to).
So in the @asm_pio decorator you declare items 2-4, and in the StateMachine constructor you say which base pin to use (item 1). That makes it easy to define a single program and instantiate it multiple times on different pins (you can’t really change items 2-4 for a different instantiation of the same program, it doesn’t really make sense to do that).
To declare multiple pins in the decorator (e.g. the count: item 2 above), use a tuple. Each item in the tuple specifies items 3 and 4. For example:
In this example:
• there are 3 set pins connected to the SM, and their initial state (set when the StateMachine is created) is: output low, output high, input low (used for open-drain)
• there is 1 sideset pin, initial state is output low
• the 3 set pins start at Pin(15)
• the 1 sideset pin starts at Pin(22)
The reason to have the constants OUT_LOW, OUT_HIGH, IN_LOW and IN_HIGH is so that the pin value and dir are automatically set before the start of the PIO program (instead of wasting instruction words to do set(pindirs, 1) etc at the start).