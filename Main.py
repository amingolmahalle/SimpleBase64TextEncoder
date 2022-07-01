from Base64TextEncoder import encode_base64

while(True):
    text = input('Type or paste here: ')

    if text == 'q':
        exit()
        
    print('result is: ')
    print(encode_base64(text))  