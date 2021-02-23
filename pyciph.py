# generate ASCII table range
ascii_char_range = [i for i in range(65,91)]

# generate ASCII code to letter dictionary
# dict_ascii_codes = {i : chr(i) for i in ascii_char_range}

# generate ASCII letter to code dictionary
# dict_ascii_letters = {chr(i) : i for i in ascii_char_range}


def caesar_cipher_encryptor(plaintext, shift):
    plaintext = list(plaintext.upper())
    ciphertext = []
    shift = shift % 26
    for x in range(len(plaintext)):
        char_code = ord(plaintext[x])
        if char_code not in ascii_char_range:
            ciphertext.append(chr(char_code))
            continue
        elif char_code + shift > ascii_char_range[-1]:
            char_code = ascii_char_range[0] + (char_code + shift) - ascii_char_range[-1]-1
        else:
            char_code = char_code + shift
        ciphertext.append(chr(char_code))
    return ''.join(ciphertext)


def caesar_cipher_decrypter(ciphertext, shift):
    ciphertext = list(ciphertext.upper())
    plaintext = []
    shift = shift % 26
    for x in range(len(ciphertext)):
        char_code = ord(ciphertext[x])
        if char_code not in ascii_char_range:
            plaintext.append(chr(char_code))
            continue
        elif char_code - shift < ascii_char_range[0]:
            char_code = ascii_char_range[-1]+1 - shift + char_code - ascii_char_range[0]
        else:
            char_code = char_code - shift
        plaintext.append(chr(char_code))
    return ''.join(plaintext)


def caesar_cipher_cracker(ciphertext):
    ciphertext = list(ciphertext.upper())
    lst = []
    for shift in range(0, 25):
        plaintext = []
        for x in range(len(ciphertext)):
            char_code = ord(ciphertext[x])
            if char_code not in ascii_char_range:
                plaintext.append(chr(char_code))
                continue
            elif char_code - shift < ascii_char_range[0]:
                char_code = ascii_char_range[-1] + 1 - shift + char_code - ascii_char_range[0]
            else:
                char_code = char_code - shift
            plaintext.append(chr(char_code))
        lst.append(''.join(plaintext) + ' (shift = ' + str(shift) + ')')
    return lst

