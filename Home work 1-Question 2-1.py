# -*- coding: utf-8 -*-
"""
Programming and Problem Solving in Telecom
Presented to Prof. Nygate
HomeWork1 question 2 - (a)
Author : Mohamed Elmasry
Date : 9-4-2018
"""

# create a variable to specify how many digit to display
n = input("Please enter how many digit to display = ") 

def main():  # define a main function 
    i = 0    # initialize the variable  
    userinput = "" # initialize the variable
    for i in range(n): # iterate for range of numbers 
        # request users to enter numbers to be displayed in series
        userinput = str(input("Please enter numbers to generate pattern = ")) + userinput

    print str(userinput[::-1]) # print the numbers 

main()


