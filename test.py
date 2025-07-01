import math
import time
import os
print("Hello Adesh")
colors = ["\033[91m", "\033[93m", "\033[92m", "\033[96m", "\033[94m", "\033[95m"]
reset = "\033[0m"

for i in range(1000):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(-12, 12):
        for x in range(-40, 40):
            angle = math.atan2(y, x)
            radius = math.sqrt(x ** 2 + y ** 2)
            char = '*' if int(radius) % 4 == int(i/4) % 4 else ' '
            color = colors[int(angle * 3 + i) % len(colors)]
            print(color + char + reset, end='')
        print()
    time.sleep(0.05)
