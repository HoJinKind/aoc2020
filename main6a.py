# Using readlines()
file1 = open("input.txt", "r")
Lines = file1.readlines()

count = 0

ls = []
# Strips the newline character
max = 0

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
    if count > max:
        max = count
        print(row, col)
        print(colPos, rowPos)
        print("count:", max)
