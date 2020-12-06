file1 = open("input.txt", "r")
Lines = file1.readlines()
import re


def checker(tempdict):
    info = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if all(name in tempdict for name in info):
        return True
    else:
        return False


counter = 0

tempdict = {}
for index, line in enumerate(Lines):
    line = line.strip()
    if line == "":
        if checker(tempdict):
            print(tempdict)
            counter += 1

        tempdict = {}
    else:
        line = re.split(" ", line)
        for item in line:
            item = re.split(":", item)
            tempdict[item[0]] = item[1]

    if index == (len(Lines) - 1):
        if checker(tempdict):
            print(tempdict)
            counter += 1

        tempdict = {}


print("counter:", counter)
