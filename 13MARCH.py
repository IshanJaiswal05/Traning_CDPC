# Simple array sum  hacker rank 
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

# def simpleArraySum(ar):
#     sum=0
#     for i in range(len(ar)):
#         sum=sum+ar[i]
#     return sum
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ar_count = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = simpleArraySum(ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()

# min max array 
#min and max array 
# arr =[]
# n=int(input("Enter the number of Elements"))
# for i in range(n):
#   a=int(input("Enter the number "))
#   arr.append(a)
# arr=sorted(arr)
# print(arr[0],arr[n-1])

# remove duplicates from unsorted array 
# def removeduplicates(arr):
#     ans=[]
#     for i in arr:
#         if i not in ans:
#             ans.append(i)
#     return ans

# if __name__ == '__main__':
#     arr = [int(x) for x in input().split()]
#     print(removeduplicates(arr))


# question is print this output 
# 1 10 
# 2 9
# 4 7 
# 5 6

# using two pinter approach
"""
i=1
j=10
while(i<j):
   print(i,"\t",j)
   i=i+1
   j=j-1
   if i==3:
     continue
   if j==8:
     continue
   print(i)
   print(j)
    
hw  """
"""
break and continue concept 
for i in range(1,11):
    if i==5:
       break 
    print(i)

print("     ")

for i in range(1,11):
    if i==5:
       continue
    print(i)
"""

# question:-
# rearrange positive and negative numbers in given array 
# arrange in alternating fashion 

# sample input : [-1,2,-3,4,5,-6]
# sample output: [-1,2,-3,4,-6,5]
# answer :-

n = int(input("Enter the number of Elements: "))
a = []
for i in range(n):
    v = int(input("Enter the number: "))
    a.append(v)

neg = []
pos = []
for x in a:
    if x < 0:
        neg.append(x)
    else:
        pos.append(x)

b = []
no_neg = len(neg)
no_pos = len(pos)
i = 0
j = 0

while i < no_neg and j < no_pos:
    b.append(neg[i])
    b.append(pos[j])
    i += 1
    j += 1

while i < no_neg:
    b.append(neg[i])
    i += 1

while j < no_pos:
    b.append(pos[j])
    j += 1

print(b)