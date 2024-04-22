from random import randint

number = randint(1, 100)
print('Guess the number!')

while True:
    guess = int(input('Enter your nimber: '))

    if guess < number:
        print('Your number is less than hidden! Try again!')

    elif guess > number:
        print('Your number is bigger than hidden! Try again!')

    elif guess == number:
        print('Well done')
        break

