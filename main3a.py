# Using readlines()
file1 = open("input.txt", "r")
Lines = file1.readlines()
import re

count = 0

ls = []
# Strips the newline character
counter = 0
for line in Lines:
    val = line.strip()
    templs = []
    val = val.replace(" ", ",")
    templs = re.split("-|,", val)
    count = templs[-1].count(templs[-2][0])
    char1 = templs[-1][int(templs[0]) - 1]

    char2 = templs[-1][int(templs[1]) - 1]

    if (char1 == templs[-2][0]) != (char2 == templs[-2][0]):
        counter += 1
        print(templs)
#     ls.append(val)
#     # print(int(line.strip()))

#     # print("Line{}: {}".format(count, line.strip()))
print("count: ", counter)

# ls1 = sorted(ls)
# print(ls1)

# for iter, val1 in enumerate(ls):
#     for iter2, val2 in enumerate(ls[iter:]):
#         if 2020 - val1 - val2 in ls:
#             print(val1)
#             print(val2)
#             val3 = 2020 - val1 - val2
#             print(val3)
#             print(val1 * val3 * val2)
