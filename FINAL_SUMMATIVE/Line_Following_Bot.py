# Motor driver pins
const int ENA = 5;  # Left motor speed (PWM)
const int IN3 = 7;  # Left motor direction 1
const int IN4 = 6;  # Left motor direction 2

const int ENB = 3;  # Right motor speed (PWM)
const int IN1 = 9;  # Right motor direction 1
const int IN2 = 8;  # Right motor direction 2

# IR sensor pins
const int leftSensorPin = A1;   # Left IR sensor (analog)
const int rightSensorPin = A0;  # Right IR sensor (analog)

# Constants
const int BASE_SPEED = 150;     # Base speed for both motors (robot goes straight if no turn is needed)
const float Kp = 0.15;          # Proportional gain - controls how sharply robot turns when off the line
                                # Higher Kp = stronger/faster corrections
                                # Lower Kp = smoother but slower correction
const int MIN_SPEED = 60;       # Minimum motor speed to prevent stalling (motors not moving at all)

void setup() {
# Motor pins
  pinMode(ENA, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

# Sensor pins
  pinMode(leftSensorPin, INPUT);
  pinMode(rightSensorPin, INPUT);

# Start serial monitor
  Serial.begin(9600);
}

# Read IR sensor values
void readSensors(int &leftValue, int &rightValue) {
  leftValue = analogRead(leftSensorPin);     # Get analog value from left sensor (0-1023)
  rightValue = analogRead(rightSensorPin);   # Get analog value from right sensor (0-1023)
}

# Set both motors forward
void setMotorDirection() {
  digitalWrite(IN1, HIGH);  # Right motor forward
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);  # Left motor forward
  digitalWrite(IN4, LOW);
}

// Set motor speeds
void setMotorSpeed(int leftSpeed, int rightSpeed) {
  analogWrite(ENA, leftSpeed);  # Set PWM speed for left motor
  analogWrite(ENB, rightSpeed); # Set PWM speed for right motor
}

void loop() {
  int leftValue, rightValue;
  readSensors(leftValue, rightValue);  # Get sensor readings

  int error = leftValue - rightValue;  # How far off-center the robot is
                                       # If left is brighter than right, robot is drifting right

  int turn = Kp * error;               # Multiply error by Kp to get turn strength
                                       # Bigger error = sharper turn

  # Adjust speeds to turn toward the line
  int leftSpeed = constrain(BASE_SPEED - turn, MIN_SPEED, 255);   # If turning right, slow left motor
  int rightSpeed = constrain(BASE_SPEED + turn, MIN_SPEED, 255);  # If turning left, slow right motor

  setMotorDirection();                  # Always set both motors to forward
  setMotorSpeed(leftSpeed, rightSpeed); # Apply the calculated speeds

  # Debug output - prints real-time values to Serial Monitor
  Serial.print("L: ");
  Serial.print(leftValue);            # Print left sensor reading
  Serial.print(" | R: ");
  Serial.print(rightValue);           # Print right sensor reading
  Serial.print(" | LS: ");
  Serial.print(leftSpeed);            # Print left motor speed
  Serial.print(" | RS: ");
  Serial.println(rightSpeed);         # Print right motor speed and end the line

  delay(10);  # Small delay to stabilize the loop
}
