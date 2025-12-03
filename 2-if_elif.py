
#When we have more than two condition then will use if elif else.
#elif statement we use n number of time where as if and else we use once a time only

#Will check a number is zero,positive,negative.

# num=int(input("Enter a number: "))

# if(num==0):
#     print("Number is zero")
# elif(num>0):
#     print("Number is possitive")
# else:
#     print("The number is negative")

# marks=int(input("Enter the marks: "))

# if(marks>=80):
#     print("A grade")
# elif(marks>=70):
#     print("B Grade")
# elif(marks>=60):
#     print("C Grade")
# else:
#     print("D Grade")

#will check greatest number from 3 given numbers:

# num1=int(input("Enter a number: "))
# num2=int(input("Enter a number: "))
# num3=int(input("Enter a number: "))

# if num1 > num2 and num1 > num3:
#     print(f"The {num1} is greatest")
# elif num2>num3:
#     print(f"The {num2} is greatest")
# else:
#     print(f"THe {num3} is greatest")


#will check smaller number from given 3 numbers

# num1=int(input("Enter a number: "))
# num2=int(input("Enter a number: "))
# num3=int(input("Enter a number: "))

# if num1 < num2 and num1 < num3:
#     print(f"The {num1} is smallest")
# elif num2 < num3:
#     print(f"The {num2} is smallest")
# else:
#     print(f"THe {num3} is smallest")


#2 Print perfect 

#5 Print the grade of student for given percentage (A(75-100), B(60-75), C(50-60), D(40-50), F(less<40))

# marks=int(input("Enter your percentage: "))

# if(marks<=100 and marks>75):
#     print("Your Grade is A")
# elif(marks<=75 and marks>60):
#     print("Your grade is B")
# elif(marks<=60 and marks>50):
#     print("Your grade is C")
# elif(marks<=50 and marks>40):
#     print("Your grade is D")
# elif(marks<=40):
#     print("Your grade if F")
# else:
#     print("invalid")

#Vowel or consonant
#Write a PYthon program to check if a given character is a vowel or a consonant

char=input("Enter the input: ")

if( char=="a" or char=="e" or char=="i" or char=="o" or char=="u"):
    print("Vowel")
else:
    print("Consonants")


#in operator

char1=input("Enter the text: ")
vowel="AEIOUaeiou"

if char1 in vowel:
    print("Vowels")
else:
    print("Consonant")
