alphabet = 'abcdefghijklmnopqrstuvwxyz'
input_text = str(input('Enter the text to be encrypted\n>>>'))
output_1 = ''
def shift_amount(i):
    '''Will determine the shift taking into account the lenth of the alphabet'''
    return i%26

for char in input_text:
    alpha_index = alphabet.find(char)
    output = output_1 + alphabet[shift_amount(alpha_index+30)]
print(output)

def encrypt(text, required_shift):
    out_string = ''
    text = text.lower()
    for char in text:
        if char not in alphabet:
            out_string = out_string + char
        else:
            alpha_index = alphabet.find(char)
            out_string = out_string + alphabet[shift_amount(alpha_index+30)]
        return out_string

new_string = 'Once Upon'
shift = encrypt(new_string, 5)