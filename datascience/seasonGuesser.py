s1 = 'winter'
s2 = 'spring'
s3 = 'rainy'
s4 = 'summer'

guess = str(input('I am thinking of a word. Can you guess what it is? Hint: It\'s a season. \nEnter your guess >>>'))
guess = guess.lower()
if guess == s4:
    print('You\'re lucky!. It is', s4, '!')
elif guess == s1:
    s1 = s1.upper()
    print('No.', s1, 'was not the word I was thinking of')
else: print('Nope. think of another season')