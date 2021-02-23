import argparse
import sys

# generate ASCII table range
ascii_char_range = [i for i in range(ord("a"), ord("z")+1)]
# generate ASCII code to letter dictionary
dict_code_to_letter = {i - ascii_char_range[0]+1: chr(i) for i in ascii_char_range}
# generate ASCII letter to code dictionary
dict_letter_to_code = {chr(i): i - ascii_char_range[0]+1 for i in ascii_char_range}


def affine_cipher_encryptor(plaintext, a, b):

    plaintext = list(str(plaintext))
    ciphertext = []
    for x in range(len(plaintext)):
        # check if char is uppercase
        upper = False
        if plaintext[x].isupper():
            upper = True
        # check if the char is letter
        elif ord(plaintext[x]) not in ascii_char_range:
            ciphertext.append(plaintext[x])
            continue
        # convert lowered char into number representing letter position in the alphabet
        char_code = ord(plaintext[x].lower()) - ascii_char_range[0]
        # code the letter with given parameters
        char_code = a * char_code + b
        # perform modulo division to create intermittency
        while True:
            if char_code >= 26:
                char_code = char_code % 26
            else:
                break
        # convert the obtained character code to the letter from dictionary
        letter = dict_code_to_letter[char_code+1]
        # if input letter was uppercase, restore it's original case
        if upper:
            letter = letter.upper()
        # append the encrypted letter to the list
        ciphertext.append(letter)
    # return joined string
    return ''.join(ciphertext)


def affine_cipher_decrypter(ciphertext, a, b):
    ciphertext = list(str(ciphertext))
    plaintext = []
    for x in range(len(ciphertext)):
        # check if char is uppercase
        upper = False
        if ciphertext[x].isupper():
            upper = True
        # check if the char is letter
        elif ord(ciphertext[x]) not in ascii_char_range:
            plaintext.append(ciphertext[x])
            continue
        # convert lowered char into number representing letter position in the alphabet
        char_code = ord(ciphertext[x].lower()) - ascii_char_range[0]
        # determine the inverse a element using the naive method algorithm
        for y in range(1, 26):
            if a * y % 26 == 1:
                # code the letter with given parameters
                char_code = y * (char_code - (b % 26) + 26)
                # perform modulo division to create intermittency
                while True:
                    if char_code >= 26:
                        char_code = char_code % 26
                    else:
                        break
                # convert the obtained character code to the letter from dictionary
                letter = dict_code_to_letter[char_code+1]
                # if input letter was uppercase, restore it's original case
                if upper:
                    letter = letter.upper()
                # append the encrypted letter to the list
                plaintext.append(letter)
    # return joined string
    return ''.join(plaintext)


def caesar_cipher_encryptor(plaintext, shift):
    plaintext = list(str(plaintext))
    ciphertext = []
    # perform modulo division to remove loops
    shift = shift % 26
    for x in range(len(plaintext)):
        # check if char is uppercase
        upper = False
        if plaintext[x].isupper():
            upper = True
        # check if the char is letter
        elif ord(plaintext[x]) not in ascii_char_range:
            ciphertext.append(plaintext[x])
            continue
        # convert lowered char into number representing letter position in the alphabet
        char_code = ord(plaintext[x].lower()) - ascii_char_range[0]+1
        # code the letter with given shift
        char_code = char_code + shift
        # perform modulo division to create intermittency
        while True:
            if char_code > 26:
                char_code = char_code % 26
            else:
                break
        # convert the obtained character code to the letter from dictionary
        letter = dict_code_to_letter[char_code]
        # if input letter was uppercase, restore it's original case
        if upper:
            letter = letter.upper()
        # append the encrypted letter to the list
        ciphertext.append(letter)
    # return joined string
    return ''.join(ciphertext)


