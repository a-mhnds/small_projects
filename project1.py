import random

play_choice = {1:'rock',2:'paper', 3:'scissors'}
val = list(play_choice.values())

ans = 'Yes'
while ans.lower() =='Yes'.lower():
    human_play = input('rock, paper, or scissors?').lower()
    computer_play = random.choice(val).lower()
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
    if ans.lower() != 'Yes'.lower() and ans.lower() != 'No'.lower():
        ans = input('Play again?(Yes/No)')