from math import ceil
from string_builder import string_builder
from base64_encoder_mapping import get_mapping

def encode_base64(text) -> str:
    decimal_to_base64 = string_builder()
    counter = 0
    ni = 0 #next item

    char_to_binary = ''.join('{0:08b}'.format(ord(char), 'b') for char in text)

    while counter < ceil((len(char_to_binary) - 1) / 6):
        char_to_binary_value = char_to_binary[ni:ni+6:]
        binary_value = '{:<06s}'.format(char_to_binary_value)
        decimal_value = int(binary_value, 2)
        decimal_to_base64.append(get_mapping(decimal_value))

        ni += 6
        counter += 1

    if len(char_to_binary) % 3 == 2:
        decimal_to_base64.append('==')
    elif len(char_to_binary) % 3 == 1:
        decimal_to_base64.append('=')

    return str(decimal_to_base64)