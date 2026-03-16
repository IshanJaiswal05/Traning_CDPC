#  Write a program to demonstrate a basic function without parameters.
def add():
    a=int(input("Enter value: "))
    b=int(input("Enter value: "))
    res=a+b  
    print(res)
if __name__=='__main__':
     add()

#  to return multiple values from a function.
def arithmatic(x,y):
   
    res1=x+y
    res2=x-y
    res3=x*y 
    res4=x/y
    
    return res1,res2,res3,res4
if __name__=='__main__':
    a=int(input("Enter value: "))
    b=int(input("Enter value: "))
    r1,r2,r3,r4=arithmatic(a,b)
    print(r1,r2,r3,r4)

# demonstrate a function with parameters but no return value.
#withnoreturn value 
def add(x,y):
   
    res=x+y  
    print(res)
if __name__=='__main__':
    a=int(input("Enter value: "))
    b=int(input("Enter value: "))
    add(a,b)

#   to demonstrate list operations and slicing.
# ls=[]
# print(type(ls))

# ls=list
# print(type(ls))


# ls=[11,22,33,44]
# print(ls)

# for i in range(len(ls)):
#     print(ls[i])
# for x in ls:
#     print(x)

ls=[11,22,33,44,55,66]
ls.append(77)
ls.append(88)
print(ls)
print(ls[0])
print(ls[-6])


print(ls[2:5])
print(ls[3:6])
print(ls[:6])
print(ls[2:])
print(ls[:])
print(ls[::1])#as it is list 
print(ls[::2])#alternate 
print(ls[::-2]) #  from 88
print(ls[::-1])  # reverses the array or list 

# to reverse a string without built-in functions (Incomplete).
# reverse the Striing
# without shortcut
# without inbuilt function 

s="ishan"
for i in range(s):
    print(s)

#  to demonstrate string slicing and type conversion.
s="ishan"
print(s[2:4])
for i in range(len(s)):
    print(s[i])
rev=s[::-1]
print(rev)

no=2345
s=str(no)
print(s[::-1])


s=s[::-1]
s=int(s)
print(s)
print(type(s))

#  to demonstrate a function with both parameters and a return value.
def add(x,y):
   
    res=x+y  
    return res 
if __name__=='__main__':
    a=int(input("Enter value: "))
    b=int(input("Enter value: "))
    res=add(a,b)
    print(res)