# 1. Write a program to check whether a number is even or odd.
no=int(input("enter the no :- "))
if no%2==0:
   print("the number is even")
else:
   print("the number is odd ")

# 2. Write a program to find the largest of three numbers.
a = float(input("enter first numbers "))
b = float(input("enter second numbers "))
c= float(input("enter thrid numbers "))
if a> b:
   if a>c:
      print(f"{a} is he largest number")
elif b>a:
    if b>c:
        print(f"{b} is the largest number")
else:
    print("{c} is the largest number ")

# 3. Check whether a number is positive, negative, or zero.
no=int(input("enter the no :- "))
if no> 0:
   
      print(f"{no} is the positive  number")
elif no==0:
   
        print(f"{no} is zero")
else:
    print(f"{no} is the negative number ")

# 4. Write a program to check whether a number is divisible by both 3 and 5.
no=float(input("enter the no :- "))
if no%3== 0 and no%5==0 :
   print(f"{no} is divisble by 3 and 5 ")

# 5. Write a program to print numbers from 1 to N.
no=int(input("enter the no :- "))
for x in range (1, no+1):
    print(x)

# 6. Write a program to print all even numbers from 1 to N.
no=int(input("enter the no :- "))
for x in range (0, no+1, 2):
    print(x)

# 7. Write a program to calculate the sum of first N natural numbers.
no=int(input("enter the no :- "))
sum=0
for x in range (0, no+1, 1):
  sum+=x
print(f"sum of first {no} naturanl number is {sum}")

# 8. Write a program to calculate the factorial of a number.
no=int(input("enter the no :- "))
factorial = 1

if no < 0:
    print("Factorial does not exist for negative numbers.")
elif no == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, no+ 1):
        factorial *= i
    print(f"The factorial of {no} is {factorial}")

# 9. Write a program to print the multiplication table of a number.
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 10. Write a program to count the number of digits in a number.
no=int(input("eneter no: "))
count=0
while(no>0):
  
    no=no//10
    count=count + 1
print("count  is ",count)

