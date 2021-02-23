import argparse
import sys

# generate ASCII table range
ascii_char_range = [i for i in range(65,91)]
# generate ASCII code to letter dictionary
dict_code_to_letter = {i - 64: chr(i) for i in ascii_char_range}
# generate ASCII letter to code dictionary
dict_letter_to_code = {chr(i): i - 64 for i in ascii_char_range}


def caesar_cipher_encryptor(plaintext, shift):
    plaintext = list(plaintext.upper())
    ciphertext = []
    shift = shift % 26
    for x in range(len(plaintext)):
        if ord(plaintext[x]) not in ascii_char_range:
            ciphertext.append(plaintext[x])
            continue
        char_code = ord(plaintext[x]) - ascii_char_range[0]+1
        char_code = char_code + shift
        while True:
            if char_code > 26:
                char_code = char_code % 26
            else:
                break
        ciphertext.append(dict_code_to_letter[char_code])
    return ''.join(ciphertext).lower()


def caesar_cipher_decrypter(ciphertext, shift):
    ciphertext = list(ciphertext.upper())
    plaintext = []
    shift = shift % 26
    for x in range(len(ciphertext)):
        if ord(ciphertext[x]) not in ascii_char_range:
            plaintext.append(ciphertext[x])
            continue
        char_code = ord(ciphertext[x]) - ascii_char_range[0]+1
        char_code = 26 + char_code - shift
        while True:
            if char_code > 26:
                char_code = char_code % 26
            else:
                break
        plaintext.append(dict_code_to_letter[char_code])
    return ''.join(plaintext).lower()


def caesar_cipher_cracker(ciphertext):
    ciphertext = list(ciphertext.upper())
    lst = []
    for shift in range(1, 26):
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
        lst.append(''.join(plaintext) + ' (shift = %d)' % shift)
    return lst


class InputTypes:
    def str_int(x):
        try:
            return int(x)
        except:
            return x


def main():
    parser = argparse.ArgumentParser(prog='pyciph', description='a Python script capable of decryption, encryption and cracking', )
    subparsers = parser.add_subparsers(title='procedures', dest='command', )
    # command: decrypt
    parser_decrypt = subparsers.add_parser('decrypt', help='decrypt the given ciphertext', )
    parser_decrypt.add_argument('-c', metavar=('CIPHERTEXT', 'SHIFT'), type=InputTypes.str_int, nargs=2,
                                help='use the Caesar cipher with given shift', )
    parser_decrypt.add_argument('-r', metavar='CIPHERTEXT', type=str, help='use the ROT13 cipher', )
    # command: encrypt
    parser_encrypt = subparsers.add_parser('encrypt', help='encrypt the given plaintext', )
    parser_encrypt.add_argument('-c', metavar=('PLAINTEXT', 'SHIFT'), type=InputTypes.str_int, nargs=2,
                                help='use the Caesar cipher with given shift', )
    parser_encrypt.add_argument('-r', metavar='PLAINTEXT', type=str, help='use the ROT13 cipher', )
    # command: crack
    parser_crack = subparsers.add_parser('crack', help='crack the cipher')
    parser_crack.add_argument('-c', type=str, help='use the Caesar cipher', )

    # parse arguments
    args = parser.parse_args()

    if not args.command:
        parser.parse_args(['--help'])
        sys.exit(0)
    # Do the stuff here
    if args.command == 'decrypt':
        if args.c:
            print(caesar_cipher_decrypter(args.c[0], args.c[1]))
        elif args.r:
            print(caesar_cipher_decrypter(args.r, 13))
        else:
            parser.parse_args(['decrypt', '-h'])
    elif args.command == 'encrypt':
        if args.c:
            print(caesar_cipher_encryptor(args.c[0], args.c[1]))
        elif args.r:
            print(caesar_cipher_encryptor(args.r, 13))
        else:
            parser.parse_args(['encrypt', '-h'])
    elif args.command == 'crack':
        if args.c:
            lst = caesar_cipher_cracker(args.c)
            for x in range(0, 25):
                print(lst[x])
        else:
            parser.parse_args(['crack', '-h'])


if __name__ == '__main__':
    main()

