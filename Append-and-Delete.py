import math
import os
import random
import re
import sys


def appendAndDelete(s, t, k):
    if len(s) + len(t) < k:
        return "Yes"
    n = len(s) if len(t) > len(s) else len(t)
    for x in range(n):
        if s[x] == t[x]:
            continue
        else:
            break
    moves = len(s) + len(t) - (2 * x)
    if int(moves) == k:
        return "Yes"
    elif int(moves) < k and int(moves) % 2 == k % 2:
        return "Yes"
    else:
        return "No"
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
