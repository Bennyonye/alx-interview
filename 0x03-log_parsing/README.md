# 0x03-log_parsing

## Task Overview

Create a Python script that reads input from **stdin**, processes log data line by line, and calculates specific metrics related to file sizes and HTTP status codes.

### Input Format
The input consists of lines with the following format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

### Key Requirements:
1. **Read Input**: The script must continuously read lines from stdin.
2. **Processing**: For every valid line, extract:
   - The **status code** (an integer) and the **file size** (an integer).
   - Any line that doesn't match the expected format should be skipped.
3. **Statistics**: 
   - After every **10 lines** (or if interrupted via **CTRL+C**), print the following:
     - **Total file size**: The sum of all previous file sizes.
     - **Number of lines per status code**: Only for valid status codes (200, 301, 400, 401, 403, 404, 405, 500). If a status code does not appear, do not print it.
   - **Output format**:
     ```
     File size: <total size>
     <status code>: <count>
     ```
   - Status codes should be printed in **ascending order**.

### Edge Cases:
- If the input format does not match, skip that line.
- Handle random or missing status codes by not printing anything for those codes.

### Example Input and Output:
A generator script (`0-generator.py`) simulates log entries:

```bash
$ ./0-generator.py | ./0-stats.py 
```

Sample output:

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
```

After 10 lines, the statistics are printed, and after the next 10 lines, the total file size and status code counts are updated.

If interrupted via `CTRL+C`, the script will print the current stats before exiting:

```
File size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

### Example Generator Script

The example generator (`0-generator.py`) randomly generates IP addresses, dates, status codes, and file sizes:

```python
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
```

This script generates logs that simulate real-world traffic, useful for testing the metrics collection script.

### Expected Behavior
The script should handle large volumes of input gracefully and handle interruptions (e.g., `CTRL+C`). It should be robust, ignoring lines that don't conform to the expected format, and efficiently computing cumulative metrics.

## Author
This project is developed and maintained by **BennyOnye**.