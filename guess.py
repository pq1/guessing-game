import random

# Generate random number from 1 to 100
x = random.randint(1, 101)
count = 6

while True:
    print('Press q to quit')
    guess = input('Guess a number from 1 to 100 with 6 tries: ')

    if guess == 'q':  # Quit the game if user types q
        print('Number was {}'.format(x))
        break
    if int(guess) == x:
        print('You won! Took you  {} of tries'.format(count))
        break
    elif int(guess) > x:
        count -= 1
        print('Too big - {} of tries left'.format(count))
    else:
        count -= 1
        print('Too small - {} of tries left'.format(count))
    if count == 0:
        print('You lose')
        break


