# Log of progress toward making autnomous vehicle
## Develop pan tilt servo control- first enter parameters
## check out map() method
 ## linear equations woking with mini pan tilt from adafruit

 Create Servo library

 Joystick control of both servos

 possibly track on a colored object using trackbars


 Review Bluetooth 
// Armuino --- Pan and Tilt ---
// Playlist: https://www.youtube.com/playlist?list=PLRFnGJH1nJiIMaqnOdfmMBxcTVbqow-A8
//
// How to Control Pan and Tilt Mount with 2-Directional Joystick 
// https://www.youtube.com/watch?v=jFOBzBefVTc
//https://www.youtube.com/watch?v=jFOBzBefVTc
#include <Servo.h>

Servo horzServo; // Create a servo object for the pan (horizontal) servo
Servo vertServo; // Create a servo object for the tilt (vertical) servo

int horzPin = 0; // Analog input for the joystick horizontal axis
int vertPin = 1; // Analog input for the joystick vertical axis
int vertVal; // Value read from the vertical axis
int horzVal; // Value read from the horizontal axis

// Setup
void setup()
{
  horzServo.attach(9); // Use pin 9 PWM output for horizontal servo
  vertServo.attach(10); // Use pin 10 PWM output for vertical servo

  /* Init Serial port */
  Serial.begin(115200);
}

// Main program loop
void loop()
{
  horzVal = analogRead(horzPin); // Read joystick horizontal position
  horzVal = map(horzVal, 0, 1023, 0, 179); // Scale reading to servo range
  horzServo.write(horzVal); // Move servo to required position

  vertVal = analogRead(vertPin); // Read joystick horizontal position
  vertVal = map(vertVal, 0, 1023, 0, 179); // Scale reading to servo range
  vertServo.write(vertVal); // Move servo to required position

  Serial.print("Position X, Y: "); 
  Serial.print(horzVal);
  Serial.print(" , "); 
  Serial.print(vertVal);
  Serial.println();
  
  delay(15); // Give servos time to settle
}


# 🥵 scaling functrion for motors
can you show this using real numbers.  let us assume a resolution go 4095  and frequency go 1000 hz
## Example of the Exponential Scaling Formula with Real Numbers

Let's see how the formula 

\[
\text{Speed} = \text{max\_speed} \times (1 - e^{-k \cdot \text{input}})
\]

works using concrete values. In this example, we’ll assume:

