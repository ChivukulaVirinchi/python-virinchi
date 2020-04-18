user_input = int(input('Lets play a guessing game. Choose a number between 1 to 10\n>>>'))
secret_number = 2
if secret_number > user_input:
    print('Your guess was too low')
elif secret_number == user_input:
    print('Hooray! you\'ve won')
else: print('Nope. You\'ve lost. You guess was too high')