"""
1. Armstrong Numbers 
Finds and prints all Armstrong numbers between 1 and 10,000 
"""

for i in range(1, 10000):
    no = i
    sum_val = 0
    temp = no

    count = 0
    while(no > 0):
        no = no // 10
        count += 1
    
    no = temp
    while(no > 0):
        rem = no % 10
        sum_val = sum_val + rem**count
        no = no // 10
        
    if temp == sum_val:
        print("Armstrong", i)



"""

2. Single Number Armstrong Check
Checks if a specific user-input number is an Armstrong number 
by summing each digit raised to the power of the total digits.
"""


#check no is amrstrong 
#153= 1^3 + 5^3 + 3^3
   #   = 153
#** = power 
no=int(input("eneter no: "))
sum=0
temp=no

# count logic 
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

"""


3.  Armstrong using Loop 
"""


#for i in range(1,10000):
 ### temp=no

# count logic 
#count=0
#while(no>0):
 #   no=no//10
  #  count+= 1
no = temp
while(no>0):
    rem=no%10
    sum =sum + rem**count
    no=no//10
    

if temp==sum:
    print("armstrog" , i)


"""
4. count numbers


"""
#count the no of digits 
no=int(input("eneter no: "))
count=0
while(no>0):
  
    no=no//10
    count=count + 1
print("count  is ",count)




"""
5. Number Reversal using Loops

"""


#reverse of number using loop
no=int(input("eneter no: "))
rev=0
while(no>0):
    rem=no%10
    rev=rev*10+rem
    no=no//10
print("reverse no  is ",rev)

"""

6. Palindrome Number Verification

"""

# plaindrome 
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
     



#peterson 
# a number is said to be peterson if the sum of factorials of 
# each digit is equal to the sum of the number itself 
# for example 145 
# 145=!1+!4+!5
# + 1+24+120
#145 

no=145 
n1=no%10
no=no//10
n2=no%10
no=no//10
n3=no%10

# jumped to logic building 

"""""
8. Sum of Digits using While Loop

"""

#using  loop
no=int(input("eneter no: "))
sum=0
while(no>0):
 x=no%10 
 sum = sum +x
 no=no//10
    
print("sum no  is ",sum)

