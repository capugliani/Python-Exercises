alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

reseting_shift = 1
full_loops = 0

for shift in range(1, shift+1):
    if reseting_shift == 26:
        reseting_shift = 1
        full_loops += 1
    reseting_shift += 1
fixing_number = shift - (full_loops * 26)

def encrypt(text_function, shift_function):
    encrypt_counting = 0
    crypto_list = []
    encrypting_text = list(text_function)

    for item in encrypting_text:
        letter_counting = 0
        if item == ' ':
            crypto_list.append(' ')
        for letter in alphabet:
            if encrypting_text[encrypt_counting] == alphabet[letter_counting]:
                if letter_counting+shift_function >= 25:
                    actual_letter = letter_counting+shift_function - 25
                    crypto_list.append(alphabet[actual_letter])
                else:
                    crypto_list.append(alphabet[letter_counting + shift_function])
            letter_counting += 1
        encrypt_counting += 1
    print(''.join(crypto_list))

def decrypt(text_function, shift_function):
    decrypt_counting = 0
    decrypto_list = []
    decrypting_text = list(text_function)

    for item in decrypting_text:
        letter_counting = 0
        for letter in alphabet:
            if decrypting_text[decrypt_counting] == alphabet[letter_counting]:
                if letter_counting+shift_function >= 25:
                    actual_letter = letter_counting-shift_function - 25
                    decrypto_list.append(alphabet[actual_letter])
                else:
                    decrypto_list.append(alphabet[letter_counting-shift_function])
            letter_counting += 1
        decrypt_counting += 1
    print(''.join(decrypto_list))

if direction == 'encode':
    encrypt(text_function=text, shift_function=fixing_number)
elif direction == 'decode':
    decrypt(text_function=text, shift_function=fixing_number)
else:
    print("Sorry, but i didn't understand if you want to encode or decode!")

