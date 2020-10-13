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




def factorPair(number, factor):
    import math
    i= number/factor
    if number % i == 0:
        lists=[i,factor]
        print( lists ) 
           
#The cosine law is used to find the length of a missing side in a triangle
#that is not a right triangle.
#It uses the formula:
#c^2 = a^2 + b^2 - 2*a*b*cos(C)

#In the assignment.py file:
#define a function called cosineLaw().

#The function should take three input parameters, and an optional 4th parameter.
#Two of the required parameters are going to be the sides of a triangle
#and the 3rd is going to be an angle measurement in degrees
#The optional parameter is a boolean True or False called "oppositeSide".
#The default will be True.

#Calculate the missing side of the triangle using the Cosine Law.  You may need to do
#some algebra to isolate your variable.  You will also need to use the quadratic
#formula to find the length of the side if it's not side c.

#We will use the math module to access a method called math.cos
#math.cos will tell us the cosine of an angle if it is in radians,
#but since we are entering the angle measure in degrees, 
#ou will need to create a function called toRadians()

#create the function toRadians()
#it will take 1 input value, a float that is the measure of the angle in degrees
#The function will convert the measure from degrees to raidans

#math.pi radians = 180 degrees

#the return value will be a float value that is the angle measure in radians


#create a function called quadratic.  The function will require 3 float parameters.
#The function will use the quadratic formula to find the solutions to a
#quadratic equation in the format ax^2 + bx + c = 0 and will return
#a sorted list of the 2 solutions

#create a function called solution. The function will require 2 float parameters
#as inputs.  Since the quadratic formula will generate 2 answers, one negative and
#one positive, this will help us decide which should be the length of the missing side.
#Return this value.
#(x points) 
    

def cosineLaw(a,b,toRadians):
    c_2= math.pow(a,2) + math.pow(b,2)
    c_1=(2*a*b) 
    c_3= math.cos(toRadians)*c_1
    c_4= c_2 - c_3
    c= math.sqrt(c_4)
    return c



def toRadians(degrees):
    degrees= float(degrees)
    answer= degrees*(math.pi/180)
    return answer




def convertAngle():
    pass

def solution(answer1, answer2):
        if answer1>0:
                return answer1
        
        if answer2>0:
                return answer2




def quadratic(a,b,c):
    import math

    x11=-b+(math.sqrt(b**2-4*a*c))
    answer1= x11/(2*a)


    x22=-b-(math.sqrt(b**2-4*a*c))
    answer2= x22/(2*a)


    lists=[answer1,answer2]
    return lists


