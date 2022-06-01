#!/usr/bin/python3
def uppercase(str):
    word = ''
    for letter in range(len(str)):
        if ord(str[letter]) > 96 and ord(str[letter]) < 123:
            word += chr(ord(str[letter])-32)
        elif ord(str[letter]) > 64 and ord(str[letter]) < 91:
            word += chr(ord(str[letter]))
        else:
            word += chr(ord(str[letter]))
    print('{}'.format(word))
