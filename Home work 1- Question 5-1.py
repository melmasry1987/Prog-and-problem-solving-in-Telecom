# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 01:09:30 2018

@author: melmasry
"""

def arbitraryseries(number):
    
    counter = 0
    while number > 1 :
        if number % 2 == 0:
            number = number / 2 
        else: 
            number = (3* number + 1 )
        counter +=1    
#        print number
    return counter   


print (arbitraryseries(2))