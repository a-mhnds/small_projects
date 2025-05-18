import random

class Guesser:
    def __init__(self,number):
        self.number = number
    def num_gen():
        number = random.randint(1,100)
        return number


def num_gues():
    guess_number = 4
    hint_number = 3
    num = Guesser.num_gen()
    print(num)
    greeting_txt = f'''
Hello! I have guessed an integer number between 1 and 100. Can you guess the number?
You have four guesses to make! You can ask up to three hints by typing "hint".
Let's begin: '''
    input_num = input(greeting_txt)

    while guess_number != 0:
        try:
            if input_num != 'hint':
                guess_number -=1
                if int(input_num) == num:
                    print('Congradulations! You guessed the number!')
                    break
                elif guess_number ==0:
                    print(f'''
Sorry! You ran out of guess! The number is {num}.''')
                    break
                elif not int(input_num) in range(1,100):
                    input_num = input(f'''
Out of range! You have {guess_number} more guesses to make.
Guess the integer number, which is between 1 and 100 or type "hint" to receive hint: ''')
                    continue
                else:
                    input_num = input(f'''
Sorry! Wrong answer! You have {guess_number} more guesses to make.
You can have up to three hints by typing "hint".
Guess again:''')
            else:
                    if hint_number == 0:
                        input_num = input('Sorry! You ran out of hints! Guess the number: ')
                        continue
                    else:
                        hint_number -=1

                        input_num = input('Hints come here...')
                        continue
              
        except ValueError:
            if guess_number ==0:
                    print(f'''
Sorry! You ran out of guess! The number is {num}.''')
                    break
            else:
                if guess_number == 1:
                    input_num = input(f'''
Wrong input! Guess the integer number, which is between 1 and 100 or type "hint" to receive hint.
You lost one guess! You have {guess_number} more guess to make.
Guess the number: ''')
                else:
                    input_num = input(f'''
Wrong input! Guess the integer number, which is between 1 and 100 or type "hint" to receive hint.
You lost one guess! You have {guess_number} more guesses to make.
Guess the number: ''')
            continue     
    

        
num_gues()