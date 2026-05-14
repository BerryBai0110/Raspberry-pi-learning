# Day 3 - USB Relay Debugging with Raspberry Pi

## Goal

The goal of today was to:

- connect a USB relay board to Raspberry Pi
- compile the official Linux SDK
- run relay control code
- debug hardware communication issues
- understand embedded Linux workflow

---

# Hardware Used

## Raspberry Pi

Used as the Linux embedded platform.

## USB Relay Board

Model:

SEEIT USB-RELAY04

4-channel USB relay module.

Features:
- USB communication
- 4 relay outputs (K1-K4)
- relay switching
- external power support
- relay driver chip (ULN2803)

## Breadboard + LED

Used to test relay output manually.

---

# Software Environment

## Linux

Worked directly inside Raspberry Pi Linux terminal.

Learned:
- terminal navigation
- compiling source code
- device scanning
- serial device detection

---

# SDK Setup

Downloaded official Linux USB relay SDK source files.

Main files:

- relaycontrol.cpp
- usbrelay.cpp
- usbrelay.hpp
- seriallib.cpp
- seriallib.hpp
- CMakeLists.txt

---

# Build Process

Created build directory:

```bash
mkdir build
cd build
```

Compiled project:

```bash
cmake ..
make -j4
```

Successfully generated executable:

```bash
usbrelay
```

---

# USB Device Detection

Checked connected serial devices:

```bash
ls /dev/tty*
```

Detected:

```bash
/dev/ttyUSB0
```

Also checked USB devices:

```bash
lsusb
```

Detected Prolific USB serial device.

---

# Code Investigation

Opened:

```text
relaycontrol.cpp
```

Learned:
- scanBoard()
- openCom()
- initBoard()
- setState()

Observed board status outputs:

```text
K1 ON
K2 OFF
```

---

# Debugging Process

## Initial Problem

Program compiled successfully but relay board showed:

```text
Connection Failed
```

Later fixed serial device path manually.

---

# Relay Status Issue

After communication succeeded:
- terminal displayed K1/K2 state changes
- but physical relay did not click
- no audible relay switching sound
- no visible hardware response

---

# Hardware Investigation

Learned relay concepts:
- relay coil
- COM / NO / NC terminals
- electromagnetic switching
- relay driver chip ULN2803

Investigated:
- RE pin
- SW pin
- jumper modes
- possible hardware enable modes

---

# Breadboard Testing

Started preparing:
- LED
- resistor
- breadboard
- relay output wiring

Goal:
- verify whether relay output physically switches

---

# Embedded Linux Concepts Learned

## Linux

Linux is the operating system running on Raspberry Pi.

Used:
- terminal
- filesystem
- compiling tools
- device interfaces

---

## Embedded Systems

Embedded systems combine:
- hardware
- software
- electronics
- device communication

This debugging process involved:
- USB communication
- relay hardware
- power considerations
- Linux device control

---

# Important Lessons

## Embedded debugging is different from normal programming

Even if:
- code compiles
- program runs
- commands print correctly

hardware may still fail because of:
- power issues
- jumper configuration
- relay modes
- driver problems
- hardware faults

---

# Current Status

## Successes

- Raspberry Pi setup complete
- Linux SDK compiled
- USB serial device detected
- relay communication partially working
- GitHub repository updated

## Remaining Issue

Relay board still does not physically switch.

Need further testing with:
- external power
- SW/RE jumper configuration
- manual relay triggering
- breadboard verification

---

# Next Steps

- manually test SW trigger
- verify relay COM/NO output
- test external power wiring
- continue embedded Linux debugging
