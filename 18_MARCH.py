# leetcode
# https://leetcode.com/problems/two-sum/
# two sum
""""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

"""
#  420 FIZZBUZZ
# https://leetcode.com/problems/fizz-buzz/
"""
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
# """
# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/
"""
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        answer = []
        sum = 0
        for i in nums:
            sum += i
            answer.append(sum)
        return answer
"""

#amazon
# Next larger element

# Example 1:
# Input:
# N = 4, arr[] = [1 3 2 4]
# Output:
# 3 4 4 -1
# Explanation:
# In the array, the next larger element
# to 1 is 3, 3 is 4, 2 is 4 and for 4 ?
# since it doesn't exist, it is -1.
"""

n = int(input("Enter the number of Elements: "))
a = []
for i in range(n):
    v = int(input("Enter the number: "))
    a.append(v)
b = []
max = 0
for i in range(n):
    if a[i] > max:
        max = a[i]
    b.append(max)
result = []
for i in range(1, n):
    result.append(b[i])
result.append(-1)
print(*result)
"""