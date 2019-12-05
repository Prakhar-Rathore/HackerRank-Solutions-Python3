import math
import os
import random
import re
import sys

def superReducedString(s):
    x = 1
    while x < len(s):
        if s[x] == s[x - 1]:
            s = s[ :x-1] + s[x + 1: ]
            x = 0
        x += 1
    if len(s) == 0:
        return "Empty String"
    else:
        return s    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
