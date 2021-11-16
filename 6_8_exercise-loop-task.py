#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 08:50:32 2019

@author: Giles
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
a,b = int(input("Enter two numbers between the 1 and 100"))
p=0
for i in range(a,b+1):
    p=p+1
print(p)
'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
stri= input("Enter a String")
print(stri[-1::-1])


'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''
number= int(input("Enter the number for table between 1 and 12"))
for i in range(1,11):
    print(number*i)

'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''
for i in range(1,13):
    print(" {} Table".format(i))
    for j in range(1,11):
           print(i*j)

'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''
a=True
list_=[]
while a:
    c= int(input("Enter the number for the Sequence-->>"))
    a=input("Want to enter more True/False")
    list_.append(c)
    sum_=0
for i in list_:
    sum_=sum_+i
mean_= sum/len(list_)

'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''
def factorial(number):
    if number ==0:
        return 1
    else:
        return factorial(number-1)
factorial(15)    

'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''
def fibonacci (number):
    f=0,t=1
    l=[]
    l.append(f)
    l.append(t)
    for i in range(3,21):
        t=f+t
        f=t
        l.append(t)
        
    return l
fibonacci(20)


'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''




'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''
i=1
p=6
while i<=p:
    if i%2!=0 and i!=5 :
        for l in range(0,p-i+1):
            print("*", end="")
    else:
        print("*", end="")
    i=i+1 
    print("\n")


'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''
odd=[]
even=[]
for i in range(1,101):
    if i%==0:
        even.append(i)
    else:
        odd.append(i)