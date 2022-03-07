import random


def winner(a, b):  # a and b represent player as user and opponent as computer/clone
    # paper beats rock, rock beat scissor, scissor beats paper
    if (a == 'Paper' and b == 'Rock') or (a == 'Rock' and b == 'Scissor') or (a == 'Scissor' and b == 'Paper'):
        return True


Player_wins = 0
Clone_wins = 0

# play area with a player and computer as opponent
while True:
    moves = ['Rock', 'Paper', 'Scissor']

    Player = input("Select your move: ")
    print()

    # condition if player wants to quit
    if Player == 'quit':
        break

    # condition if player enter invalid input
    if Player not in moves:
        print("Invalid move.")
        continue

    print("Players choice: ", Player)

    Clone = random.choice(moves)
    print("Clones choice: ", Clone)
    print()

    # conditions for player and computer/clone to win or lose or draw
    if Player == Clone:
        print("Its a Tie!")
        Player_wins += 1
        Clone_wins += 1

    elif winner(Player, Clone):
        print("Yon Won!")
        Player_wins += 5

    else:
        print("You Lost! Better luck next time.")
        Clone_wins += 5

print("Player Total wins: ", Player_wins)
print("Clone Total wins: ", Clone_wins)

print("Cya Loser!")
