#If Statement:

#Syntax:
'''
if(condition expression)
    print("Statement to be execute")

    
'''

a=10
b=12

if(a<b):
    print("The valuue of a is greater than b")
else:
    print("The valuue of b is greater than a")

#we need to check a given number is even or not

num=int(input("Enter the value: "))

if(num%2==0):
    print("The above number is Even")
else:
    print("The above value is not Even")

#check given number is divisible by 5 or not

num=int(input("Enter the value: "))

if(num%5==0):
    print("THe number is divisible by 5")
else:
    print("The number is not divisible by 5")

#check given number is divisible by 5 and 10

num=int(input("Enter the value: "))

if(num%5==0 and num%10==0):
    print("Number is divisible by 5 and 10")
else:
    print("Number is not divisible by 5 and 10")

#take the input from the user and check is he applicable for voting

age=int(input("Enter the age: "))

if(age>=18):
    print("You are applicable for voting")
else:
    print("You are not applicable for voting")

#take a 2 number and check greater and smaller among them

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

if(num1>num2):
    print("Number1 is greater than Nnmber2")
else:
    print("Number2 is greater than Number1")


#Check a number is positive or not.

num=int(input("Enter the value: "))

if(num>0):
    print("Number is possitive")
else:
    print("Number in negative")