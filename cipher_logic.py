
import random
import os

#Random will need a seed to prevent the characters from being scrambled every run.
all_possible_Chars = list(range(65, 91)) + list(range(97, 123)) + list(range(48, 58)) + list(range(32, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def character_list_builder(shift):
    char_array = all_possible_Chars.copy()
    random.seed(shift)
    random.shuffle(char_array)

def encypt_or_decrypt(x):
    if(x.lower() == "encrypt" or x.lower() == "e"):
        return('Mask')
    elif(x.lower() == "decrypt" or x.lower() == "d"):
        return("Reveal")
    else:
        return(print("Invalid response, please enter encrypt or decrypt. E or D will also work!"))

def get_key_and_message():
    while True:
        x = input("What number value should be the shift for the cipher? : ")
        if x.strip().lstrip('-').isdigit():
            shift = x
            break
        else:
            print("Please enter a number for the shift.")
    while True:
        y = input("What is the secret message? : ")
        if not y.strip():
            print("The message cannot be empty.")
        else:
            break
    return shift, y

def message_cipher(shift, text):
    character_list_builder(abs(int(shift)))
    shift = int(shift)
    message_list = list(text)

    for i, character in enumerate(message_list):
        ascii_val = ord(character)
        if ascii_val in all_possible_Chars:
            idx = all_possible_Chars.index(ascii_val)
            new_idx = (idx + shift) % len(all_possible_Chars)
            message_list[i] = chr(all_possible_Chars[new_idx])
        else:
            #Debug..
            return("Character not found in table: "+ character)

    return ''.join(message_list)