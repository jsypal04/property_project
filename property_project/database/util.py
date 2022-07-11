import math

# radius of earth in meters
RADIUS = 6371000

# uses the haversine formula
# the coordinates MUST be in radians NOT degrees
def hav(p1, p2, RADIUS):
    return (2 * RADIUS) * math.asin(math.sqrt((math.sin((p2[0] - p1[0]) / 2) ** 2) + math.cos(p1[0]) * math.cos(p2[0]) * (math.sin((p2[1] - p1[1]) / 2) ** 2)))

def str_to_num(str):
    num = ""
    for char in str:
        if (char != ",") and (char != "$"):
            num += char

    return float(num)

def float_to_str(num):
    num = str(int(num))

    neg = "N"

    if num[0] == "-":
        num = num[1:]
        neg = "Y"


    num2 = ""

    i = len(num) - 1
    while i >= 0:
        num2 += num[i]

        i -= 1

    num3 = ""
    for i in range(len(num2)):
        num3 += num2[i]
        if (i + 1) % 3 == 0:
            num3 += ","

    num4 = ""
    j = len(num3) - 1
    while j >= 0:
        num4 += num3[j]

        j -= 1

    if num4[0] == ",":
        num4 = num4[1:]

    if neg == "Y":
        num4 = "-" + num4

    return num4


if __name__ == "__main__":
    n = -126270.0

    print(float_to_str(n))
