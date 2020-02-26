#!/usr/bin/env python3
fahrenheit = 0
print("华氏温度 摄氏度")
while fahrenheit <= 120:
    celsius = (fahrenheit - 32) / 1.8
    print("{:5d} {:7.2f}".format(fahrenheit,celsius))
    fahrenheit += 3
