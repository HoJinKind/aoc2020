file1 = open("input.txt", "r")
Lines = file1.readlines()
import re

ls = []
# Strips the newline character
counter31 = 0
position31 = 0

counter11 = 0
position11 = 0

counter51 = 0
position51 = 0


counter71 = 0
position71 = 0

alt = True

counter12 = 0
position12 = 0

for index, line in enumerate(Lines):
    val = line.strip()
    if val[position31] == "#":
        counter31 += 1

    if val[position51] == "#":
        counter51 += 1

    if val[position71] == "#":
        counter71 += 1

    if val[position11] == "#":
        counter11 += 1

    position31 = (position31 + 3) % len(val)
    position11 = (position11 + 1) % len(val)
    position51 = (position51 + 5) % len(val)
    position71 = (position71 + 7) % len(val)
    if alt:
        if val[position12] == "#":
            counter12 += 1
        position12 = (position12 + 1) % len(val)
    alt = not alt


print("final31: ", counter31)


print("final51: ", counter51)


print("final11: ", counter11)


print("final71: ", counter71)
print(counter11 * counter12 * counter31 * counter51 * counter71)
