#Nested Statement

#A nested if statement is when we create one if statement inside another if statement.

#Find the greatest number from given 3 numbers using nested:

# num1=int(input("Enter a num1: "))
# num2=int(input("Enter a num2: "))
# num3=int(input("Enter a num3: "))

# if(num1 > num2):
#     if(num1 > num3):
#         print(f"The {num1} is greatest")
#     else:
#         print(f"The {num3} is greatest")
# else:
#     if num2>num3:
#         print(f"The {num2} is greatest")
#     else:
#         print(f"The {num3} is greatest")

#Find the smallest number from given 3 numbers using nested:

# num1=int(input("Enter a num1: "))
# num2=int(input("Enter a num2: "))
# num3=int(input("Enter a num3: "))

# if(num1 < num2):
#     if(num1 < num3):
#         print(f"The {num1} is smallest")
#     else:
#         print(f"The {num3} is smallest")
# else:
#     if(num2 < num3):
#         print(f"The {num2} is smallest")
#     else:
#         print(f"The {num3} is smallest")

#if students pass or not, if pass check he is in class toppers list

# mark=int(input("Enter the marks: "))

# if(mark>=35):
#     print("Your are pass")
#     if(mark >=90):
#         print("You are in class topper list")
#     else:
#         print("You are pass but not in class topper list")
# else:
#     print("You are fail")


#Find the middle number from 3 numbers:

# num1=int(input("Enter a num1: "))
# num2=int(input("Enter a num2: "))
# num3=int(input("Enter a num3: "))

# if(num1 <num2):
#     if num1 > num3:
#         print(f"The {num1} is middle")
#     elif num2 < num3:
#         print(f"The {num2} is middle")
#     else:
#         print(f"The {num3} is middle")
# else:
#     if num1<num3:
#         print(f"The {num1} is middle")
#     elif num2 > num3:
#         print(f"The {num2} is middle")
#     else:
#         print(f"The {num3} is middle")

# Check the temprature given by user is for which season(spring(15-30 °C), summer(30+ °C), autumn(0-10 °C), and winter( 10–15 °C)

# temp=int(input("Enter the temperature: "))

# if(temp>0 and temp<=10):   #7>0
#     print("Autumn")
# elif(temp>10 and temp<=15):
#     print("Winter")
# elif(temp>15 and temp<=30):
#     print("Spring")
# elif(temp>30):  #50>30
#     print("summer")
# else:
#     print("Invalid")

# temp=int(input("Enter the temperature: "))

# if(temp>=0):
#     if(temp<=10):
#         print("Autumn")
#     elif(temp<=15):
#         print("Winter")
#     elif(temp<=30):
#         print("Spring")
#     else:
#         print("Summer")
# else:
#     print("invalid")


#Leap Year:

'''
2024 : Leap year
2400 :
'''

# year=int(input("Enter the year: "))

# if(year%4==0):
#     if(year %100==0):
#         if(year%400==0):
#             print("Leap Year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")

'''
Q15) Alice is trying to find a no which is non negative and even and divisible by 3 given by Alice .
Q16) Write a program to print Yes if no which is odd and between 10 to 15 and divisible by 4 given by user
Q17) Write a program to check the input nos. given by Jeff and Bob are same or not for same "Won" else "Lost"
Q18) Create a program using nested if-else where the player chooses between "tea" or "coffee,"and then chooses "hot" or "cold" to get a final drink suggestion.
Q19)A student needs to know if they passed their exam. Write a program that checks their score and prints "Pass" if it is 40 or more, otherwise "Fail."


'''

#Q15) Alice is trying to find a no which is non negative and even and divisible by 3 given by Alice .

# num=int(input("Enter the value: "))

# if(num>=0):
#     if(num%2==0):
#         if(num %3== 0):
#             print(f"The {num} is positive,even and divisible by 3")
#         else:
#             print(f"{num} is positive and even, but not divisible by 3")
#     else:
#         print(f"{num} is positive but not even")
# else:
#     print(f"{num} is negative")


# Q16) Write a program to print Yes if no which is odd and between 10 to 15 and divisible by 4 given by user

# num=int(input("Enter the Number: "))

# if num%2!=0:
#     if num>10 and num<15:
#         if num%4==0:
#             print("Number is odd and between 10 & 15 and divisible by 4")
#         else:
#             print("No ")
#     else:
#         print("No")
# else:
#     print("No")

#Q17) Write a program to check the input nos. given by Jeff and Bob are same or not for same "Won" else "Lost"

# jeffinput=int(input("Enter the jeff input: "))
# bobinput=int(input("Enter the bob input: "))

# if(jeffinput==bobinput):
#     print("input are same")
# else:
#     print("Not same")


#Q18) Create a program using nested if-else where the player chooses between "tea" or "coffee,"and then chooses "hot" or "cold" to get a final drink suggestion.

# drink=input("Enter drink tea or coffee :")

# if( drink =="tea"):
#     drank=input("Which want hot/cold: ")
#     if(drank=="hot"):
#         print("You get hot tea")
#     else:
#         print("you will get cold tea")
# elif( drink =="coffee"):
#     drank=input("Which want hot/cold: ")
#     if(drank=="hot"):
#         print("You get hot coffee")
#     else:
#         print("You get cold coffee")
# else:
#     print("Invalid")


# Q19)A student needs to know if they passed their exam. Write a program that checks their score and prints "Pass" if it is 40 or more, otherwise "Fail."

# marks=int(input("Enter the marks: "))

# if(marks>=40):
#     print("Pass")
# else:
#     print("Fail")

#Q20) Write a Python program that takes the user's age and income as input and determines if they qualify for a loan based on these rules:
'''

   If the age is less than 18, print "Not eligible for a loan."
   If the age is between 18 and 60:
   If the income is less than 20,000, print "Eligible for a basic loan."
   If the income is between 20,000 and 50,000, print "Eligible for a standard loan."
   If the income is above 50,000, print "Eligible for a premium loan."
   If the age is above 60:
   If the income is less than 30,000, print "Eligible for a senior citizen basic loan."
   If the income is 30,000 or more, print "Eligible for a senior citizen premium loan."
'''

age=int(input("Enter the age: "))
if(age>18):
    income=int(input("Enter the income: "))
    if(age>=18 and age<=60):
        if(income < 20000):
            print("Eligible for a basic loan.")
        elif 20000 <= income <= 50000:
            print("Eligible for a standard loan.")
        elif(income>50000):
            print("Eligible for a premium loan.")
        else:
            print("Not Eligible for a basic loan.")
    elif(age>60):
        if(income>30000):
            print("Eligible for a senior citizen basic loan.")
        elif(income<30000):
            print("Eligible for a senior citizen premium loan.")
        else:
            print("Not eligible due to income")
else:
    print("Not Eligible due to age limit")

    









    











