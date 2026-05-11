# Day 3 - USB Relay Debugging

## Today I learned

* Difference between Windows and Linux relay software
* `.exe` cannot run directly on Raspberry Pi
* `windows.h` is Windows-only
* How to use:

  * gcc
  * cmake
  * make
* How Linux detects USB serial devices
* How to compile C++ projects on Raspberry Pi

---

# Work Completed

## 1. Tested Windows source code

Tried:

```bash
gcc TestCOM.c -o testcom
```

Error:

```text
windows.h: No such file or directory
```

Conclusion:

* Windows COM code cannot compile on Linux

---

## 2. Identified correct Linux SDK

Used:

```text
USB-RELAY(SourceCodeProjet2)
```

Contains:

* relaycontrol.cpp
* usbrelay.cpp
* serialib.cpp

---

## 3. Installed build tools

```bash
sudo apt update
sudo apt install cmake g++
```

---

## 4. Built Linux relay project

```bash
mkdir build
cd build
cmake ..
make -j4
```

Build successful:

```text
[100%] Built target usbrelay
```

---

## 5. Connected relay via USB

Relay LED turned on successfully.

---

## 6. Detected relay device

Used:

```bash
ls /dev/tty*
```

Detected:

```text
/dev/ttyUSB0
```

This confirms:

* Raspberry Pi detects the relay
* USB serial communication works

---

# Current Problem

Program still shows:

```text
Connection Failed
```

Likely cause:

* relaycontrol.cpp is not connecting to `/dev/ttyUSB0`

---

# Next Step

Modify:

```cpp
relaycontrol.cpp
```

Set serial port manually:

```cpp
"/dev/ttyUSB0"
```
