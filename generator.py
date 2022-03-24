import math
x0 = 1000
a = 24693
c = 3517
K = math.pow(2, 17)

def lcong_randnum(i, num=x0):
    if i == 0: return num / K
    return lcong_randnum(i - 1, ((num * a) + c) % K)
