import random

# Generate random number from 1 to 100
x = random.randint(1, 101)

while True:
    print('Press q to quit')
    guess = input('Guess a number: ')
    if guess == 'q':
        break
    elif int(guess) == x:
        print('You won!')
        break
    else:
        print('Wrong')

