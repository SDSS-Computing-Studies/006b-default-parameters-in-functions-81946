#! python3

import math

def tempConversion(degrees, unit):
    if unit=="C":
        answer= (degrees*9/5)+32
        answer=float(answer)
        return answer
    if unit=="F":
        answer= (degrees-32)*5/9
        answer=float(answer)
        return answer


#Factor Pair
#In the assignment.py file:
#Define a function called factorPair().
#It has 2 required integer inputs:
#a number, and a factor
#The return value is a sorted list of the 2 factors that multiply to 
#make the number

#Example Command:
#print( factorPair(10,2) )
#expects:
#[2, 5]

def factorPair(number, factor):
    import math
    i= number/factor
    if number % i == 0:
        lists=[i,factor]
        print( lists ) 
           

    


def cosineLaw():
    pass

def convertAngle():
    pass

def solution():
    pass

def quadratic():
    pass

