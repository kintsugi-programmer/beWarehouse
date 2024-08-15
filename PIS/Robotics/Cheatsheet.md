## Boilerplate

```cpp
// Arduino Sketch Boilerplate

// Include necessary libraries
// Libraries provide additional functionality for sensors, actuators, communication, etc.
#include <Arduino.h>  // Required for Arduino framework

// Define global variables/constants
const int ledPin = 13;  // Define the pin connected to the LED

// Setup function - runs once when the Arduino is powered on or reset
void setup() {
  // Initialize serial communication at 9600 baud rate for debugging
  Serial.begin(9600);

  // Set the LED pin as an output
  pinMode(ledPin, OUTPUT);

  // Print a message to the serial monitor
  Serial.println("Setup complete. Ready to start...");
}

// Loop function - runs repeatedly after setup() completes
void loop() {
  // Your main program logic goes here

  // Example: Blink the LED
  digitalWrite(ledPin, HIGH);  // Turn on the LED
  delay(1000);  // Wait for 1 second
  digitalWrite(ledPin, LOW);   // Turn off the LED
  delay(1000);  // Wait for 1 second
}
```

### Comments Explanation:

1. `#include <Arduino.h>`: This line includes the Arduino framework header file. It's required for every Arduino sketch.

2. `const int ledPin = 13;`: This line declares a constant integer variable named `ledPin` and assigns the value 13 to it. This is the pin connected to the LED.

3. `void setup() {...}`: This is the setup function. It runs once when the Arduino is powered on or reset. Inside this function, you initialize variables, set pin modes, and perform other one-time setup tasks.

4. `Serial.begin(9600);`: This line initializes serial communication with a baud rate of 9600 bits per second. This allows you to communicate with the Arduino via the serial monitor for debugging purposes.

5. `pinMode(ledPin, OUTPUT);`: This line sets the pin mode of `ledPin` as an output. This is necessary because you want to control the LED connected to this pin.

6. `Serial.println("Setup complete. Ready to start...");`: This line prints a message to the serial monitor indicating that the setup is complete and the Arduino is ready to start running the main program logic.

7. `void loop() {...}`: This is the loop function. It runs repeatedly after the `setup()` function completes. Inside this function, you put your main program logic, which typically includes reading sensors, controlling actuators, and making decisions based on sensor readings.

8. `digitalWrite(ledPin, HIGH);`: This line turns on the LED connected to `ledPin` by setting the pin's output to HIGH.

9. `delay(1000);`: This line pauses the program execution for 1000 milliseconds (1 second).

10. `digitalWrite(ledPin, LOW);`: This line turns off the LED connected to `ledPin` by setting the pin's output to LOW.

11. `delay(1000);`: This line pauses the program execution for another 1000 milliseconds.

This boilerplate provides a solid foundation for creating Arduino sketches. You can modify and expand upon it to suit the specific requirements of your projects.

## Code
```
# Arduino Cheatsheet

## Arduino Board Types
- Uno
- Mega
- Nano
- Micro
- Due
- Leonardo
- Yun
- Zero
- 101
- MKR Family
- Gemma

## Arduino IDE Shortcuts
- Ctrl+N - New Sketch
- Ctrl+O - Open Sketch
- Ctrl+S - Save Sketch
- Ctrl+R - Upload Sketch
- Ctrl+Shift+M - Open Serial Monitor

## Arduino Programming Basics

### Structure
- `void setup() { }` - Runs once at startup
- `void loop() { }` - Runs repeatedly

### Variables
- `int` - Integers (-32,768 to 32,767)
- `long` - Long integers (-2,147,483,648 to 2,147,483,647)
- `float` - Floating-point numbers (3.4028235E+38)
- `double` - Double precision floating-point numbers (1.7976931348623157E+308)
- `char` - Single character
- `bool` - Boolean (true or false)
- `String` - String of characters
- `Array` - Collection of variables

### Constants
- `const` - Define constant values

### Control Structures
- `if`/`else` - Conditional statements
- `for` - Loop with counter
- `while` - Loop until condition is false
- `do`/`while` - Loop at least once
- `switch`/`case` - Multiple branch conditionals

### Functions
- `void functionName() { }` - Declare a function
- `return` - Return a value from a function

## Digital I/O

### pinMode()
- `pinMode(pin, mode)` - Configure pin mode
  - Modes: `INPUT`, `OUTPUT`, `INPUT_PULLUP`

### digitalRead()
- `digitalRead(pin)` - Read digital value (HIGH or LOW) from pin

### digitalWrite()
- `digitalWrite(pin, value)` - Write digital value (HIGH or LOW) to pin

## Analog I/O

### analogRead()
- `analogRead(pin)` - Read analog value (0-1023) from pin

### analogWrite() (PWM)
- `analogWrite(pin, value)` - Write analog value (0-255) to PWM pin

## Serial Communication

### Serial.begin()
- `Serial.begin(baud)` - Start serial communication at baud rate

### Serial.print()
- `Serial.print(data)` - Send data over serial

### Serial.println()
- `Serial.println(data)` - Send data + newline over serial

### Serial.read()
- `Serial.read()` - Read incoming serial data

## Time

### millis()
- `millis()` - Returns elapsed time in milliseconds since program start

### micros()
- `micros()` - Returns elapsed time in microseconds since program start

### delay()
- `delay(ms)` - Pause program execution for specified milliseconds

### delayMicroseconds()
- `delayMicroseconds(us)` - Pause program execution for specified microseconds

## Math

### min() and max()
- `min(x, y)` - Returns smallest of x or y
- `max(x, y)` - Returns largest of x or y

### abs()
- `abs(x)` - Returns absolute value of x

### constrain()
- `constrain(x, a, b)` - Limits x to range a-b

### map()
- `map(value, fromLow, fromHigh, toLow, toHigh)` - Re-maps a number from one range to another

### pow()
- `pow(base, exponent)` - Raises base to exponent power

### sq() and sqrt()
- `sq(x)` - Returns square of x
- `sqrt(x)` - Returns square root of x

## Arrays

### Declaring Arrays
- `type arrayName[arraySize];`
- `type arrayName[] = {value1, value2, ...};`

### Accessing Array Elements
- `arrayName[index]`

### Array Size
- `sizeof(arrayName)`

## Strings

### String Object
- `String stringName = "Initial Value";`

### String Functions
- `stringName.length()` - Get string length
- `stringName.charAt(index)` - Get character at index
- `stringName.concat(string2)` - Concatenate strings
- `stringName.equals(string2)` - Compare strings
- `stringName.indexOf(value)` - Find index of value
- `stringName.toLowerCase()` / `stringName.toUpperCase()`
- `stringName.trim()` - Remove leading/trailing whitespace

## Bitwise Operations

### Bitwise AND
- `&` - Bitwise AND

### Bitwise OR
- `|` - Bitwise OR

### Bitwise XOR
- `^` - Bitwise XOR

### Bitwise NOT
- `~` - Bitwise NOT

### Bitshift Left
- `<<` - Shift bits left

### Bitshift Right
- `>>` - Shift bits right

## Libraries

### Including Libraries
- `#include <LibraryName.h>`

