# This imports random
import random

# This welcomes the player
print('Welcome to guess the number!')

# This asks for the player's name
print('What is your name?')

# This gets the player's name
name = str(input())

# This saves the player's name and asks them to guess a number
print('Well, ' + name + ' I am thinking of a number between 1 and 20. Guess it!')

# This generates a random number between 1 and 20
num = random.randint(1, 20)

# This is a check to make sure random number var works
#print(num)

# This sets the number of guess to 0
guessesTaken = 0

# This allows 5 chances to guess the number
for guessesTaken in range(5):
    print('Take a guess.')
    # This takes the player's guess and saves it
    guess = int(input())
    # if the guessed number is greater than the random number, the program tells the user the guess is too high
    if guess >= num and guess != num:
        print('Your guess is too high.')

    # if the guessed number is lower than the random number, the program tells the use the guess is too low
    # python needed != to evaluate this correctly
    if guess <= num and guess != num:
        print('Your guess is too low.')

    # if the guess matches the number, this breaks the loop
    if guess == num:
        break

# if the guess equals the number and the guesses taken are less than 5, this prints a confirmation of the match
if guess == num and guessesTaken <= 5:
    print('Bingo! I was thinking of ' + str(guess) + ' exactly!')

# this finds the sum of the number of guesses taken and turns it into a string
guessesTaken = str(guessesTaken + 1)

# this tells the player how many guess it took them to get the right answer
print('It took ' + name + ' ' + guessesTaken + ' attempts to guess the number. Great job!')

# if the player uses up all their guesses, this reveals the number and tells them better luck next time
if guess != num and guessesTaken >= 6:
    num = str(num)
    print('Nope. The number I had in mind was ' + num + '.'
          'Better luck next time ' + name + '.')

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
