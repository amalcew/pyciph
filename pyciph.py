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
        upper = False
        if plaintext[x].isupper():
            upper = True
        elif ord(plaintext[x]) not in ascii_char_range:
            ciphertext.append(plaintext[x])
            continue
        char_code = ord(plaintext[x].lower()) - ascii_char_range[0]
        char_code = a * char_code + b
        while True:
            if char_code >= 26:
                char_code = char_code % 26
            else:
                break
        letter = dict_code_to_letter[char_code+1]
        if upper:
            letter = letter.upper()
        ciphertext.append(letter)
    return ''.join(ciphertext)


def affine_cipher_decrypter(ciphertext, a, b):
    ciphertext = list(str(ciphertext))
    plaintext = []
    for x in range(len(ciphertext)):
        upper = False
        if ciphertext[x].isupper():
            upper = True
        elif ord(ciphertext[x]) not in ascii_char_range:
            plaintext.append(ciphertext[x])
            continue
        char_code = ord(ciphertext[x].lower()) - ascii_char_range[0]
        for y in range(1, 26):
            if a * y % 26 == 1:
                char_code = y * (char_code - (b % 26) + 26)
                while True:
                    if char_code >= 26:
                        char_code = char_code % 26
                    else:
                        break
                letter = dict_code_to_letter[char_code+1]
                if upper:
                    letter = letter.upper()
                plaintext.append(letter)

    return ''.join(plaintext)


def caesar_cipher_encryptor(plaintext, shift):
    plaintext = list(str(plaintext))
    ciphertext = []
    shift = shift % 26
    for x in range(len(plaintext)):
        upper = False
        if plaintext[x].isupper():
            upper = True
        elif ord(plaintext[x]) not in ascii_char_range:
            ciphertext.append(plaintext[x])
            continue
        char_code = ord(plaintext[x].lower()) - ascii_char_range[0]+1
        char_code = char_code + shift
        while True:
            if char_code > 26:
                char_code = char_code % 26
            else:
                break
        letter = dict_code_to_letter[char_code]
        if upper:
            letter = letter.upper()
        ciphertext.append(letter)
    return ''.join(ciphertext)


def caesar_cipher_decrypter(ciphertext, shift):
    ciphertext = list(str(ciphertext))
    plaintext = []
    shift = shift % 26
    for x in range(len(ciphertext)):
        upper = False
        if ciphertext[x].isupper():
            upper = True
        elif ord(ciphertext[x]) not in ascii_char_range:
            plaintext.append(ciphertext[x])
            continue
        char_code = ord(ciphertext[x].lower()) - ascii_char_range[0]+1
        char_code = 26 + char_code - shift
        while True:
            if char_code > 26:
                char_code = char_code % 26
            else:
                break
        letter = dict_code_to_letter[char_code]
        if upper:
            letter = letter.upper()
        plaintext.append(letter)
    return ''.join(plaintext)


class InputTypes:
    def extract_str(x):
        try:
            return int(x)
        except:
            return x


def main():
    parser = argparse.ArgumentParser(prog='pyciph', description='a Python script capable of decryption, encryption', )
    subparsers = parser.add_subparsers(title='procedures', dest='command', )
    # command: decrypt
    parser_decrypt = subparsers.add_parser('decrypt', help='decrypt the given ciphertext', )
    parser_decrypt.add_argument('--affine', metavar=('PLAINTEXT', 'a', 'b'), type=InputTypes.extract_str, nargs=3,
                                help='use the affine cipher (with f(x) = ax+b function)', )
    parser_decrypt.add_argument('--caesar', metavar=('CIPHERTEXT', 'SHIFT'), type=InputTypes.extract_str, nargs=2,
                                help='use the Caesar cipher with given shift', )
    parser_decrypt.add_argument('--rot13', metavar='CIPHERTEXT', type=str, help='use the ROT13 cipher', )
    # command: encrypt
    parser_encrypt = subparsers.add_parser('encrypt', help='encrypt the given plaintext', )
    parser_encrypt.add_argument('--affine', metavar=('PLAINTEXT', 'a', 'b'), type=InputTypes.extract_str, nargs=3,
                                help='use the affine cipher (with f(x) = ax+b function)', )
    parser_encrypt.add_argument('--caesar', metavar=('PLAINTEXT', 'SHIFT'), type=InputTypes.extract_str, nargs=2,
                                help='use the Caesar cipher with given shift', )
    parser_encrypt.add_argument('--rot13', metavar='PLAINTEXT', type=str, help='use the ROT13 cipher', )

    # parse arguments
    args = parser.parse_args()

    if not args.command:
        parser.parse_args(['--help'])
        sys.exit(0)
    # Do the stuff here
    if args.command == 'decrypt':
        if args.affine:
            print(affine_cipher_decrypter(args.affine[0], args.affine[1], args.affine[2]))
        elif args.caesar:
            print(caesar_cipher_decrypter(args.caesar[0], args.caesar[1]))
        elif args.rot13:
            print(caesar_cipher_decrypter(args.rot13, 13))
        else:
            parser.parse_args(['decrypt', '-h'])
    elif args.command == 'encrypt':
        if args.affine:
            print(affine_cipher_encryptor(args.affine[0], args.affine[1], args.affine[2]))
        elif args.caesar:
            print(caesar_cipher_encryptor(args.caesar[0], args.caesar[1]))
        elif args.rot13:
            print(caesar_cipher_encryptor(args.rot13, 13))
        else:
            parser.parse_args(['encrypt', '-h'])


if __name__ == '__main__':
    main()

