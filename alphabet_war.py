'''
There is a war and nobody knows - the alphabet war!
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.
Task:
Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.
The left side letters and their power:
 w - 4
 p - 3 
 b - 2
 s - 1
The right side letters and their power:
 m - 4
 q - 3 
 d - 2
 z - 1
'''

def alphabet_war(fight):
    right_side = {'m' : 4,'q' : 3,'d' : 2,'z' : 1}
    left_side = {'w' : 4,'p' : 3,'b' : 2,'s' : 1}
    right = 0
    left = 0
    for letter in fight:
        if letter in right_side:
            right = right + (right_side[letter])
        elif letter in left_side:
            left = left + (left_side[letter])
    if left > right:
        return("Left side wins!")
    elif right > left:
        return("Right side wins!")
    else:
        return ("Let's fight again!")


