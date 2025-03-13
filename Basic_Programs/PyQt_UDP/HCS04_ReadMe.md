In your PIO program, the timing of the ultrasonic signal is measured in clock cycles. You use x as a counter, and it decrements in a loop. The key lines are:

python
Copy
Edit
jmp(not_y, "moveOn")  # 1 clock cycle
jmp(x_dec, "land")    # 1 clock cycle
jmp(not_y, "moveOn") checks if the echo pin is still high.
jmp(x_dec, "land") decrements the counter (x) and loops back if the echo is still active.
Each iteration of the loop takes 2 clock cycles.

The 3/2 Factor:
You multiply by 3/2 because:

2 cycles per loop iteration: jmp instructions each take 1 cycle.
1 extra cycle for the initial state check: When the echo pin goes high, the state machine spends 1 extra cycle detecting that initial transition.
This means the total cycles counted include an initial overhead of 1 extra cycle, so on average, the effective cycles correspond to 1.5 cycles per iteration, hence multiplying by 3/2.

Why Divide by 2 for Distance?
Since sound waves travel to the target and back, you only care about the one-way trip distance, so dividing by 2 gives the actual distance to the object.

Distance Calculation:
The formula:

distance
=
clockCycles
×
0.0342
2
distance= 
2
clockCycles×0.0342
​	
 
comes from:

Sound travels at ~342 m/s (0.0342 cm/µs).
Your state machine runs at 1 MHz (1 cycle = 1 µs).
The 3/2 factor adjusts for the cycle counting behavior, and dividing by 2 accounts for the round-trip travel.

Key Insights:
in_(pins, 1) just reads the pin state (1 cycle), but most cycles come from the loop.
sm.get() returns the inverted x counter value, giving you the elapsed cycles.
Multiplying by 3/2 corrects the clock cycle count, accounting for loop structure and initial transition.

The in_(pins, 1) instruction is inside the loop, so it gets executed on every iteration, adding 1 cycle each time through the loop.

Here’s the breakdown:

1 cycle for in_(pins, 1) to read the echo pin state.
1 cycle for jmp(not_y, "moveOn") to check if the echo signal is still high.
1 cycle for jmp(x_dec, "land") to decrement the counter and loop back.
That makes 3 cycles per loop iteration, and since the actual distance calculation only needs the time the echo pin is high, multiplying by 3/2 corrects for those 3 cycles in the loop.

The time between sending and receiving the pulse tells you the distance, using the formula:

Distance
=
Time
×
Speed of Sound
2
Distance= 
2
Time×Speed of Sound
​	
 
The division by 2 accounts for the round trip (to the target and back).

Your PIO State Machine Code
In your pulse_program, you’re using a PIO state machine to handle the timing. The critical section is:

label("land")
in_(pins,1)      # 1 clock cycle
mov(y,isr)       # 1 clock cycle
jmp(not_y,"moveOn") # 1 clock cycle
jmp(x_dec,"land")   # 1 clock cycle

Why Multiply by 3?
The reason for multiplying by 3 is because every iteration of your timing loop (land) takes 3 clock cycles:

in_(pins, 1) → 1 cycle
mov(y, isr) → 1 cycle
jmp(not_y, "moveOn") (or jmp(x_dec, "land")) → 1 cycle
So, for each iteration of the loop, it takes 3 cycles. When you call sm.get(), you retrieve the number of iterations the loop ran, not the actual time. Therefore, multiplying by 3 gives you the total clock cycles spent in the loop.

Why Divide by 2?
After you get the total clock cycles, you divide by 2 because the measured time includes the pulse going to the target and back. You only want the one-way distance.

Final Distance Calculation
You multiply sm.get() by 3 to account for the clock cycles per loop iteration.
You divide by 2 for the round trip.
You multiply by the speed of sound in cm/µs (0.0342 cm/µs).
clockCycles = sm.get() * 3 / 2
distance = clockCycles * 0.0342

Potential Improvements
More Accurate Timing: Use a higher frequency for more precise timing, though 1 MHz is generally fine.
Avoid Blocking: Use interrupts or a non-blocking loop to avoid stalling the program during the sm.get() call.
Error Handling: Add a timeout to handle cases where no echo is received, preventing infinite waits.
