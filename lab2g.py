#!/usr/bin/env python3
# Author: Haider ali
# Author ID: Hali129
# Date Created: 2024/05/31

import sys

if len(sys.argv) > 2:
    print("Error: Too many arguments provided")
    sys.exit()

try:
    if len(sys.argv) == 2:
        timer = int(sys.argv[1])
    else:
        timer = 3  # Default countdown number
except ValueError:
    print("Error: Argument must be a valid number")
    sys.exit()

if timer <= 0:
    print("Error: The number must be greater than zero")
    sys.exit()

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
