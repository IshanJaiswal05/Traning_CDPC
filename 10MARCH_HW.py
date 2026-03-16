"""
1. 
This program takes the user's name and age as input 
and prints a formatted greeting message.
"""

name=(input("write yourname:"))
age =int(input("write your age :"))
print(f"Hello {name}, you are {age} years old.")

"""
2. 
Calculates the perimeter of a rectangle using the 
length and width provided by the user.
"""
length=int(input("length:- "))
width=int(input("width:- "))
perimeter= 2*(length + width)
print(f"perimeter is {perimeter}")

"""
3. 
Converts a given distance in kilometers into 
meters and centimeters.
"""
no=int(input("Number to convert kilometers into meters and centimeters:- "))
print( no*1000,"meters  ")
print( no*100000,"centimeters  ")

"""
4. 
Takes the prices of three products as input and 
calculates the final bill amount.
"""
ip1=int(input("first product price:- "))
ip2=int(input("first product price:- "))
ip3=int(input("first product price:- "))
bill= ip1+ip2+ip3
print(f"the bill is :- ",bill)

"""
5. 
Converts a user-defined number of hours into 
total minutes and seconds.
"""
hrs=float(input("enter the hours :- "))
min = hrs*60
sec= min*60
print (f"minutes = {min},seconds ={sec}") 

"""
6.
Calculates the area of a triangle based on 
the base and height inputs from the user.
"""
base = float(input("write the base :- "))
height = float(input("write the height :- "))
Area = (base* height) / 2
print(f"Area of triangle is {Area}")

"""
7. 
Takes a number as input and displays its 
doubled and tripled values.
"""
no=float(input("enter the number :- "))
print(f"double of the number  is {no*2} and triple of the number is {no*3}")

"""
8. 
Computes the total number of seconds present 
in a specific number of days.
"""
no=float(input(" enter the number of days :- "))
print(f"number of seconds in the given number of days are:- {no*86400}")

"""
9. 
Takes a value in rupees and converts it into 
the equivalent amount in paise.
"""
n1=float(input("enter the number of rupees to be converted into paisa:- "))
print(f"{n1} of rupees are {n1*100} paias ")

"""
10.
Calculates the total strength of a class by 
adding the number of boys and girls.
"""
boys=int(input("enter the number of boys:- "))
girls=int(input("enter the number of girls:- "))
print(f"Total number of students are {boys + girls}")

# 11. Write a program to reverse a 5-digit number using arithmetic operators.
no=int(input("eneter any value"))
n1=no%10 #12345=5
no=no//10 #1234
n2 = no % 10  #4
no=no//10 #123 
n3=no%10  #3
no=no//10 #12 
n4 = no%10 #2 
no=no//10 # 2
n5 = no%10 #1 
rev = n1*10000+n2*1000+n3*100+n4*10+n5*1
print(rev)

# 12. Write a program to check whether a number is palindrome.
no=int(input("eneter no: "))
rev=0
temp=no
while(no>0):
    rem=no%10
    rev=rev*10+rem
    no=no//10


if temp==rev:
    print("palindrome")
else:
    print("not palindrome ")

# 13. Write a program to find the sum of digits of a number.
no=int(input("eneter no: "))
sum=0
while(no>0):
 x=no%10 
 sum = sum +x
 no=no//10
    
print("sum no  is ",sum)

# 14. Write a program to check whether a number is an Armstrong number.
no=int(input("eneter no: "))
sum=0
temp=no 
count=0
while(no>0):
    no=no//10
    count+= 1
no = temp
while(no>0):
    rem=no%10
    sum =sum + rem**count
    no=no//10
if temp==sum:
    print("armstrog")
else:
    print("not armstrong  ")

# 15. Write a program to print numbers divisible by 7 between 1 and N.
n = int(input("Enter N: "))

for i in range(1, n + 1):
    if i % 7 == 0:
        print(i)