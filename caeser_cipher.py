from cipher_logic import message_cipher, encypt_or_decrypt, get_key_and_message, clear_terminal
from caeser_logo import cipher_logo

def main():
    clear_terminal()
    print(cipher_logo)
    while True:
        cipher_key = 0
        message = ''

        while(encypt_or_decrypt != "Invalid response"):
            encrypt_decrypt = encypt_or_decrypt(input("Do you want to encrypt or decrypt a message? : "))
            if(encrypt_decrypt == "Mask"):
                cipher_key, message = get_key_and_message()
                encrypted_message = message_cipher(cipher_key, message)
                clear_terminal()
                print("Your encrypted message is :\n" + encrypted_message)
            elif(encrypt_decrypt == "Reveal"):
                cipher_key, message = get_key_and_message()
                encrypted_message = message_cipher(-int(cipher_key), message)
                clear_terminal()
                print("Your decrypted message is :\n" + encrypted_message)
            else:
                continue
            break      
        while True:
            again = input("Do you want to encrypt or decrypt again? Yes/No : ")
            if again.lower() == "yes" or again.lower() == "y":
                break
            elif again.lower() == "no" or again.lower() == "n":
                print("End program.")
                return
            else:
                print("Incorrect input, type yes or no. Y or N works as well.")

if __name__ == "__main__":
    main()