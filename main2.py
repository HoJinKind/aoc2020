# Using readlines()
file1 = open("input.txt", "r")
Lines = file1.readlines()

count = 0

ls = []
# Strips the newline character
for line in Lines:
    val = int(line.strip())
    ls.append(val)
    # print(int(line.strip()))

    # print("Line{}: {}".format(count, line.strip()))

ls1 = sorted(ls)
print(ls1)

for iter, val1 in enumerate(ls):
    for iter2, val2 in enumerate(ls[iter:]):
        if 2020 - val1 - val2 in ls:
            print(val1)
            print(val2)
            val3 = 2020 - val1 - val2
            print(val3)
            print(val1 * val3 * val2)
