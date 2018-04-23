import random
import math

def drawDieRoll(r1, r2=0):

    print('\n---------------------------------------------------\n')
    if r2 != 0:
        print('You rolled: ' +str(r1+r2))
        print(' _______   _______')
        print('| {tl1}   {tr1} | | {tl2}   {tr2} |'.format(tl1='●' if r1 in [2,3,4,5,6] else ' ',
                                                                   tr1='●' if r1 in [4,5,6] else ' ',
                                                                   tl2='●' if r2 in [2,3,4,5,6] else ' ',
                                                                   tr2='●' if r2 in [4,5,6] else ' '))
        print('| {ml1} {mm1} {mr1} | | {ml2} {mm2} {mr2} |'.format(ml1='●' if r1==6 else ' ',
                                                                           mm1='●' if r1 in [1,3,5] else ' ',
                                                                           mr1='●' if r1==6 else ' ',
                                                                           ml2='●' if r2==6 else ' ',
                                                                           mm2='●' if r2 in [1,3,5] else ' ',
                                                                           mr2='●' if r2==6 else ' '))
        print('| {bl1}   {br1} | | {bl2}   {br2} |'.format(bl1='●' if r1 in [4,5,6] else ' ',
                                                                   br1='●' if r1 in [2,3,4,5,6] else ' ',
                                                                   bl2='●' if r2 in [4,5,6] else ' ',
                                                                   br2='●' if r2 in [2,3,4,5,6] else ' '))
        print(' ¯¯¯¯¯¯¯   ¯¯¯¯¯¯¯\n\n')

    else:
        print('You rolled: ' +str(r1+r2))
        print(' _______ ')
        print('| {tl1}   {tr1} |'.format(tl1='●' if r1 in [2,3,4,5,6] else ' ',
                                             tr1='●' if r1 in [4,5,6] else ' '))
        print('| {ml1} {mm1} {mr1} |'.format(ml1='●' if r1==6 else ' ',
                                                 mm1='●' if r1 in [1,3,5] else ' ',
                                                 mr1='●' if r1==6 else ' '))
        print('| {bl1}   {br1} |'.format(bl1='●' if r1 in [4,5,6] else ' ',
                                             br1='●' if r1 in [2,3,4,5,6] else ' '))
        print(' ¯¯¯¯¯¯¯ \n\n')
        

    

def rollDie(oneOrTwo=1):
    roll = random.randint(1,6)
    if oneOrTwo == 2:
        roll2 = random.randint(1,6)
        drawDieRoll(roll, roll2)
        return (roll, roll2)
    else:
        drawDieRoll(roll)
        return roll



def canHit(bonus=100, precisionLvl=15, roll=1, doubleRoll=False):

    #Change algorithm to rely more on the die roll rather than skill
    #Preclvl should make chance of hitting 20-60%, die roll adds another 35%
    #Double bonus stays at 5%
    
    #base chance of hitting is 1 in 5 or 200/1000
    #Roll of die (1-6) makes possible hit percentage 20-40% or 200-400/1000
    chance = int(200*(((roll-1)*0.2)+1))

    #Add bonus from weapon and equipment
    chance += bonus

    #Add precision level bonus
    chance = math.ceil(chance*(((precisionLvl-1)*0.019208)+1))
    
    #Double roll bonus is 5% or 50 added to chance
    if doubleRoll:
        chance += 50

    print('Hit chance: '+str(chance)+' in 1000 = '+str(chance/10)+'%')
    
    #Generate the number to decide if player hits or not
    genHit = random.randint(1,1000)
    print('Random num: '+str(genHit))

    #Attack only successful when random number is between one and chance
    if genHit <= chance:
        print('HIT')
        return True
    else:
        print('MISS')
        return False
    


def attack():
    
    attRoll, damRoll = rollDie(2)
    hit = canHit(roll=attRoll, doubleRoll=(attRoll==damRoll))


for x in range(10):
    attack()
    pause = input()

 

'''
for x in range(10):
    arr = []
    for x in range(10):
        arr.append(random.randint(1,1000))
    arr.sort()
    #print(arr)
        #attack()
        #print("HIT: " + str(canHit(roll=rollDie())))
        #drawDieRoll(rollDie(), rollDie())

    good = 0
    for a in arr:
        if a<400:
            good+=1
    print(str(good*10)+'%')


 _______ 
| ●   ● |
|   ●   |
| ●   ● |
 ¯¯¯¯¯¯¯

'''
