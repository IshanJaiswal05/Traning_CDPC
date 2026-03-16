# 1. Basic Input and String Concatenation 

a=input("enter any value")
a=input("enter any value")
res =a+a
print(res)

# 2. Extracting the Last Digit

n=int(input("enter any value"))

res =n%10
print(res)

# 3. Sum of Two Digits
#/ no=45
#/ 4 5 
#/ we want ans 9 45

no=int(input("enter any value"))
n1=no%10 #5
n2=no//10 #5
res = n1+n2
print(res)

# 4. Sum of Five Digits
# sum of three digit no 

no=int(input("enter any value"))
n1=no%10 #12345=5
no=no//10 #1234
n2 = no % 10  #4
no=no//10 #123 
n3=no%10  #3
no=no//10 #12 
n4 = no%10 #2 
no=no//10 # 2
n5 = no%10 #1 

res = n1+n2+n3 +n4+n5 
print(res)

# sum of five digint num hw 

# 5. Reversing a Five Digit Number
# reverse the num

no=int(input("enter any value"))
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
# 5 digit reverse hw 
