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


def vigenere_cipher_encryptor(plaintext, key):
    # format the key
    key = key.lower().strip()
    # check, if key contains any char that IS NOT a letter. If so, break the process and return error
    for x in range(len(key)):
        if ord(key[x]) not in ascii_char_range:
            print("ERROR")
            return None
    ciphertext = []
    k = 0
    for x in range(len(plaintext)):
        # check if char is uppercase
        upper = False
        if plaintext[x].isupper():
            upper = True
        # check if the char is letter
        elif ord(plaintext[x]) not in ascii_char_range:
            ciphertext.append(plaintext[x])
            continue
        # calculate the shift
        n = dict_letter_to_code[plaintext[x].lower()] - 1
        # obtain the encrypted letter by using Caesar cipher with calculated shift
        letter = caesar_cipher_encryptor(key[k], n)
        # if input letter was uppercase, restore it's original case
        if upper:
            letter = letter.upper()
        # append the encrypted letter to the list
        ciphertext.append(letter)
        # loop the key
        k += 1
        if k == len(key):
            k = 0
    return ''.join(ciphertext)


def vigenere_cipher_decrypter(ciphertext, key):
    # format the key
    key = key.lower().strip()
    # check, if key contains any char that IS NOT a letter. If so, break the process and return error
    for x in range(len(key)):
        if ord(key[x]) not in ascii_char_range:
            print("ERROR")
            return None
    plaintext = []
    k = 0
    for x in range(len(ciphertext)):
        # check if char is uppercase
        upper = False
        if ciphertext[x].isupper():
            upper = True
        # check if the char is letter
        elif ord(ciphertext[x]) not in ascii_char_range:
            plaintext.append(ciphertext[x])
            continue
        # calculate the shift
        n = dict_letter_to_code[key[k]] - 1
        # obtain the decrypted letter by using Caesar cipher with calculated shift
        letter = caesar_cipher_decrypter(ciphertext[x], n)
        # if input letter was uppercase, restore it's original case
        if upper:
            letter = letter.upper()
        # append the decrypted letter to the list
        plaintext.append(letter)
        # loop the key
        k += 1
        if k == len(key):
            k = 0
    return ''.join(plaintext)


def rail_fence_cipher_encryptor(plaintext, n):
    plaintext = plaintext.lower()
    # create matrix where the plaintext will be placed
    matrix = [[' ' for x in range(len(plaintext))] for y in range(n)]
    # start from row 1
    row = 1
    decreasing = False
    for x in range(len(plaintext)):
        # check if the char is A-Z letter
        if ord(plaintext[x]) not in ascii_char_range:
            continue
        # perform char placement - when last row is meet, decrease the row from last to the first
        # algorithm creates so called 'rail fence'
        if not decreasing:
            matrix[row-1][x] = plaintext[x]
            row += 1
            if row == n:
                decreasing = True
        else:
            matrix[row-1][x] = plaintext[x]
            row -= 1
            if row == 1:
                decreasing = False
    ciphertext = []
    # join the cipher row by row
    for row in range(len(matrix)):
        ciphertext.append(''.join(matrix[row]))
    return [''.join(ciphertext).replace(' ', '').upper(), matrix]


class InputTypes:
    def extract_str(x):
        try:
            return int(x)
        except:
            return x


