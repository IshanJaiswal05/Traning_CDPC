# hacker rank 
#compare the triplets
#https://www.hackerrank.com/challenges/compare-the-triplets/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
""""
def compareTriplets(a, b):
  alice=0
    bob=0
    for i in range (3):
        if a[i]>b[i]:
            ap=ap+1
        elif a[i]<b[i]:
            bp=bp+1
        elif b[i]==a[i]:
            pass
    return alice,bob   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
"""


## A Very Big Sum

# https://www.hackerrank.com/challenges/a-very-big-sum/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys


def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')
    fptr.close()
    """
# Diagonal Difference
#
# https://www.hackerrank.com/challenges/diagonal-difference/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def diagonalDifference(arr):
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0
    for i in range(n):
        primary_sum = sum+  arr[i][i]
        secondary_sum =sum +arr[i][n - 1 - i]
    return (primary_sum - secondary_sum)
   
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
"""
# plus minus sum 

# https://www.hackerrank.com/challenges/plus-minus/problem
#!/bin/python3
""""
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    n = len(arr)

    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1

    print(pos/n)
    print(neg/n)
    print(zero/n)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
"""
"""
# ARRAY SHIFT
n = int(input("Enter the number of Elements OF ARRAY : "))
arr = []
for i in range(n):
    array= int(input("Enter the number: "))
    arr.append(array)
b = int(input("Enter the number of steps: "))
for _ in range(b):
    last_no= arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last_no
for i in range(n):
    print(arr[i])

"""
"""
#Question: Rotate an array to the right by a given number of steps
#sample input: [1,2,3,4,5] rotated by 2 steps 
#expected out: [4,5,1,2,3]
def rotate_right(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

arr = [1,2,3,4,5]
k = 2

result = rotate_right(arr, k)
print(result)

"""