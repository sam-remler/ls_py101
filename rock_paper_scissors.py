import random

VALID_MOVES = ['Rock', 'Paper', 'Scissors']

def prompt(message):
    print("---->" + message)

def results_rps(player1_move, player2_move):
    """ Takes in two players rock paper scissors moves, outputs the updated score of the game"""
    if player1_move == player2_move:
        return 0, 0
    elif (player1_move == 'Rock') & (player2_move == 'Scissors'):
        return 1, 0
    elif (player1_move == 'Rock') & (player2_move == 'Paper'):
        return 0, 1
    elif (player1_move == 'Paper') & (player2_move == 'Rock'):
        return 1, 0
    elif (player1_move == 'Paper') & (player2_move == 'Scissors'):
        return 0, 1
    elif (player1_move == 'Scissors') & (player2_move == 'Paper'):
        return 1, 0
    elif (player1_move == 'Scissors') & (player2_move == 'Rock'):
        return 0, 1
    else:
        return None, None
    
score = {'player1': 0,
         'player2' : 0}

while True:
    prompt("Welcome to Rock Paper Scissors!")
    while True:
        prompt(f"What's your move? Valid options are {", ".join(VALID_MOVES)}")
        move = input()
        if move in VALID_MOVES:
            break
        else:
            prompt("Not a valid move!")
            
    computer_move = VALID_MOVES[random.randint(0,2)]
    
    result = results_rps(move, computer_move)

    score['player1'] += result[0]
    score['player2'] += result[1]

    if result[0] ==result[1]:
        prompt("We Tied")
    elif result[0] > result[1]:
        prompt("Congrats you wom that one!")
    else:
        prompt("Sorry I won that one!")

    prompt(f"The updated results are You: {score['player1']} and Computer: {score['player2']}")

    prompt("Would you like to continue (y/n?)")
    yn = input()
    if yn == 'n':
        break

        


    
