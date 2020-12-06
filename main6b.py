# Using readlines()
file1 = open("input.txt", "r")
Lines = file1.readlines()

count = 0

ls = []
# Strips the newline character
max = 0

lsSeats = []
for line in Lines:
    val = line.strip()
    row = val[:-3]
    col = val[-3:]
    rowPos = 64
    colPos = 4

    for index, rowHop in enumerate(row[:-1]):
        if rowHop == "F":
            rowPos = rowPos - (2 ** (5 - index))  # 64, 32, 16
        else:
            rowPos = rowPos + (2 ** (5 - index))
    if row[-1] == "F":
        rowPos -= 1
    for index, colHop in enumerate(col[:-1]):
        if colHop == "L":
            colPos = colPos - (2 ** (1 - index))
        else:
            colPos = colPos + (2 ** (1 - index))
    if col[-1] == "L":
        colPos -= 1

    count = rowPos * 8 + colPos
    lsSeats.append(count)
for i in range(1, 127):
    for j in range(8):
        if not ((i * 8 + j) in lsSeats):
            if (i * 8 + j + 1) in lsSeats and (i * 8 + j + 1) in lsSeats:
                print("not in", i * 8 + j)

# most front seat will be smallest, most large seat will be biggest.
# just have to check if the seat earlier, and after exist