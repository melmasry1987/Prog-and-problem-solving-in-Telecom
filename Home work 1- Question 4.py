"""
Programming and Problem Solving in Telecom
Presented to Prof. Nygate
HomeWork1 question 4
Author : Mohamed Elmasry
Date : 9-4-2018
"""

def main():  # define a function
    # request input from user 
    rows = int(input("please enter number of rows : "))
   
    for i in range(0,rows): # iterate for number of rows
        print(' '*(rows-i-1) + '*'*(2*i+1))  # print incrementing number of spaces
        
main()




