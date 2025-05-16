import random

play_choice = {1:'rock',2:'paper', 3:'scissors'}
val = list(play_choice.values())
computer_play = random.choice(val)

ans = 'Yes'
while ans =='Yes':
    human_play = input('rock, paper, or scissors?')
    out_str = f'''I chose {computer_play}, and you chose {human_play}.'''
    print(out_str)
    if human_play in play_choice.values():
        if human_play == computer_play:
            print('Tie!')
        else:
            if human_play == 'rock':
                if computer_play == 'scissors':
                    print('You won!')
                else:
                    print('I won!')
            if human_play == 'paper':
                if computer_play == 'scissors':
                    print('I won!')
                else:
                    print('you won!')
            if human_play == 'scissors':
                if computer_play == 'rock':
                    print('I won!')
                else:
                    print('you won!')
    else:
        print('Error: Incorrect choice!')
    ans = input('Play again?(Yes/No)')
    if ans != 'Yes' and ans != 'No':
        ans = input('Play again?(Yes/No)')