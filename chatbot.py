import random

class Guesser:
    def __init__(self,number):
        self.number = number


    @staticmethod
    def num_gen():
        return random.randint(1,100)


    def get_factors(self):
        factors_lst = []
        prime_flag = True
        for i in range(2,self.number):
            if self.number % i == 0:
                prime_flag = False
                factors_lst.append(i)
        if prime_flag == True:
            return 'The number is prime!'
        else:
            return factors_lst
    

    def get_multiples(self):
        return(self.number*i for i in range(1,10+1))
    

    def get_larger(self):
        if self.number > 98:
            larger_number = [99,100]
        else:
            larger_number = random.choice(range(self.number+1,100))
        return(larger_number)
    

    def get_smaller(self):
        if self.number <3:
            smaller_number = [1,2]
        else:
            smaller_number = random.choice(range(1,self.number-1))
        return(smaller_number)
    
    
    def odd_even(self):
        if self.number % 2 == 0:
            return 'even'
        else:
            return 'odd'



def num_gues():
    guess_number = 4
    hint_number = 3
    num = Guesser.num_gen()

    guesser_instance = Guesser(num)

    greeting_txt = f'''Hello! I have guessed an integer number between 1 and 100. Can you guess the number?
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
                    print(f'''Sorry! You ran out of guess! The number is {num}.''')
                    break
                elif not int(input_num) in range(1,100):
                    input_num = input(f'''Out of range! You have {guess_number} more guesses to make.
Guess the integer number, which is between 1 and 100 or type "hint" to receive hint: ''')
                    continue
                else:
                    input_num = input(f'''Sorry! Wrong answer! You have {guess_number} more guesses to make.
You can have up to three hints by typing "hint".
Guess again:''')
            else:
                    if hint_number == 0:
                        input_num = input('Sorry! You ran out of hints! Guess the number: ')
                        continue
                    else:

                        hint_number -=1
                        hint_lst = ['a','b','c']
                        hint_selector = random.choice(hint_lst)

                        if hint_selector == 'a':
                            num_mults = guesser_instance.get_multiples()
                            num_mults_lst = list(num_mults)
                            num_factors = guesser_instance.get_factors()
                            if num_factors == 'The number is prime!':
                                num_factors_lst = num_factors
                            else:   
                                num_factors_lst = list(num_factors)
                            a_selector = random.choice([1,2])
                            if a_selector == 1:
                                print('Factors of the number are:',num_factors_lst)
                                input_num = input('You got one hint! Guess the number: ')
                            else:
                                print('One of the multiples of the number is',random.choice(num_mults_lst))
                                input_num = input('You got one hint! Guess the number: ')
                                
                        elif hint_selector == 'b':
                            larger_num = guesser_instance.get_larger()
                            smaller_number = guesser_instance.get_smaller()
                            b_selector = random.choice([1,2])
                            if b_selector == 1:
                                print('The number is smaller than ',larger_num)
                                input_num = input('You got one hint! Guess the number: ')
                            else:
                                print('The number is larger than ',smaller_number)
                                input_num = input('You got one hint! Guess the number: ')
                        elif hint_selector == 'c':
                            print('Parity of the number is:',guesser_instance.odd_even())
                            input_num = input('You got one hint! Guess the number: ')
              
        except ValueError:
            if guess_number ==0:
                    print(f'''Sorry! You ran out of guess! The number is {num}.''')
                    break
            else:
                if guess_number == 1:
                    input_num = input(f'''Wrong input! Guess the integer number, which is between 1 and 100 or type "hint" to receive hint.
You lost one guess! You have {guess_number} more guess to make.
Guess the number: ''')
                else:
                    input_num = input(f'''Wrong input! Guess the integer number, which is between 1 and 100 or type "hint" to receive hint.
You lost one guess! You have {guess_number} more guesses to make.
Guess the number: ''')
            continue     
    

        
num_gues()