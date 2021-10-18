# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 10:12:23 2016

@author: kevinzhang
"""

letters = ['R', 'Y', 'B', 'G', 'W', 'O', 'r', 'y', 'b', 'g', 'w', 'o']

key_ini = input('Enter a 4-character key: ')
key_str = key_ini.upper()
guess_ini = input('Enter a guess: ')
guess_str = guess_ini.upper()

history = ''
exact = 0
partial = 0
game = False
while (game == False):
    for ch in letters:
        repeat = guess_str.count(ch)
        if not(len(guess_str) == 4 and guess_str.isalpha()): 
            guess_str = input('Enter a 4 character alphabetical guess, try again: ')
            continue
        if repeat > 1:
            guess_str = input('Enter a guess without repeats, try again: ')
            continue 
        if guess_str[0] not in letters or guess_str[1] not in letters or guess_str[2] not in letters or guess_str[3] not in letters:
            guess_str = input('Enter a guess from RYGBWO: ')
        else:
           game = True
   
    while (game == True):
        for i in range(4):
             if guess_str[i] == key_str[i]:
                 exact += 1
        for r in range(4):
            if guess_str[i] in key_str[r]:
                partial += 1
                break
            print('Your current answer has', exact, 'exact letters and', partial, 'partial letters')
            
    history += '\n' + guess_str
    print('Previous guesses: ', history)
    
    guess_count += 1
    print('Guess count (out of eight): ', guess_count)
    
    guess_str = input('Wrong guess, try again: ')    
    
    if guess_count == 3:
        print('Out of guesses, game over')
        break
    if guess_str == key_str:
        print('Guess correct, game over. ', 'Key: ', key_str)
        break  