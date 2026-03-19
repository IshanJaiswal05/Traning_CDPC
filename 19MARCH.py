# https://leetcode.com/problems/palindrome-number/
# palindrome
""""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = abs(x)
        rev = 0
        while n != 0:
            rem = n % 10
            n = n // 10
            rev = rev * 10 + rem
        if x < 0:
            return False
        if rev == x:
            return True
        else:
            return False

"""

# https://leetcode.com/problems/richest-customer-wealth/
# 1672. Richest Customer Wealth
""""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = []
        for i in accounts:
            sum = 0
            for j in range(len(i)):
                sum = sum + i[j]
            ans.append(sum)
        return max(ans)

 """
# https://www.hackerearth.com/practice/basic-programming
# /input-output/basics-of-input-output/practice-problems/algorithm/find-product/
# hackerearth
"""
N = int(input())
A = list(map(int, input().split()))
ten = 1000000007
sum = 1
for x in A:
    sum = (sum * x) % ten
print(sum)

"""
# hackerank
# https://www.hackerrank.com/challenges/staircase/problem
# Staircase
"""

def staircase(n):
    for i in range(1, n + 1):
        print((n - i) * ' ' + i * '#')

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

"""

# create a maxtrix such that row wise and coloum wise both the answer should be 15 
# 8  1  6
# 3  5  7
# 4  9  2

# https://www.hackerrank.com/challenges/mini-max-sum/problem
# hackerank 
# Mini-Max Sum
"""
def miniMaxSum(arr):
   def miniMaxSum(arr):
    res=[]
    s=0
    for i in range(len(arr)):
        s=sum(arr)-arr[i]
        res.append(s)
    print(min(res),max(res))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

"""
# Birthday Cake Candles
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

"""
def birthdayCakeCandles(candles):
     max1=max(candles)
     ans=candles.count(max1)
     return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

"""

# https://www.hackerrank.com/challenges/time-conversion/problem
# Time Conversion
"""
def timeConversion(s):
    period = s[-2:]
    hr, minutes, seconds = s[:-2].split(":")

    if period == "AM":
        if hr == "12":
            hr = "00"
    else:
        if hr != "12":
            hr = str(int(hr) + 12)

    return f"{hr}:{minutes}:{seconds}"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
"""