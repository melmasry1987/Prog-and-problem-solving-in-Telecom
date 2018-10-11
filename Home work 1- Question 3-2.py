"""
Programming and Problem Solving in Telecom
Presented to Prof. Nygate
HomeWork1 question 3 - (b)
Author : Mohamed Elmasry
Date : 9-4-2018
"""
def main():
    rows= int(input("please enter the number of rows: " )) 
    # outer loop for number of rows 
    for i in range(1,rows):
        # inner loop for the pattern 
        for j in range (0,rows-i-1):
              print rows-i-1,
              j =j+1 # increase counter for inner loop
        for k in range (1,i+1):
            print i,
            k +=1
        i = i + 1 # increase counter for outer loop
        print '\r'  # start printing for a new line


main()  # call the function
