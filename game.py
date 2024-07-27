#Number guessing game
from random import randint

code =True

while code:
    num = input('enter a upper boundary: ')

    if num.isdigit():
        num = int(num)
        code = False

    else:
        print('invalid number, please enter a number!')

correct = randint(1, num)

guess = None
count = 1

while guess != correct:
    guess = input(f'enter a number between 1 and {num}\n ')
      
    if guess.isdigit():
        guess = int(guess)

    if guess == correct:
        print('yay!, you won')
    else:
        print('try again')
        count += 1
print('it took', count, 'guess(es), to get it')
# print('you win!!!')



