from random import shuffle
from statistics import mean
import time
import os
os.system('clear')
a = [14,2,3,4,5,6,7,8,9,10,11,12,13]

suits = ["Hearts","Clubs","Diamond","Spade"]

cards = []


for i in suits:
    for j in a:
        temp=[j,i]
        cards.append(temp)


def drawCards():
    myHand = []
    shuffle(cards)
    for i in range(3):
        myHand.append(cards[0])
        cards.pop(0)

    return myHand

myHand = drawCards()


def trial_check(hand):
    if hand[0][0]==hand[1][0]==hand[2][0]:
        return 9*hand[0][0]
    
    return 0

def color_check(hand):
    a = max([hand[0][0],hand[1][0],hand[2][0]])
    if hand[0][1]==hand[1][1]==hand[2][1]:
        return 3*a
    
    return 0
def sequence_check(hand):
    for i,j in hand:
        if (mean([hand[0][0],hand[1][0],hand[2][0]])==i) and abs(hand[0][0]-hand[1][0])==1:
            return 5*i
    return 0

def pair_check(hand):
    a = [hand[0][0],hand[1][0],hand[2][0]]
    for i in a:
        if a.count(i)==2:
            return i*2
    return 0


# def score_calc(hand):


player1_hand=[]
player2_hand=[]

player1_score=0
player2_score=0

player1_score_later=0
player2_score_later=0

color_score1 = 0
color_score2 = 0

def wincheck(player1_score,player2_score,x):
    if player1_score>player2_score:
        print(f"{player1_name} Won by",x)
    elif player2_score>player1_score:
        print(f"{player2_name} won by",x)
    else:
        print("Draw")  

player1_name = input("Enter Player 1 Name: ")  
player2_name = input("Enter Player 2 Name: ") 
os.system('clear')

while True:
    
    player1_hand=drawCards()

    
    player2_hand=drawCards()

    

    
    print(f"{player1_name}'s cards:\n")
    for i in player1_hand:
        
        val,suite = i
        player1_score_later+=val

        if val==14:
            val='A'
        elif val==13:
            val='K'
        elif val==12:
            val='Q'
        elif val==11:
            val='J'
        
        time.sleep(1)
        print(f"{val} of {suite}")

    print(f"\n\n{player2_name}'s cards:\n")
    for i in player2_hand:
        val,suite = i
        player2_score_later+=val

        if val==14:
            val='A'
        elif val==13:
            val='K'
        elif val==12:
            val='Q'
        elif val==11:
            val='J'
        time.sleep(1)
        print(f"{val} of {suite}")

    print("\n\n")

    if player2_score>player1_score:
        player1_score,player2_score=0,1
    else:
        player2_score,player1_score=0,1

    color_score1= color_check(player1_hand)
    color_score2= color_check(player2_hand)

    valueplayer1 = trial_check(player1_hand)
    valueplayer2 = trial_check(player2_hand)
    if valueplayer1 or valueplayer2:
        player1_score+=valueplayer1
        player2_score+=valueplayer2
        wincheck(player1_score,player2_score,'trial')
        break
    valueplayer1 = sequence_check(player1_hand)
    valueplayer2 = sequence_check(player2_hand)
    if valueplayer1 or valueplayer2:
    
        player1_score+=valueplayer1
        player2_score+=valueplayer2
        if color_score1 or color_score2:
            player1_score+=color_score1
            player2_score+=color_score2
            wincheck(player1_score,player2_score,' Pure Sequence')
        wincheck(player1_score,player2_score,'Sequence')
        break
    if color_score1 or color_score2:
            player1_score+=color_score1
            player2_score+=color_score2
            wincheck(player1_score,player2_score,'Same Color')
            break    
    
    valueplayer1 = pair_check(player1_hand)
    valueplayer2 = pair_check(player2_hand)
    if valueplayer1 or valueplayer2:
        player1_score+=valueplayer1
        player2_score+=valueplayer2
        wincheck(player1_score,player2_score,'pair')
        break

    player1_score+=player1_score_later
    player2_score+=player2_score_later
    
    wincheck(player1_score,player2_score,'values')   
    
    break

print("Game ends")
