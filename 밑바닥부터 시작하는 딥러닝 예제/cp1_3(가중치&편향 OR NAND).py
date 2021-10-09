import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) ## 가중치
    b = 0.7 ## 편향
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) ## 가중치
    b = -0.2 ## 편향
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print("NAND(0,0) : " + str(NAND(0, 0)))
print("NAND(0,1) : " + str(NAND(0, 1)))
print("NAND(1,0) : " + str(NAND(1, 0)))
print("NAND(1,1) : " + str(NAND(1, 1)))

print("OR(0,0) : " + str(OR(0, 0)))
print("OR(0,1) : " + str(OR(0, 1)))
print("OR(1,0) : " + str(OR(1, 0)))
print("OR(1,1) : " + str(OR(1, 1)))