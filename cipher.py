import getpass
#importing the user automated password or we can say we impoet the pathway where user inputs his/her password according to the instruction provided
print("!!!!!!<--------------------------------------------* Caesar Cipher Tool *-------------------------------------------------->!!!!!!")
print(" ")



#defining the message!!
def analyze_message(message):
    num_letters = sum(c.isalpha() for c in message)
    num_digits = sum(c.isdigit() for c in message)
    num_special = len(message) - num_letters - num_digits

    print("Please check the message you wrote was correct or not by using certain links:")
    print("\nFirst and last characters of the message: {message[:1]}***{message[-1]}")
    print("Total number of characters entered: {len(message)}")
    print("Number of alphabetical letters: {num_letters}")
    print("Number of digits: {num_digits}")
    
    if num_special > 0:
        print("Number of special characters: {num_special}")
        print("Special characters are present in the message.")
    else:
        print("No special characters in the message.")

def caesar_cipher(text, shift, action):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            if action == 'e':
                result_char = chr((ord(char) - start + shift) % 26 + start)
            elif action == 'd':
                result_char = chr((ord(char) - start - shift) % 26 + start)
            else:
                raise ValueError("Invalid action. Use 'e' to encrypt or 'd' to decrypt")
            result += result_char
        else:
            result += char
    return result

def main():
    while True:
        action = input("Do you want to encrypt or decrypt a message? Input 'e' for encryption, 'd' for decryption, or 'q' to quit: ").lower()
        if action == 'q':
            print("Exiting the program. Goodbye!")
            return
        elif action in ['e', 'd']:
            break
        else:
            print("Invalid action. Please choose 'e', 'd', or 'q' to quit.")

    if action == 'q':
        return

    # here we use getpass library to make our message visible.....!!!
    message = getpass.getpass(prompt="Enter the message (invisible, type carefully): ")

    if action != 'q':
        analyze_message(message)

        # Use of getpass to make the shift value input invisible
        shift = int(getpass.getpass(prompt="Enter the shift value (invisible, type carefully): "))

        if action == 'e':
            result = caesar_cipher(message, shift, 'e')
            print("\nEncrypted Message:", result)
        elif action == 'd':
            result = caesar_cipher(message, shift, 'd')
            print("\nDecrypted Message:", result)

if __name__ == "__main__":
    main()
