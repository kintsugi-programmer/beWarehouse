# Arduino

[ArdProg.md](ArdProg.md)
[Cheatsheet.md](Cheatsheet.md)
[IDE.md](IDE.md)
[Intro.md](Intro.md)
[README.md](README.md)

## Class 1 : aside ppt
# Additional Uses of Arduino and Important Concepts

## Aesthetics and Wearable Technology
Arduino boards like LilyPad can be used for wearable technology applications. They can be sewn into clothing or accessories, allowing for the integration of electronics and interactive elements into fashion and wearable designs.

## Signals: Analog vs. Digital
- **Analog**: Analog signals represent data at every point in time, forming a continuous waveform. Examples include sensor readings like temperature, light, or sound.
- **Digital**: Digital signals are discrete values, defined by the manufacturer or system. They typically represent binary states (0 or 1, HIGH or LOW).

## Pins and Current Considerations
Arduino pins have current limitations that must be considered:
- Most digital pins can safely source or sink up to 40mA of current.
- Trying to drive high-current devices like motors directly from digital pins can damage the pins.
- For higher current requirements, use analog pins or external power sources and control circuits.

### Power Supply Options
Arduino boards can be powered in two ways:
1. **USB Cable**: When connected to a computer or power bank via USB, the board draws power from the USB port.
2. **External Power Supply**: An external power supply (e.g., battery pack, wall adapter) can be connected to the board's power pins for standalone operation.

## Components and Sensors

### Light-Dependent Resistor (LDR)
An LDR is a resistor whose resistance varies depending on the amount of light it receives. LDRs are commonly used in light-sensing circuits and can be interfaced with Arduino using analog pins and the `analogRead()` function.

### Analog-to-Digital Converter (ADC)
The ADC is a component that converts analog signals (like those from sensors) into digital values that can be processed by the microcontroller. Arduino boards have built-in ADCs that allow reading analog inputs through the `analogRead()` function.

## Arduino IDE and Programming

### Serial Monitor
The Serial Monitor is a tool within the Arduino IDE that allows you to send and receive data over the serial communication channel. It's useful for debugging, displaying sensor values, or sending commands to the Arduino.

### Writing Code
Before writing code, it's a good practice to outline the algorithm or logic on paper first. This can help avoid common pitfalls and ensure a clear understanding of the program flow.

Arduino programs run in a linear fashion, executing code from top to bottom. While it's possible to write procedural code, it's recommended to follow Object-Oriented Programming (OOP) principles whenever possible for better code organization and maintainability.

### Interrupts
Interrupts are a way to respond to external events or signals in real-time, without having to constantly check for them in the main program loop. Arduino supports hardware interrupts on specific pins (typically digital pins 2 and 3), which can be used to trigger an Interrupt Service Routine (ISR) when a signal is detected.

### Digital Pin Modes
When configuring digital pins as inputs, there are two modes available:
1. `INPUT`: The pin will read the actual voltage present on the pin.
2. `INPUT_PULLUP`: The pin has an internal pull-up resistor enabled, which holds the pin at a HIGH state (5V) when nothing is connected. This mode is useful for switch or button inputs.

### Voltage Thresholds
Arduino boards operate at 5V logic levels:
- Voltages between 0V and 1.5V are interpreted as LOW (0).
- Voltages between 4V and 5.5V are interpreted as HIGH (1).

## Finding Project Ideas
There are several ways to find inspiration for Arduino projects:

1. **Online Resources**: Platforms like YouTube and instructional websites often feature project tutorials and ideas that have been implemented before. While not wholly original, these can serve as a starting point for learning and customization.

2. **Research Publications**: Explore research papers, theses, or publications from universities and academic institutions. These can provide insights into novel applications and cutting-edge projects developed by students and researchers.

When starting with Arduino, it's generally recommended to begin with smaller projects and gradually work your way up to more complex endeavors. Small projects allow you to learn and contribute incrementally, building confidence and skills along the way.
