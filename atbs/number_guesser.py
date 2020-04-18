# Date: 22/12/19 
# This is a secret number guessing game
import random
print('Hello! What is your name?')
Name = input()
secretNumber = random.randint(1, 20)
print('Lets play a secret number game shall we?')
print('Well ' + Name + ' I am thinking of a number between 1 and 10')

for gussesTaken in range(1, 6):
     print('Take a guess:')
     guess = int(input())
     if guess < secretNumber:
          print('Your guess was too low. Try again')
     elif guess > secretNumber:
          print('Your number was too high. Try again')
     else: 
          break
if guess == secretNumber:
      print('Yay! your guess was correct!')
else: print('Nope. The number I was thinking of was ' + str(secretNumber))