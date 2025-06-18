# LINE FOLLOWING ROBOT

## Purpose
Use two IR sensors and proportional control with error averaging to follow a black line smoothly using two DC motors.

## Creator
- **Author:** Kamal Azeemi  
- **Created:** 18-Jun-2025  
- **Updated:** 18-Jun-2025

## Features
- Reads analog input from left and right IR sensors (`A1` and `A0`).
- Calculates error using: `error = leftValue - rightValue`.
- Applies proportional control with smoothing: `turn = Kp * averageError`.
- Stores the last 5 error values in a list (array) for more stable motion.
- Calculates average error to reduce sudden changes in direction.
- Modular code broken into custom functions:
  - `readSensors()` – Reads analog values from the IR sensors
  - `setMotorDirection()` – Sets motor direction forward
  - `setMotorSpeed()` – Applies PWM speed to both motors
  - `getAverageError()` – Averages recent error values

- Example Output:
   - `L: 850 | R: 200 | AvgErr: 650 | LS: 52 | RS: 248`  
   - `L: 900 | R: 900 | AvgErr: 0   | LS: 150 | RS: 150`

## Requirements
- Arduino Uno or compatible board
- L298N Motor Driver
- 2x IR Sensors (Analog Output)
- 2x DC Motors
- External battery pack (for motors)
- Arduino IDE

## Usage
1. Connect the components as per the defined pins in the code.
2. Open Arduino IDE and upload the sketch to the board.
3. Open Serial Monitor at 9600 baud to observe real-time feedback.
4. Place the robot on a black line and observe behavior.

### TO RUN:
```bash
1. Connect Arduino via USB
2. Select the correct board and port in Arduino IDE
3. Click "Upload"
4. Watch your robot follow the line with stable correction
