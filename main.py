from base64_text_encoder import encode_base64

while(True):
    text = input('Type or paste your text: ')

    if text == 'q':
        exit()
        
    print('base64 result is: ')
    print(encode_base64(text))  