### Popular Libraries
- LiquidCrystal (LCD)
- Servo
- Ethernet
- SPI
- Wire (I2C)
- SD (SD Card)

## Interrupts

### attachInterrupt()
- `attachInterrupt(interrupt, function, mode)` - Attach function to interrupt

### detachInterrupt()
- `detachInterrupt(interrupt)` - Detach interrupt

## Power Management

### Sleeping
- `LowPower.idle(...)` - Sleep between clock cycles
- `LowPower.adcSafe(...)` - Sleep while keeping ADC functional
- `LowPower.powerDown(...)` - Put microcontroller into deep sleep
```
### Arduino Basics:

1. **What is Arduino?**
   - Arduino is an open-source electronics platform based on easy-to-use hardware and software.
   - It consists of a physical programmable circuit board (often referred to as a microcontroller) and a development environment that implements the Processing/Wiring language.

2. **Arduino Board Components:**
   - Microcontroller (ATmega series in most Arduino boards)
   - Digital Input/Output Pins
   - Analog Input Pins
   - Power Pins (5V, 3.3V, GND)
   - USB Interface
   - Reset Button

3. **Arduino IDE:**
   - Integrated Development Environment for writing, compiling, and uploading code to Arduino boards.
   - Supports C/C++ programming language.
   - Provides a set of libraries and examples for easy development.

4. **Setup and Loop:**
   - Every Arduino program consists of two main functions: `setup()` and `loop()`.
   - `setup()` function runs once when the Arduino is powered on or reset.
   - `loop()` function runs continuously after `setup()` finishes executing.

### Arduino Programming Basics:

1. **Syntax:**
   - Statements end with a semicolon `;`.
   - Curly braces `{}` define blocks of code.
   - Comments start with `//` for single-line comments or enclosed between `/* */` for multi-line comments.

2. **Data Types:**
   - `int`, `long`, `float`, `double`: Numeric data types.
   - `char`, `String`: Character and string data types.
   - `bool`: Boolean data type.

3. **Variables and Constants:**
   - Variables hold data that can be changed during the execution of the program.
   - Constants hold values that remain constant throughout the program.
   - Variables and constants are declared with their data type followed by their name.

4. **Operators:**
   - Arithmetic: `+`, `-`, `*`, `/`, `%` (Modulus)
   - Relational: `==`, `!=`, `<`, `>`, `<=`, `>=`
   - Logical: `&&` (AND), `||` (OR), `!` (NOT)
   - Assignment: `=`, `+=`, `-=`, `*=`, `/=`

### Arduino Functions and Libraries:

1. **Digital I/O:**
   - `pinMode(pin, mode)`: Configures the specified pin to behave as an input or output.
   - `digitalWrite(pin, value)`: Writes a HIGH or LOW value to a digital pin.
   - `digitalRead(pin)`: Reads the digital value (HIGH or LOW) from a pin.

2. **Analog I/O:**
   - `analogRead(pin)`: Reads the analog value (0 to 1023) from an analog pin.
   - `analogWrite(pin, value)`: Writes a PWM value (0 to 255) to a PWM-capable pin.

3. **Time Functions:**
   - `delay(ms)`: Pauses the program for the specified number of milliseconds.
   - `millis()`: Returns the number of milliseconds since the Arduino board started running.
   - `micros()`: Returns the number of microseconds since the Arduino board started running.

4. **Serial Communication:**
   - `Serial.begin(baudRate)`: Initializes serial communication with the specified baud rate.
   - `Serial.available()`: Returns the number of bytes available for reading from the serial port.
   - `Serial.read()`: Reads the next byte of incoming serial data.
   - `Serial.write(data)`: Sends data over the serial port.

### Additional Tips and Tricks:

- Always include necessary libraries using `#include <LibraryName.h>` at the beginning of your sketch.
- Use meaningful variable and function names for better code readability.
- Keep your code modular by breaking it into smaller functions.
- Comment your code to explain its functionality and make it easier to understand.
- Test your code incrementally and use serial debugging to troubleshoot issues.

This cheat sheet covers the basics of Arduino programming and usage. For more advanced topics such as interrupts, timers, and interfacing with sensors and actuators, you may need to consult additional resources or specific documentation.