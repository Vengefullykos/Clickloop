# Click.py User Manual

## Overview

`click.py` is a Python script that allows users to simulate mouse clicks and keyboard key presses via the command line. Users can choose to click at a fixed mouse position or allow free movement of the mouse for clicking. Additionally, users can simulate pressing any key, including commonly used special keys.

## System Requirements

- Python 3.x
- `pynput` library

## Installation Steps

### 1. Install Python 3

- **Windows**:
  1. Download the Python 3 installer from the [Python official website](https://www.python.org/downloads/).
  2. During installation, check the "Add Python to PATH" option.

- **macOS**:
  1. Install using Homebrew (if Homebrew is not installed, please install it first):
     ```bash
     brew install python
     ```

- **Linux**:
  1. Install using the package manager (for example, on Ubuntu):
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

### 2. Install the `pynput` Library

Run the following command in the terminal or command prompt:

```bash
pip3 install pynput
```

## Usage

### Running the Program

In the terminal or command prompt, run the program using the following command format:

```bash
python3 click.py {mouse,keyboard} presses_per_second duration [position ...]
```

### Parameter Description

- **action**: Choose the type of action, which can be `mouse` or `keyboard`.
- **presses_per_second**: The number of clicks or key presses per second (integer).
- **duration**: The duration (seconds, integer).
- **position**: The x and y coordinates of the mouse position (only required when selecting `mouse`, two floating-point numbers).

### Examples

1. **Clicking at a fixed mouse position**:
   ```bash
   python3 click.py mouse 10 5 400 300
   ```
   This will click at position `(400, 300)` 10 times per second for 5 seconds.

2. **Allowing the user to freely move the mouse for clicking**:
   ```bash
   python3 click.py mouse 10 5
   ```
   This will click at the user's current mouse position 10 times per second for 5 seconds.

3. **Simulating keyboard key presses** (any key can be specified):
   ```bash
   python3 click.py keyboard 10 5 k
   ```
   This will press the `k` key 10 times per second for 5 seconds.

   Other keys can also be pressed, for example:
   ```bash
   python3 click.py keyboard 10 5 enter
   ```

### Notes

- Ensure you have permission to control the mouse and keyboard when running the script.
- On some systems, you may need to run the script with administrator privileges.
- Use caution to avoid running the key simulator in places where you do not want input.
- To stop the program, you can use `Ctrl+C`, which will interrupt the program and stop the operation.

## Conclusion

`click.py` is a simple yet powerful tool suitable for scenarios that require automation of mouse clicks and keyboard input. Please use it according to your needs and follow the instructions above for installation and operation.
