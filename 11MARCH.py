"""
1. ASCII Character Grid

"""
n=65
for i in range(1,5):   
     for j in range(1,5):
        print(chr (n),end="\t")
        n=n+1
     print()    

"""
2. Incremental Row Pattern

"""
# 1
# 22
# 333
# 4444
# j jo hai wo i time chalta hai 
for i in range(1,5):   
     for j in range(1,i+1):
        print(i,end="")
     print()   

"""
3. Nested Loop Grid Basics

"""
# #pattern 
# for x in range(10):  // outer loop = rows 
#     for x in range(10):  //inner loop = coloums 
# # all moditfiaction are in inner loop 
for i in range(1,5):   
     for j in range(1,5):
        print(i,end="")
     print()    
print( "    ")

for i in range(1,5):   
     for j in range(1,5):
        print(j,end="")
     print()    

"""
4. Continuous Number Grid

"""
#  1 2 3 4
# 5 6 7 8 
# 9 10 11 12
# 13 14 15 16
n=1
for i in range(1,5):   
     for j in range(1,5):
        print(n,end="\t")
        n=n+1
     print()    

"""
5. Mathematical Series Calculation
Calculates the sum of a mathematical power series based on 
user input for n and x.
"""
# #         x^1  X^2  x^3 
# sum = a+ ----+----+-----+---n // series
           # 1    2     3 
n=int(input("enter n: "))
x=int(input("enter x: "))
sum =1 
for i in range (1,n):
    sum =sum+(x**i)/i
print(sum)

"""
6. Star Triangle and Inverted Triangle

"""
# *
# **
# ***
# ****
for i in range(1,5):   
     for j in range(1,i+1):
        print("*",end="")
     print()   

# ****
# ***
# **
# *
for i in range(4,0,-1):   
     for j in range(1,i+1):
        print("*",end="")
     print()   

# hw string in python and learn from help4code.com   learn 
# string handling ans string search methods