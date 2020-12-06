file1 = open("input.txt", "r")
Lines = file1.readlines()
import re


def checker(tempdict):
    info = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if all(name in tempdict for name in info):
        if (
            byr_check(tempdict["byr"])
            and iyr_check(tempdict["iyr"])
            and eyr_check(tempdict["eyr"])
            and hgt_check(tempdict["hgt"])
            and hcl_check(tempdict["hcl"])
            and ecl_check(tempdict["ecl"])
            and pid_check(tempdict["pid"])
        ):
            return True
        else:
            return False
    else:
        return False


def byr_check(byr):
    return 1920 <= int(byr) <= 2002


def hgt_check(hgt):
    val = hgt[:-2]
    metric = hgt[-2:]
    if metric == "cm":
        return 150 <= int(val) <= 193
    elif metric == "in":
        return 59 <= int(val) <= 76
    else:
        return False


def iyr_check(iyr):
    return 2010 <= int(iyr) <= 2020


def eyr_check(eyr):
    return 2020 <= int(eyr) <= 2030


def hcl_check(hcl):
    return re.match("#[a-f\d]{6}", hcl)


def ecl_check(ecl):
    return ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def pid_check(pid):
    return re.match("[\d]{9}", pid)


counter = 0

tempdict = {}
for index, line in enumerate(Lines):
    line = line.strip()

    if line != "":
        line = re.split(" ", line)
        for item in line:
            item = re.split(":", item)
            tempdict[item[0]] = item[1]
    else:
        if checker(tempdict):
            print(counter)
            counter += 1

        tempdict = {}
    if index == (len(Lines) - 1):
        if checker(tempdict):
            print(tempdict)
            counter += 1

        tempdict = {}


print("counter:", counter)


print(hcl_check("#733820"))
if hcl_check("#733820"):
    print(True)


print(pid_check("093154719"))