- **Resolution**: 4095 (This will be our maximum speed)
- **Frequency**: 1000 Hz (This will influence the control rate but won't directly affect our calculations here)
- **Scaling Factor \( k \)**: Let’s choose \( k = 5 \) for this example.
- **Input**: Values between 0 and 1 to represent the normalized input.

### Step 1: Setting Up Parameters

- **max_speed** = 4095
- **k** = 5

### Step 2: Calculate Speed for Different Input Values

Let’s calculate the speed for various input values: 0, 0.25, 0.5, 0.75, and 1.

#### Case 1: Input = 0

\[
\text{Speed} = 4095 \times (1 - e^{-5 \cdot 0}) = 4095 \times (1 - e^{0}) = 4095 \times (1 - 1) = 0
\]

#### Case 2: Input = 0.25

\[
\text{Speed} = 4095 \times (1 - e^{-5 \cdot 0.25}) = 4095 \times (1 - e^{-1.25})
\]

Calculating \( e^{-1.25} \):

\[
e^{-1.25} \approx 0.2865 \quad (\text{using a calculator})
\]

Then,

\[
\text{Speed} = 4095 \times (1 - 0.2865) = 4095 \times 0.7135 \approx 2923.7325 \quad (\text{approximately } 2924)
\]

#### Case 3: Input = 0.5

\[
\text{Speed} = 4095 \times (1 - e^{-5 \cdot 0.5}) = 4095 \times (1 - e^{-2.5})
\]

Calculating \( e^{-2.5} \):

\[
e^{-2.5} \approx 0.0821
\]

Then,

\[
\text{Speed} = 4095 \times (1 - 0.0821) = 4095 \times 0.9179 \approx 3756.1455 \quad (\text{approximately } 3756)
\]

#### Case 4: Input = 0.75

\[
\text{Speed} = 4095 \times (1 - e^{-5 \cdot 0.75}) = 4095 \times (1 - e^{-3.75})
\]

Calculating \( e^{-3.75} \):

\[
e^{-3.75} \approx 0.0235
\]

Then,

\[
\text{Speed} = 4095 \times (1 - 0.0235) = 4095 \times 0.9765 \approx 3994.1175 \quad (\text{approximately } 3994)
\]

#### Case 5: Input = 1

\[
\text{Speed} = 4095 \times (1 - e^{-5 \cdot 1}) = 4095 \times (1 - e^{-5})
\]

Calculating \( e^{-5} \):

\[
e^{-5} \approx 0.0067
\]

Then,

\[
\text{Speed} = 4095 \times (1 - 0.0067) = 4095 \times 0.9933 \approx 4068.64 \quad (\text{approximately } 4069)
\]

### Summary of Results

| **Input** | **Speed**       |
|-----------|-----------------|
| 0         | 0               |
| 0.25      | 2924            |
| 0.5       | 3756            |
| 0.75      | 3994            |
| 1         | 4069            |

### Conclusion

The output speeds smoothly transition from 0 to nearly **4095** as the input increases from 0 to 1. This gradual scaling is useful for applications where a smooth ramp-up is desired, such as controlling the speed of a motor or fading an LED. The exponential decay function alone provides a non-linear yet visually pleasing transition, improving user experience significantly.

## Comparing Logarithmic Growth vs. Exponential Scaling for LED Brightness Control

You’ve implemented a logarithmic approach to control LED brightness using a potentiometer in your MicroPython script. Below, I’ll analyze the advantages and disadvantages of using this method compared to the exponential scaling formula:

### Current Method: Logarithmic Growth with PWM

**Advantages:**

1. **Perceived Brightness Control**: 
   - This method replicates a human perception of brightness more accurately since our eyes perceive changes in light intensity logarithmically. The logarithmic approach helps create a smoother visual experience.
  
2. **Controlled Steps**:
   - By dividing the brightness into discrete steps (e.g., using an exponent ranging from 0 to 16), you can achieve a clear and distinct differentiation between levels. This is particularly useful for applications where you want specific brightness levels.

3. **Simple Calculation**:
   - The use of a straightforward exponentiation, \( y = 2^{\text{exponentVal}} \), makes it easy to visualize and understand how brightness levels are manipulated.

4. **Direct Mapping**:
   - The transformation from potentiometer values to brightness levels uses direct mapping using slopes, making the implementation clean.

**Disadvantages:**

1. **Non-linear Behavior**:
   - The logarithmic growth can make it hard to achieve fine control at lower brightness levels since the output growth is non-linear, potentially resulting in larger jumps in brightness at lower levels.

2. **Calibration Needs**:
   - The slope formula \((.00026046 \cdot \text{potVal} - 0.733)\) may require adjustment and calibration to ensure it works across different potentiometers or setups.

### Proposed Method: Exponential Scaling Formula

**Advantages:**

1. **Smoother Transition**:
   - The exponential scaling function \( \text{Speed} = \text{max\_speed} \times (1 - e^{-k \cdot \text{input}}) \) provides a continuous and smooth transition from 0 to max speed, making it feel very natural during increases and decreases.

2. **Fine Control Over Speed**:
   - The parameter \( k \) in the formula allows for easy adjustment of the rate of change, providing a high level of customization for responsiveness. Increasing or decreasing \( k \) can make transitions faster or slower without altering the overall structure.

3. **Wide Range**:
   - The formula allows for a wide dynamic range when compressed, which can be particularly useful when working with lower resolutions or limited-state changes.

4. **Ease of Implementation**:
   - Since this is a standard mathematical function available in many programming environments, it can often be implemented with minimal custom code, benefiting from established performance characteristics.

**Disadvantages:**

1. **Complexity**:
   - Unlike the logarithmic approach, it requires understanding of both exponential growth and decay concepts, which might be less intuitive for newcomers.

2. **Less Fine Control at Extremes**:
   - Although providing smooth transitions, it may yield less granular control at certain stages, particularly near minimum and maximum values, unless carefully fine-tuned.

### Summary Comparison

| **Aspect**                    | **Logarithmic Growth**                             | **Exponential Scaling**                         |
|-------------------------------|----------------------------------------------------|------------------------------------------------|
| **Perceived Brightness**      | More aligned with human perception                  | Offers smooth transitions                        |
| **Control Steps**             | Clear differentiation in steps                     | Wide dynamic range with fewer distinct steps    |
| **Calculation Complexity**     | Simpler calculations, but requires calibration     | Requires understanding of exponential functions  |
| **Adjustment**                | Manual slope calibration needed                     | Parameter \( k \) allows easy tuning            |
| **Output Behavior**           | Non-linear at lower values                          | Smooth and continuous rise                       |

### Conclusion

Both methods offer unique advantages based on the specific application and user needs. The logarithmic approach you've used is effective for controlling LED brightness with a clear understanding of human perception. In contrast, the exponential scaling method provides smooth transitions and flexible control, which could be beneficial in different contexts. Your choice should align with the behavior you want to achieve in your application, along with ease of implementation and control requirements.

## Example of the Exponential Scaling Formula with Real Numbers

Let's see how the formula 

\[
\text{Speed} = {max\_speed} \times (1 - e^{-k \cdot \text{input}})
\]

works using concrete values. In this example, we’ll assume:

- **Resolution**: 4095 (This will be our maximum speed)
- **Frequency**: 1000 Hz (This will influence the control rate but won't directly affect our calculations here)
- **Scaling Factor \( k \)**: Let’s choose \( k = 5 \) for this example.
- **Input**: Values between 0 and 1 to represent the normalized input.

### Step 1: Setting Up Parameters

- **max_speed** = 4095
- **k** = 5

### Step 2: Calculate Speed for Different Input Values

Let’s calculate the speed for various input values: 0, 0.25, 0.5, 0.75, and 1.

#### Case 1: Input = 0

\[
\text{Speed} = 4095 \times (1 - e^{-5 \cdot 0}) = 4095 \times (1 - e^{0}) = 4095 \times (1 - 1) = 0
\]

#### Case 2: Input = 0.25

\[
\text{Speed} = 4095 \times (1 - e^{-5 \cdot 0.25}) = 4095 \times (1 - e^{-1.25})
\]

Calculating \( e^{-1.25} \):

\[
e^{-1.25} \approx 0.2865 \quad (\text{using a calculator})
\]

Then,

\[
\text{Speed} = 4095 \times (1 - 0.2865) = 4095 \times 0.7135 \approx 2923.7325 \quad (\text{approximately } 2924)
\]

#### Case 3: Input = 0.5

\[
\text{Speed} = 4095 \times (1 - e^{-5 \cdot 0.5}) = 4095 \times (1 - e^{-2.5})
\]

Calculating \( e^{-2.5} \):

\[
e^{-2.5} \approx 0.0821
\]

Then,

\[
\text{Speed} = 4095 \times (1 - 0.0821) = 4095 \times 0.9179 \approx 3756.1455 \quad (\text{approximately } 3756)
\]

#### Case 4: Input = 0.75

\[
\text{Speed} = 4095 \times (1 - e^{-5 \cdot 0.75}) = 4095 \times (1 - e^{-3.75})
\]

Calculating \( e^{-3.75} \):

\[
e^{-3.75} \approx 0.0235
\]

Then,

\[
\text{Speed} = 4095 \times (1 - 0.0235) = 4095 \times 0.9765 \approx 3994.1175 \quad (\text{approximately } 3994)
\]

#### Case 5: Input = 1

\[
\text{Speed} = 4095 \times (1 - e^{-5 \cdot 1}) = 4095 \times (1 - e^{-5})
\]

Calculating \( e^{-5} \):

\[
e^{-5} \approx 0.0067
\]

Then,

\[
\text{Speed} = 4095 \times (1 - 0.0067) = 4095 \times 0.9933 \approx 4068.64 \quad (\text{approximately } 4069)
\]

### Summary of Results

| **Input** | **Speed**       |
|-----------|-----------------|
| 0         | 0               |
| 0.25      | 2924            |
| 0.5       | 3756            |
| 0.75      | 3994            |
| 1         | 4069            |

### Conclusion

The output speeds smoothly transition from 0 to nearly **4095** as the input increases from 0 to 1. This gradual scaling is useful for applications where a smooth ramp-up is desired, such as controlling the speed of a motor or fading an LED. The exponential decay function alone provides a non-linear yet visually pleasing transition, improving user experience significantly.