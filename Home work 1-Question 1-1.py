# -*- coding: utf-8 -*-
"""
Programming and Problem Solving in Telecom
Presented to Prof. Nygate
HomeWork1 question 1
Author : Mohamed Elmasry
Date : 9-4-2018
"""

def main():

    x = [7,8,3,2,11,6,9,10,13,15,16] #create unsorted list
    i = 0   # initialze temp variable and assign a value = 0 
    y = sorted(x)   # create a new variable to assign it to the sorted list 
    
    # two whiles loops one to check the sorted list and other to check unsorted list 
    print "print the numbers < 10 for unsorted list "
    while i < len(x):  # len function to determine length of list
        if x[i]< 10:
            print x[i] 
        i += 1  # increase counter
        
    j= 0  # initialize the variable for new loop
    print "print the numbers < 10 for sorted list "    
    while y[j] < 10 : # check sorted list values < 10 
        print y[j]   # print vlaues of sorted list 
        j += 1  # increment counter of loop Break condition 


main()

    
    

    
   

    