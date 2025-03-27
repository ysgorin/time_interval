# TimeInterval
A Python class for representing and manipulating time intervals in HH:MM:SS format.

### Features
* Initialize time intervals with hours, minutes, and seconds.
* Perform arithmetic operations (`+`, `-`, `*`) on time intervals.
* Auto-normalize values (e.g., `65 seconds -> 1 minute 5 seconds`).
* Formatted string output (`HH:MM:SS`).

### Usage
``` sh
from time_interval import TimeInterval

# Create TimeInterval objects
t1 = TimeInterval(1, 30, 45)  # 1 hour, 30 minutes, 45 seconds
t2 = TimeInterval(0, 45, 30)  # 45 minutes, 30 seconds

# String representation
print(t1)  # Output: 1:30:45

# Addition
print(t1 + t2)  # Output: 2:16:15

# Subtraction
print(t1 - t2)  # Output: 0:45:15

# Multiplication
print(t2 * 2)  # Output: 1:31:00
```
### Requirements
* Python 3.x

### Installation
Download [`time_interval.py`](time_interval.py) and import it into your project.

### License
[MIT License](LICENSE)