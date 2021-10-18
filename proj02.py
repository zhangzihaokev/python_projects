###############################################################################
#CSE 231 Project 2, online section 730. 
#This program draws a specified number (at least 3) of randomly colored circles
#of a specified radius (at least 20) in a ring formation.  
#prompt for number of circles
#   check to see if it is a digit and at least 3
#prompt for a radius
#   check to see if it is a digit and at least 20
#turtle draws a ring of circles of the given specifications. 
#
#
#
#
#
###############################################################################
"""
Created on Sun May 29 12:19:04 2016
"""
print('This program will draw a specified number (at least 3) of randomly\
colored circles of a specified radius (at least 20) in a ring formation.')

import turtle
import random


try:
    cir_str = input('Enter the desired number of circles (at least 3): ')
    if cir_str.isdigit() and int(cir_str) >= 3: #Checks the input to be a digit and at least 3
        cir_int = int(cir_str)
        print('The value is good')
    else:
        count = int(cir_str) #If not, prompt the user until correct value is entered
        while count < 3:
            count = int(input('Value not accepted. Try another: '))
        cir_int = count
except ValueError: #Makes sure input is not string
    cir_int = int(input('Please enter a number: '))
    
    
try:            
    rad_str = input('Enter the desired radius (at least 20): ')
    if rad_str.isdigit() and int(rad_str) >= 20:
        rad_int = int(rad_str)
        print('The value is good')

    else:
        count = int(rad_str)
        while count < 20:
            count = int(input('Value not accepted. Try another: '))
        rad_int = count
except ValueError:
    rad_int = int(input('Please enter a number: '))        
        
        
n = cir_int
for i in range(n):
    turtle.color(random.random(),random.random(), random.random())
    turtle.begin_fill()
    turtle.circle(rad_int)
    turtle.end_fill()
    turtle.penup()
    turtle.right(360/cir_int) #Makes sure the circles are drawn in a ring formation
    turtle.forward(rad_int)
    turtle.pendown()
    