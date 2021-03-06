from random import randint

# Generate random number from 1 to 100
x = randint(1, 101)
count = 6
tries = 0

while count > 0:

    print('Press letter to quit')
    guess = input('Guess a number from 1 to 100: ')
    try:
        val = int(guess)

        if val == x:
            print('You won! Took you  {} of tries'.format(tries))
            break
        elif val > x:
            count -= 1
            tries += 1
            print('Too big - {} of tries left'.format(count))
        else:
            count -= 1
            tries += 1
            print('Too small - {} of tries left'.format(count))

        if count == 0:
            print('You lose')
    except ValueError:
        print('Input was not an integer')
        break