def main():
    parser = argparse.ArgumentParser(prog='pyciph', description='pyciph - commandline tool for encryption and decryption with classical ciphers', )
    # global flags
    parser.add_argument('-q', '--quiet', action='store_true', help='pyciph will return only the output string')
    parser.add_argument('-v', '--verbose', action='store_true', help='pyciph will return more information about the process')
    subparsers = parser.add_subparsers(title='procedures', dest='command', )

    # procedure: encrypt
    parser_encrypt = subparsers.add_parser('encrypt', help='encrypt the given plaintext', )
    parser_encrypt.add_argument('--affine', metavar=('PLAINTEXT', 'a', 'b'), type=InputTypes.extract_str, nargs=3,
                                help='use the Affine cipher (linear function)', )
    parser_encrypt.add_argument('--atbash', metavar=('PLAINTEXT'), type=str,
                                help='use the Atbash cipher (affine cipher with a=25, b=25)', )
    parser_encrypt.add_argument('--caesar', metavar=('PLAINTEXT', 'SHIFT'), type=InputTypes.extract_str, nargs=2,
                                help='use the Caesar cipher with given shift', )
    parser_encrypt.add_argument('--vigenere', metavar=('PLAINTEXT', 'KEY'), type=str, nargs=2,
                                help='use the Vigenere cipher with given key')
    parser_encrypt.add_argument('--rail-fence', metavar=('PLAINTEXT', 'n'), type=InputTypes.extract_str, nargs=2,
                                help='use Rail Fence cipher with given height of the matrix')
    parser_encrypt.add_argument('--rot13', metavar='PLAINTEXT', type=str,
                                help='use the ROT13 cipher (Caesar cipher with shift = 13)', )

    # procedure: decrypt
    parser_decrypt = subparsers.add_parser('decrypt', help='decrypt the given ciphertext', )
    parser_decrypt.add_argument('--affine', metavar=('PLAINTEXT', 'a', 'b'), type=InputTypes.extract_str, nargs=3,
                                help='use the Affine cipher (linear function)', )
    parser_decrypt.add_argument('--atbash', metavar=('CIPHERTEXT'), type=str,
                                help='use the Atbash cipher (affine cipher with a=25, b=25)', )
    parser_decrypt.add_argument('--caesar', metavar=('CIPHERTEXT', 'SHIFT'), type=InputTypes.extract_str, nargs=2,
                                help='use the Caesar cipher with given shift', )
    parser_decrypt.add_argument('--vigenere', metavar=('CIPHERTEXT', 'KEY'), type=str, nargs=2,
                                help='use the Vigenere cipher with given key')
    parser_decrypt.add_argument('--rot13', metavar='CIPHERTEXT', type=str,
                                help='use the ROT13 cipher (Caesar cipher with shift = 13)', )

    # parse arguments
    args = parser.parse_args()

    if not args.command:
        parser.parse_args(['--help'])
        sys.exit(0)
    # procedure: encrypt
    if args.command == 'encrypt':
        if args.affine:
            if not args.quiet:
                print("Using Affine cipher")
                if args.verbose:
                    print('Verbose - nothing more to show')
                print("Slope (a): %s, Intercept (b): %s" % (args.affine[1], args.affine[2]))
                print('Plaintext: %s\n' % args.affine[0])
                print('Ciphertext: %s' % affine_cipher_encryptor(args.affine[0], args.affine[1], args.affine[2]))
            else:
                print(affine_cipher_encryptor(args.affine[0], args.affine[1], args.affine[2]))
        elif args.atbash:
            if not args.quiet:
                print("Using Atbash cipher")
                if args.verbose:
                    print('Verbose - nothing more to show')
                print('Plaintext: %s\n' % args.atbash)
                print('Ciphertext: %s' % affine_cipher_encryptor(args.atbash, 25, 25))
            else:
                print(affine_cipher_encryptor(args.atbash, 25, 25))
        elif args.caesar:
            if not args.quiet:
                print("Using Caesar cipher")
                if args.verbose:
                    print('Verbose - nothing more to show')
                print('Shift = %s: a → %s' % (str(args.caesar[1]), caesar_cipher_encryptor('a', args.caesar[1])))
                print('Plaintext: %s\n' % args.caesar[0])
                print('Ciphertext: %s' % caesar_cipher_encryptor(args.caesar[0], args.caesar[1]))
            else:
                print(caesar_cipher_encryptor(args.caesar[0], args.caesar[1]))
        elif args.vigenere:
            if not args.quiet:
                print('Using Vigenere cipher')
                if args.verbose:
                    print('Verbose - nothing more to show')
                print('Key: %s' % args.vigenere[1])
                print('Plaintext: %s\n' % args.vigenere[0])
                print('Ciphertext: %s' % vigenere_cipher_encryptor(args.vigenere[0], args.vigenere[1]))
            else:
                print(vigenere_cipher_encryptor(args.vigenere[0], args.vigenere[1]))
        elif args.rail_fence:
            output = rail_fence_cipher_encryptor(args.rail_fence[0], args.rail_fence[1])
            cipher = output[0]
            matrix = output[1]
            if not args.quiet:
                print('Key = %s' % args.rail_fence[1])
                print('Plaintext: %s' % args.rail_fence[0])
                if args.verbose:
                    print('Matrix: ')
                    for x in range(len(matrix)):
                        print(matrix[x])
                print('\nCiphertext: %s' % cipher)
            else:
                print(cipher)
        elif args.rot13:
            if not args.quiet:
                print("Using ROT13 cipher")
                if args.verbose:
                    print('Verbose - nothing more to show')
                print('Plaintext: %s\n' % args.rot13)
                print('Ciphertext: %s' % caesar_cipher_encryptor(args.rot13, 13))
            else:
                print(caesar_cipher_encryptor(args.rot13, 13))
        else:
            parser.parse_args(['encrypt', '-h'])

    # procedure: decrypt
    elif args.command == 'decrypt':
        if args.affine:
            if not args.quiet:
                print("Using Affine cipher")
                if args.verbose:
                    print('Verbose - nothing more to show')
                print("Slope (a): %s, Intercept (b): %s" % (args.affine[1], args.affine[2]))
                print('Ciphertext: %s\n' % args.affine[0])
                print('Plaintext: %s' % affine_cipher_decrypter(args.affine[0], args.affine[1], args.affine[2]))
            else:
                print(affine_cipher_decrypter(args.affine[0], args.affine[1], args.affine[2]))
        elif args.atbash:
            if not args.quiet:
                print("Using Atbash cipher")
                if args.verbose:
                    print('Verbose - nothing more to show')
                print('Plaintext: %s\n\nCiphertext: %s' % (args.atbash, affine_cipher_encryptor(args.atbash, 25, 25)))

            else:
                print(affine_cipher_decrypter(args.atbash, 25, 25))
        elif args.caesar:
            if not args.quiet:
                print("Using Caesar cipher")
                if args.verbose:
                    print('Verbose - nothing more to show')
                print('Shift = %s: a → %s' % (args.caesar[1], caesar_cipher_encryptor('a', args.caesar[1])))
                print('Ciphertext: %s\n' % args.caesar[0])
                print('Plaintext: %s' % caesar_cipher_decrypter(args.caesar[0], args.caesar[1]))
            else:
                print(caesar_cipher_decrypter(args.caesar[0], args.caesar[1]))
        elif args.vigenere:
            if not args.quiet:
                print("Using Vigenere cipher")
                if args.verbose:
                    print('Verbose - nothing more to show')
                print('Key: %s' % args.vigenere[1])
                print('Ciphertext: %s\n' % args.vigenere[0])
                print('Plaintext: %s' % vigenere_cipher_decrypter(args.vigenere[0], args.vigenere[1]))
            else:
                print(vigenere_cipher_decrypter(args.vigenere[0], args.vigenere[1]))
        elif args.rot13:
            if not args.quiet:
                print("Using ROT13 cipher")
                if args.verbose:
                    print('Verbose - nothing more to show')
                print('Ciphertext: %s\n' % args.rot13)
                print('Plaintext: %s' % caesar_cipher_decrypter(args.rot13, 13))
            else:
                print(caesar_cipher_decrypter(args.rot13, 13))
        else:
            parser.parse_args(['decrypt', '-h'])


if __name__ == '__main__':
    main()

# TODO
# - vigenere cipher decrypter
# - rail fence cipher decrypter
