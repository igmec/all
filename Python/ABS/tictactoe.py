def printBoard(b):
    print('   |   |   ')
    print(' '+b['top-L']+' | '+b['top-M']+' | '+b['top-R']+' ')
    print('___|___|___')
    print('   |   |   ')
    print(' '+b['mid-L']+' | '+b['mid-M']+' | '+b['mid-R']+' ')
    print('___|___|___')
    print('   |   |   ')
    print(' '+b['low-L']+' | '+b['low-M']+' | '+b['low-R']+' ')
    print('   |   |   ')


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

player = True
gameOver = False

while not gameOver:
    printBoard(theBoard)
    #CHECK FOR VALID MOVE
    if player:
        print('Enter your move player 1 (X): ', end=' ')
    else:
        print('Enter your move player 2 (O): ', end=' ')
    move = input()
    print()

    if player:
        theBoard[move] = 'X'
    else:
        theBoard[move] = 'O'

    player = not player




