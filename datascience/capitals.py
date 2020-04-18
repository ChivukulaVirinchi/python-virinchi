capitals = {'France':'Paris','Germany':'Berlin','India':'New Delhi','China':'Beijeing'}
capitals.get ('India')
# for country in capitals:
#     print(country)

print(capitals.items())

for country, city in capitals.items():
    print(f'The capital of {country} is {city}')

# print(capitals.values())

# if 'India' in capitals:
#     print('It contains India')