import random
randoma = random.randint(0, 9)
print('Want to play a guessing game? I\'ll choose a number between 1-10 and you guess it. You have three tries to get it correctly.' )
choice = str(input('Yes or No?\n>>>'))

if 'yes' in choice.lower():
    print('Then lets play! I have already chosen my number. Guess it!')
    i = 0
    while i <= 3:
        i = i + 1
        guess = int(input('What\'s your first guess?\n>>>'))
        if randoma == guess:
            print('Wow! you are a lucky one! Winner Winner Chicken Dinner')
            i = i + 2
        elif randoma < guess:
            print('Nope. You guess was too high. Try again')
        elif randoma > guess:
            print('Nope. Your guess was too low. Try again')
        if i == 3:
            print('Too many guesses. The number I chose was thinking of was', randoma, '. Better luck next time!')
            break 

            
elif 'no' in choice.lower():
    print('Never mind then. I\'ll find someone else to play with')
else: print('Enter a valid answer')