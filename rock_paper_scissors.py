import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer chose: {computer}")
    if user == computer:
        return 'It\'s a tie.'
    if win(user, computer):
        return 'You won!'
    return 'You lost!'

def win(player, opponent):
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

print(play())
