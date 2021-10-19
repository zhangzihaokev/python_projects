# -*- coding: utf-8 -*-
132"""
Created on Sun May 22 11:25:50 2016

@author: kevinzhang
"""

#Project 1: Integer guessing puzzle. CSE 231, online section 730, May 22, 2016#


num_str = input('Please enter a 3 digit number. \
The tens digit should be as least as large as the ones and hundreds: ')

num_int = int(num_str)

hun_int = num_int//100 #isolates the hundreds digit 
ten_int = (num_int%100)//10 #isolates the tens digit
one_int = num_int%10 #isolates the ones digit

th_dif = ten_int - hun_int # difference between tens and hundreds
to_dif = ten_int - one_int # difference between tens and ones

print('I am a 3 digit number')
print('My tens digit is', th_dif, 'more than my hundreds digit')
print('My ones digit is', to_dif, 'less than my tens digit')
print('What number am I?')
