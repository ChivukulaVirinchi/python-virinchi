temperature = int(input('Enter a temperature in Celcius\n>>>'))
if temperature >= 50:
    print('Too hot! try not to go out!')
elif temperature > 30:
    print('You\'ll be needing shorts today!')
elif temperature <= 30 and temperature > 20:
    print('It\'s warm but not shorts weather!')
elif temperature <= 20 and temperature > 10:
    print('You\'ll probably need a coat today!')
else: print('Too cold! Don\'t go out')
