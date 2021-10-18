# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:09:25 2016

@author: kevinzhang
"""
#CSE 231 online section 730
import cards

def build_suit(h):
    '''Returns a dictionary using the suits as keys and the lists of cards as values'''
    D_suit = {}
    club = []
    diamond = []
    heart = []
    spade = []
    for i in h:
        if i.suit() == 1: #This portion checks the suit of each card in hand and places it in the appropriate suit list
            club.append(i)
            D_suit['clubs'] = club #Sets the dictionary keys to be equal to the suit names and adds in the list created as values
        if i.suit() == 2:
            diamond.append(i)
            D_suit['diamonds'] = diamond
        if i.suit() == 3:
            heart.append(i)
            D_suit['hearts'] = heart
        if i.suit() == 4:
            spade.append(i)
            D_suit['spades'] = spade
    return D_suit
            
def build_rank(h):
    '''Returns a dictionary that has card ranks as keys and the lists of cards as values'''
    D_rank = {}
    value_1 = []
    value_2 = []
    value_3 = []
    value_4 = []
    value_5 = []
    value_6 = []
    value_7 = []
    value_8 = []
    value_9 = []
    value_10 = []
    value_11 = []
    value_12 = []
    value_13 = []
    for i in h:
        if i.rank() == 1: #Checks the ranks of each card in hand and places it in the appropriate rank list
            value_1.append(i)
            D_rank[i.rank()] = value_1 #Sets the key of dicitonary to the rank of cards and adds the list as values
        if i.rank() == 2:
            value_2.append(i)
            D_rank[i.rank()] = value_2    
        if i.rank() == 3:
            value_3.append(i)
            D_rank[i.rank()] = value_3
        if i.rank() == 4:
            value_4.append(i)
            D_rank[i.rank()] = value_4
        if i.rank() == 5:
            value_5.append(i)
            D_rank[i.rank()] = value_5
        if i.rank() == 6:
            value_6.append(i)
            D_rank[i.rank()] = value_6
        if i.rank() == 7:
            value_7.append(i)
            D_rank[i.rank()] = value_7
        if i.rank() == 8:
            value_8.append(i)
            D_rank[i.rank()] = value_8
        if i.rank() == 9:
            value_9.append(i)
            D_rank[i.rank()] = value_9
        if i.rank() == 10:
            value_10.append(i)
            D_rank[i.rank()] = value_10
        if i.rank() == 11:
            value_11.append(i)
            D_rank[i.rank()] = value_11
        if i.rank() == 12:
            value_12.append(i)
            D_rank[i.rank()] = value_12
        if i.rank() == 13:
            value_13.append(i)
            D_rank[i.rank()] = value_13
    return D_rank
  
def four_kind(D):
    '''Returns a list of cards with four of a kind if it exists, otherwise a blank list'''
    blank = []
    for v in D.values():
        if len(v) == 4: #The dictionary is indexed by rank, so the value must be a list of cards with the same rank
            return v #Having the list length be four means there are four cards of the same rank
    return blank  
    
def three_kind(D):
    '''Returns a list of cards with three of a kind if it exists, otherwise a blank list'''
    blank = []
    for v in D.values():
        if len(v) == 3: #Having the list length be three means there must be three cards of the same rank
            return v
    return blank

def pair(D):
    '''Returns a list of a pair of cards if it exists, otherwise a blank list'''
    blank = []
    for v in D.values():
        if len(v) == 2: #Having the list length be two means there must be two cards of the same rank
            return v
    return blank
    
def two_pair(D):
    '''Returns a list of two pairs of cards if it exists, otherwise a blank list'''
    blank = []
    pair_list = []
    for v in D.values():
        if len(v) == 2:
            pair_list.append(v) #Adds all lists of length two, i.e. pairs, to pair_list
    if len(pair_list) == 2: #If there are two pairs in this list, return them
        return pair_list
    return blank
    
def full_house(D):
    '''Returns a list of cards with three of them same and two of them the same if it exists, otherwise a blank list'''
    blank = []
    pair_list = []
    for v in D.values():
        if len(v) == 2: #Checks for a pair
            pair_list.append(v)
        if len(v) == 3: #Checks for three of a kind
            pair_list.append(v)
    if len(pair_list) == 2 and len(pair_list[0])+len(pair_list[1]) == 5:
        return pair_list #If the sum of the two elements in pair_list is five, we have a triple and a pair
    return blank
        
def flush(D):
    '''Returns a list of 5 cards with all the same suit if it exists, otherwise a blank list'''
    blank = []
    for v in D.values(): #This uses a different dictionary that has suits as keys
        if len(v) == 5: #The values of this dictionary must be cards of the same suit, if there are five of these cards return them
            return v
    return blank
    
def straight(D):
    '''Returns a list of five cards of consecutive rank if it exists, otherwise a blank list'''
    blank = []
    rank_list1 = []
    rank_list2 = []
    for i in D.values():
        rank_list1 += i
    for j in rank_list1:
        rank_list2.append(j.rank())   #Gets all the ranks of the hand in a list
    v = sorted(list(set(rank_list2))) #Removes any repeats
    x = []
    for i in range(len(v)):
        if i != len(v)-1 and v[i] == v[i+1]-1: #If the rank is one less than the next element add it to x
            x.append(v[i])
        if i == len(v)-1 and v[i] == v[i-1]+1: #Special case for the last element
            x.append(v[i])
        if i != 0 and v[i] == v[i-1]+1: #If the rank is one more than the previous element add it to x
            x.append(v[i])
        if i == 0 and v[i] == v[i+1]-1: #Special case for the first element
            x.append(v[i])
    y = sorted(list(set(x))) # Removes any repeats
    z = []
    if len(y)==5 and y[4]-y[0]==4: #Ensures that the length is five and that elements are consecutive
        for i in y:
            z.append(D[i][0]) #Converts the ranks back into cards
        return z
    return blank
    
def straight_flush(D):
    '''Returns a list of five cards of consecutive rank and same suit if it exists, otherwise a blank list'''
    blank = []
    rank_list1 = []
    rank_list2 = []
    for i in D.values():
        rank_list1 += i
    for j in rank_list1:
        rank_list2.append(j.rank())   
    v = sorted(list(set(rank_list2))) #Removes any repeats
    x = []
    for i in range(len(v)):
        if i != len(v)-1 and v[i] == v[i+1]-1:
            x.append(v[i])
        if i == len(v)-1 and v[i] == v[i-1]+1:
            x.append(v[i])
        if i != 0 and v[i] == v[i-1]+1:
            x.append(v[i])
        if i == 0 and v[i] == v[i+1]-1:
            x.append(v[i])
    y = sorted(list(set(x)))
    z = []
    if len(y)==5 and y[4]-y[0]==4:
        for i in y:
            z.append(D[i][0]) #Everything until this point is the same as straight
        print(z)
    D2 = build_suit(z) #Builds a dictionary using the suits of the five straights as keys
    
    for k in D2.values():
        if len(k) == 5: #If the five cards are of the same suit, return them
            return k
    return blank


the_deck = cards.Deck()
the_deck.shuffle()

play_str = input('Play a round? (Y or N): ') #Prompts user 
play_lower = play_str.lower() #Counts Y and y 
while play_lower == 'y': #As long as the user enters y, the game goes on
    print('Let\'s play poker!')
    h1 = []
    h2 = []
    com = []
   
    for i in range(2): #Deals two cards to each player
        h1.append(the_deck.deal())
        h2.append(the_deck.deal())
    for i in range(5): #Deals five cards to community
        com.append(the_deck.deal())
    hand1 = h1 + com #Considers each player's hand along with the community 
    hand2 = h2 + com        
    D_rank1 = build_rank(hand1) #Builds the rank and suit dictionary for both players
    D_suit1 = build_suit(hand1)
    D_rank2 = build_rank(hand2)
    D_suit2 = build_rank(hand2)
    print('Cards in deck: ', len(the_deck))
    if len(the_deck) >= 9: #Ensures there are enough cards in the deck to play
        print()
        print('Community : ', com)
        print('Player 1: ', h1)
        print('Player 2: ', h2)
        print()
        if straight_flush(D_rank1) or straight_flush(D_rank2): #If either players satisfy a straight flush
            if straight_flush(D_rank2) and straight_flush(D_rank1): #Both satisfies
                print('It\'s a tie. Both players have a straight flush.')
                print('Player 1\'s hand: ', straight_flush(D_rank1))
                print('Player 2\'s hand: ', straight_flush(D_rank2))
            if straight_flush(D_rank1) and not(straight_flush(D_rank2)): #only player 1 satisfies
                print('Straight Flush!')
                print('Player 1 Wins!')
                print('Winning hand:', straight_flush(D_rank1))
            if straight_flush(D_rank2) and not(straight_flush(D_rank1)): #only player 2 satisfies
                print('Straight Flush!')
                print('Player 2 Wins!')
                print('Winning hand:', straight_flush(D_rank2))
        elif four_kind(D_rank1) or four_kind(D_rank2): #Rest of categories is same as srtraight flush
            if four_kind(D_rank2) and four_kind(D_rank1):
                print('It\'s a tie. Both players have four of a kind.')
                print('Player 1\'s hand: ', four_kind(D_rank1))
                print('Player 2\'s hand: ', four_kind(D_rank2))
            if four_kind(D_rank1) and not(four_kind(D_rank2)):
                print('Four of a Kind!')
                print('Player 1 Wins!')
            
                print('Winning hand:', four_kind(D_rank1))
            if four_kind(D_rank2) and not(four_kind(D_rank1)):
                print('Four of a Kind!')
                print('Player 2 Wins!')
                print('Winning hand:', four_kind(D_rank2))
        elif full_house(D_rank1) or full_house(D_rank2):
            if full_house(D_rank2) and full_house(D_rank1):
                print('It\'s a tie. Both players have a full house.')
                print('Player 1\'s hand: ', full_house(D_rank1))
                print('Player 2\'s hand: ', full_house(D_rank2))
            if full_house(D_rank1) and not(full_house(D_rank2)):
                print('Full House!')
                print('Player 1 Wins!')
                print('Winning hand:', full_house(D_rank1))
            if full_house(D_rank2) and not(full_house(D_rank1)):
                print('Full House!')
                print('Player 2 Wins!')
                print('Winning hand:', full_house(D_rank2))
        elif flush(D_suit1) or flush(D_suit2):
            if flush(D_suit2) and flush(D_suit1):
                print('It\'s a tie. Both players have a flush.')
                print('Player 1\'s hand: ', flush(D_suit1))
                print('Player 2\'s hand: ', flush(D_suit2))
            if flush(D_suit1) and not(flush(D_suit2)):
                print('Flush!')
                print('Player 1 Wins!')
                print('Winning hand:', flush(D_suit1))
            if pair(D_rank2) and not(flush(D_suit1)):
                print('Flush!')
                print('Player 2 Wins!')
                print('Winning hand:', flush(D_suit2))
        elif straight(D_rank1) or straight(D_rank2):
            if straight(D_rank2) and straight(D_rank1):
                print('It\'s a tie. Both players have a straight.')
                print('Player 1\'s hand: ', straight(D_rank1))
                print('Player 2\'s hand: ', straight(D_rank2))
            if straight(D_rank1) and not(straight(D_rank2)):
                print('Straight!')
                print('Player 1 Wins!')
                print('Winning hand:', straight(D_rank1))
            if straight(D_rank2) and not(straight(D_rank1)):
                print('Straight!')
                print('Player 2 Wins!')
                print('Winning hand:', straight(D_rank2))
        elif three_kind(D_rank1) or three_kind(D_rank2):
            if three_kind(D_rank2) and three_kind(D_rank1):
                print('It\'s a tie. Both players have three of a kind.')
                print('Player 1\'s hand: ', three_kind(D_rank1))
                print('Player 2\'s hand: ', three_kind(D_rank2))
            if three_kind(D_rank1) and not(three_kind(D_rank2)):
                print('Three of a Kind!')
                print('Player 1 Wins!')
                print('Winning hand:', three_kind(D_rank1))
            if three_kind(D_rank2) and not(three_kind(D_rank1)):
                print('Three of a Kind!')
                print('Player 2 Wins!')
                print('Winning hand:', three_kind(D_rank2))
        elif two_pair(D_rank1) or two_pair(D_rank2):
            if two_pair(D_rank1) and two_pair(D_rank2):
                print('It\'s a tie. Both players have a two pair.')
                print('Player 1\'s hand: ', two_pair(D_rank1))
                print('Player 2\'s hand: ', two_pair(D_rank2))
            if two_pair(D_rank1) and not(two_pair(D_rank2)):
                print('Two Pair!')
                print('Player 1 Wins!')
                print('Winning hand:', two_pair(D_rank1))
            if two_pair(D_rank2) and not(two_pair(D_rank1)):
                print('Two Pair!')
                print('Player 2 Wins!')
                print('Winning hand:', two_pair(D_rank2))
        elif pair(D_rank1) or pair(D_rank2):
            if pair(D_rank2) and pair(D_rank1):
                print('It\'s a tie. Both players have a pair.')
                print('Player 1\'s hand: ', pair(D_rank1))
                print('Player 2\'s hand: ', pair(D_rank2))
            if pair(D_rank1) and not(pair(D_rank2)):
                print('One Pair!')
                print('Player 1 Wins!')
                print('Winning hand:', pair(D_rank1))
            if pair(D_rank2) and not(pair(D_rank1)):
                print('One Pair!')
                print('Player 2 Wins!')
                print('Winning hand:', pair(D_rank2))
        else: #Neither players had any good hands
            print('It\'s a tie. No player has a better hand')
    else: #When there are less than 9 cards, end the game
        print('Not enough cards, game over.')
        break
    play_lower = input('Play a round? (Y or N): ')
print()
print('Thanks for playing!')
