print ('Welcome to the game of guessing numbers!')

number = 14

guess = int (input ('Please input a number between 1-100: '))

while guess != number:
      if guess > number:
            print ('My number is smaller.')
            guess = int (input ('Please input a number between 1-100: '))
      elif guess < number:
            print ('My number is bigger.')
            guess = int (input ('Please input a number between 1-100: '))
      else:
            print ('You win!')
