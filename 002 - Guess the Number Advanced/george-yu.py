import random

ANSWER = random.randint(1, 100)
CHANCES = 5

for chance in range(CHANCES):
    print('You have', CHANCES-chance, 'chances left.')
    guess = int(input('Make you guess: '))
    if guess < ANSWER:
        print('Too small!\n')
    elif guess > ANSWER:
        print('Too big!\n')
    else: # guess == ANSWER
        print('Correct!')
        break
else:
    print('No chances left...')
