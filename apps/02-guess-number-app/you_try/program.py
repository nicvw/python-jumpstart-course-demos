import random

def main():
    print('------------------------------------')
    print('       GUESS THE NUMBER GAME')
    print('------------------------------------')
    print()
    guess = -1
    number = random.randint(0, 100)
    while guess != number:
        try:
            guess = int(input('Guess a number between 1 and 100: '))
        except ValueError:
            print('Invalid input, please enter a number')
            continue
        else:
            if guess < number:
                print('Sorry but {} is LOWER than the number'.format(guess))
            elif guess > number:
                print('Sorry but {} is HIGHER than the number'.format(guess))
            else:
                print('YES! You\'ve got it.  The number was {}'.format(guess))


if __name__ == '__main__':
    main()
