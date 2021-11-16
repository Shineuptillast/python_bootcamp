#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:04:18 2019

@author: Giles
"""

'''
Question 1
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for
example if the user inputs 2 the code will print two. Reject any input that
is not a number in that range
'''
number= int(input("enter a number between 1 and 5"))
if number == 1:
    print("ONE")
elif number==2:
    print("TWO")
elif number==3:
    print("Three")
elif number==4:
    print("four")
elif number == 5:
    print("Five")
else:
    print("Number should be between 1 and 5")
    


'''
Question 2
Repeat the previous task but this time the user will input a string and the
code will ouput the integer value. Convert the string to lowercase first.
'''
number= input("Enter the number between 1 and 5 in word format")
number=number.upper()
if number == "ONE":
    print(1)
elif number=="TWO":
    print(2)
elif number=="THREE:
    print(3)
elif number=="FOUR":
    print(4)
elif number == "FIVE:
    print(5)
else:
    print("Number should be between 1 and 5")


'''
Question 3
Create a variable containing an integer between 1 and 10 inclusive. Ask the
user to guess the number. If they guess too high or too low, tell them they
have not won. Tell them they win if they guess the correct number.
'''
guess = int(input("Enter the number between the range 1 and 10 both inclusive"))

if guess == 5:
    print("Your Correct, you guessed it")
elif guess <5 :
    print("You guessed pretty low kindly do it again")
else:
    print("you guessed pretty high")
    


'''
Question 4
Ask the user to input their name. Check the length of the name. If it is
greater than 5 characters long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret
'''
name= input("Enter your name")
length = len(name)
if length >5:
    print("Your name is of length {}".format(length))


'''
Question 5
Ask the user for two integers between 1 and 20. If they are both greater than
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero
'''
number1= int(input("Enter first number"))
number2= int(input("Enter second number"))
if number1 >15 and number> 15:
    return number1*number2
elif number1>15 or number2>15:
    return number1+number2
else:
    return 0




'''
Question 6
Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.
'''
number1= int(input("Enter first number"))
number2= int(input("Enter second number"))
number1
number2
v=0
v=number1
number1=number2
number2=v

print(number1,number2)
