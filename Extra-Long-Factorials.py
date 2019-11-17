import math
import os
import random
import re
import sys


def extraLongFactorials(n):
    factorial = 1
    if n > 0:
        for x in range(1, n + 1):
            factorial *= x
    else:
        return 1
    return factorial


if __name__ == '__main__':
    n = int(input())
    result = extraLongFactorials(n)
    print(result)
