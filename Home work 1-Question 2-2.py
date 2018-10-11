# -*- coding: utf-8 -*-
"""
Programming and Problem Solving in Telecom
Presented to Prof. Nygate
HomeWork1 question 2 - (b)
Author : Mohamed Elmasry
Date : 9-4-2018
"""
def pattern():
    startnum = int(input("please enter the starting number :"))  # request input from the user 
    rows= int(input("please enter the number of rows: " ))  # request input from the user
    # outer loop for number of rows
    for i in range(0,rows):
        #inner loop for the pattern 
        for j in range (0,i+1):
            print startnum,
            j =j+1 # increase counter for inner loop
        i = i + 1  # increase counter for outer loop
        print '\r'  # start printing for a new line
        startnum += 1  # increase printed number in new line


pattern()  # call the function