def caesar_cipher_decrypter(ciphertext, shift):
    ciphertext = list(str(ciphertext))
    plaintext = []
    # perform modulo division to remove loops
    shift = shift % 26
    for x in range(len(ciphertext)):
        # check if char is uppercase
        upper = False
        if ciphertext[x].isupper():
            upper = True
        # check if the char is letter
        elif ord(ciphertext[x]) not in ascii_char_range:
            plaintext.append(ciphertext[x])
            continue
        # convert lowered char into number representing letter position in the alphabet
        char_code = ord(ciphertext[x].lower()) - ascii_char_range[0]+1
        # code the letter with given shift
        char_code = 26 + char_code - shift
        # perform modulo division to create intermittency
        while True:
            if char_code > 26:
                char_code = char_code % 26
            else:
                break
        # convert the obtained character code to the letter from dictionary
        letter = dict_code_to_letter[char_code]
        # if input letter was uppercase, restore it's original case
        if upper:
            letter = letter.upper()
        # append the encrypted letter to the list
        plaintext.append(letter)
    # return joined string
    return ''.join(plaintext)


class InputTypes:
    def extract_str(x):
        try:
            return int(x)
        except:
            return x


def main():
    parser = argparse.ArgumentParser(prog='pyciph', description='pyciph - commandline tool for encryption and decryption with classical ciphers', )
    subparsers = parser.add_subparsers(title='procedures', dest='command', )

    # procedure: decrypt
    parser_decrypt = subparsers.add_parser('decrypt', help='decrypt the given ciphertext', )
    parser_decrypt.add_argument('--affine', metavar=('PLAINTEXT', 'a', 'b'), type=InputTypes.extract_str, nargs=3,
                                help='use the affine cipher (linear function)', )
    parser_decrypt.add_argument('--atbash', metavar=('CIPHERTEXT'), type=str,
                                help='use the Atbash cipher (affine cipher with a=25, b=25)', )
    parser_decrypt.add_argument('--caesar', metavar=('CIPHERTEXT', 'SHIFT'), type=InputTypes.extract_str, nargs=2,
                                help='use the Caesar cipher with given shift', )
    parser_decrypt.add_argument('--rot13', metavar='CIPHERTEXT', type=str,
                                help='use the ROT13 cipher (Caesar cipher with shift = 13)', )
    # procedure: encrypt
    parser_encrypt = subparsers.add_parser('encrypt', help='encrypt the given plaintext', )
    parser_encrypt.add_argument('--affine', metavar=('PLAINTEXT', 'a', 'b'), type=InputTypes.extract_str, nargs=3,
                                help='use the affine cipher (linear function)', )
    parser_encrypt.add_argument('--atbash', metavar=('PLAINTEXT'), type=str,
                                help='use the Atbash cipher (affine cipher with a=25, b=25)', )
    parser_encrypt.add_argument('--caesar', metavar=('PLAINTEXT', 'SHIFT'), type=InputTypes.extract_str, nargs=2,
                                help='use the Caesar cipher with given shift', )
    parser_encrypt.add_argument('--rot13', metavar='PLAINTEXT', type=str,
                                help='use the ROT13 cipher (Caesar cipher with shift = 13)', )

    # parse arguments
    args = parser.parse_args()

    if not args.command:
        parser.parse_args(['--help'])
        sys.exit(0)

    # procedure: decrypt
    if args.command == 'decrypt':
        if args.affine:
            print(affine_cipher_decrypter(args.affine[0], args.affine[1], args.affine[2]))
        elif args.atbash:
            print(affine_cipher_decrypter(args.atbash, 25, 25))
        elif args.caesar:
            print(caesar_cipher_decrypter(args.caesar[0], args.caesar[1]))
        elif args.rot13:
            print(caesar_cipher_decrypter(args.rot13, 13))
        else:
            parser.parse_args(['decrypt', '-h'])

    # procedure: encrypt
    elif args.command == 'encrypt':
        if args.affine:
            print(affine_cipher_encryptor(args.affine[0], args.affine[1], args.affine[2]))
        elif args.atbash:
            print(affine_cipher_encryptor(args.atbash, 25, 25))
        elif args.caesar:
            print(caesar_cipher_encryptor(args.caesar[0], args.caesar[1]))
        elif args.rot13:
            print(caesar_cipher_encryptor(args.rot13, 13))
        else:
            parser.parse_args(['encrypt', '-h'])


if __name__ == '__main__':
    main()

