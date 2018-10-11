"""
Programming and Problem Solving in Telecom
Presented to Prof. Nygate
HomeWork1 question 5
Author : Mohamed Elmasry
Date : 9-4-2018
"""


def arbitraryseries(number): # define a function to perform required operation
    
    counter = 0  # reset the counter after each number
    while number > 1 :   # create a while loop
        if number % 2 == 0:  # check if the number is even
            number = number / 2 
        else:  # otherwise the number is odd 
            number = (3* number + 1 ) 
        counter +=1    # increment counter by 1 
    return counter    # return the counter by one


def main(): # define main function
    
    print "Number " + '    '+"Number of Steps"  # print table header
    number_of_steps = []  # create an empty list
    
    for number in range (1,101): # iterate through the hundred number
        print str(number) + '         ' + str(arbitraryseries(number)) 
        number_of_steps.append(arbitraryseries(number)) 
    # retrieve the number with highest steps
    print "Number with most steps ", number_of_steps.index(max(number_of_steps))+1 
    # retrieve the maximum number of steps reached
    print "Maximum number of steps reached ", max(number_of_steps)
    # retrieve number where maximum steps equal to number 
    print "numbers equal number of steps to reach 1"
    # iterate through the numbers 
    for number in range (1,100):   
        if number == arbitraryseries(number):
            print number
                  
main()


