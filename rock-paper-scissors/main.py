import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors:  ")
    computer = random.choice(['r' , 'p' ,'s'])

    if user == computer:
        return 'tie'
    
    if is_win(user, computer):
        return "you won!"
    
    return "you lost"
    
    # r > s, s>p, p>r

def is_win(player, opponent):
    # return true if player wins
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
     or (player == 'p' and opponent == 'r'):
        return True 
    
print(play())