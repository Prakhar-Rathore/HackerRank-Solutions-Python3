import math
import os
import random
import re
import sys

def squares(a, b):
    count = 0
    end = int(b ** (0.5))
    start = int(a ** (0.5))
    for x in range(start, end + 1):
        if b >= (x * x) >= a:
            count += 1 
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
