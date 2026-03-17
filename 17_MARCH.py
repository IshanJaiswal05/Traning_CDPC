# # Roy and Profile Picture
# https://www.hackerearth.com/practice/basic-programming
# /input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/
"""
l=int(input())
n=int(input())
for x in range(n):
    W,H = map(int,input().split())

    if W < l or H < l:
        print("UPLOAD ANOTHER")
    elif W == H:
        print("ACCEPTED")
    else:
        print("CROP IT")
       """

# https://www.hackerearth.com/problem/algorithm/monk-and-rotation-3-bcf1aefe/
# logic
"""
arr=[12,312,3,123,123]
for i in range(10):
       print(arr,end=" ")
print(arr) #[12,312,3,123,123]
print(*arr)  #12 312 3 123 123 
"""
#    0 1 2 3 4


# Monk and Rotation
# n=int(input("enter the number of elements"))
# arr[n]

"""
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2
        
        arr = input_data[idx : idx + n]
        idx += n
        
        k %= n
        
        if k == 0:
            print(*(arr))
        else:
            res = arr[-k:] + arr[:-k]
            print(*(res))

if __name__ == "__main__":
    solve()
"""

#Toggle string 
#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output
# /practice-problems/algorithm/modify-the-string/?utm_source=chatgpt.com
"""
S = input()
result ="" 
for ch in S:
    if ch.islower():
        result +=ch.upper()
    else:
        result +=ch.lower()
print(result)
"""
#find the majority element:
# question: find the majority elemrnt(element that appears more than n/2 times) 
# in an array. 
# sample input: [3,3,4,2,4,4,2,4,4]
# expect output : majority element : 4
"""
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
majority = None
count = 0 
for i in arr:
    if count == 0:
        majority = i
    count += 1 if i == majority else -1
if arr.count(majority) > len(arr) // 2:
    print(majority)
else:
    print("No majority element found")

"""
# product of array except self:
# question 
# given an array ,return an array where each element is the product of 
# of all elements in array execpt itself 
# sample input: [1,2,3,4]
# expected output:[24,12,8,6]
arr = list(map(int, input().split()))
n = len(arr)
result = [1] * n

left = 1
for i in range(n):
    result[i] = left
    left *= arr[i]

right = 1
for i in range(n - 1, -1, -1):
    result[i] *= right
    right *= arr[i]

print(result)