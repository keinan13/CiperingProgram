import os

class Encryption:
    def __init__(self):
        pass

    @staticmethod
    def clean_text(text):
        return ''.join(filter(str.isalpha, text)).lower()

    def shift_encrypt(self, text, key):
        text = self.clean_text(text)
        result = ""
        for char in text:
            result += chr((ord(char) - 97 + key) % 26 + 97)
        return result

    def shift_decrypt(self, text, key):
        return self.shift_encrypt(text, -key)

    def atbash_encrypt_decrypt(self, text):
        text = self.clean_text(text)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        atbash_key = alphabet[::-1]
        result = text.translate(str.maketrans(alphabet, atbash_key))
        return result

    def modulo_encrypt(self, text, key):
        text = self.clean_text(text)
        result = []
        for char in text:
            num = (ord(char) - 97 + key) % 26
            result.append(str(num))
        return ','.join(result)

    def modulo_decrypt(self, text, key):
        result = ""
        numbers = text.split(',')
        for num in numbers:
            char = chr((int(num) - key + 26) % 26 + 97)
            result += char
        return result

    def transposition_encrypt(self, text):
        text = self.clean_text(text)
        return text[::-1]

    def transposition_decrypt(self, text):
        return self.transposition_encrypt(text)

    def zigzag_encrypt(self, text, key):
        text = self.clean_text(text)
        if key >= len(text):
            return text + "\n(Note: If the key is bigger than the number of characters in the word/sentence to encrypt, the word remains the same)"
        if key == 1:
            return text
        rail = [['\n' for _ in range(len(text))] for _ in range(key)]
        dir_down = False
        row, col = 0, 0
        for i in range(len(text)):
            if (row == 0) or (row == key - 1):
                dir_down = not dir_down
            rail[row][col] = text[i]
            col += 1
            if dir_down:
                row += 1
            else:
                row -= 1
        result = []
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])
        return "".join(result)

    def zigzag_decrypt(self, text, key):
        text = self.clean_text(text)
        if key == 1:
            return text
        rail = [['\n' for _ in range(len(text))] for _ in range(key)]
        dir_down = None
        row, col = 0, 0
        for i in range(len(text)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
            rail[row][col] = '*'
            col += 1
            if dir_down:
                row += 1
            else:
                row -= 1
        index = 0
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] == '*' and index < len(text):
                    rail[i][j] = text[index]
                    index += 1
        result = []
        row, col = 0, 0
        for i in range(len(text)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
            if rail[row][col] != '*':
                result.append(rail[row][col])
                col += 1
            if dir_down:
                row += 1
            else:
                row -= 1
        return "".join(result)

class Helpers:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_help(encryption_type):
        text = "yehudaandamir"
        key = 3
        encryption = Encryption()
        if encryption_type == "Shift Cipher":
            example = encryption.shift_encrypt(text, key)
            detailed_explanation = (
                f"Shift Cipher Example:\n"
                f"Original: {text}\n"
                f"Shift Key: {key}\n"
                f"Encrypted: {example}\n\n"
                f"Explanation: Each letter in '{text}' is shifted {key} places down the alphabet. For example, 'a' becomes 'd', 'b' becomes 'e', and so on."
            )
        elif encryption_type == "Substitution Cipher (Atbash)":
            example = encryption.atbash_encrypt_decrypt(text)
            detailed_explanation = (
                f"Atbash Cipher Example:\n"
                f"Original: {text}\n"
                f"Encrypted: {example}\n\n"
                f"Explanation: The Atbash cipher reverses the alphabet, so 'a' becomes 'z', 'b' becomes 'y', and so on.\n"
                f"  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z\n"
                f"  Z Y X W V U T S R Q P O N M L K J I H G F E D C B A"
            )
        elif encryption_type == "Modulo Cipher":
            example = encryption.modulo_encrypt(text, key)
            detailed_explanation = (
                f"Modulo Cipher Example:\n"
                f"Original: {text}\n"
                f"Key: {key}\n"
                f"Encrypted: {example}\n\n"
                f"Explanation: Each letter in '{text}' is converted to a number (a=0, b=1, ..., z=25), then the key is added and the result is taken modulo 26. The result is converted back to letters."
            )
        elif encryption_type == "Transposition Cipher":
            example = encryption.transposition_encrypt(text)
            detailed_explanation = (
                f"Transposition Cipher Example:\n"
                f"Original: {text}\n"
                f"Encrypted: {example}\n\n"
                f"Explanation: The characters in '{text}' are reversed."
            )
        elif encryption_type == "Zigzag Cipher":
            example = encryption.zigzag_encrypt(text, key)
            detailed_explanation = (
                f"Zigzag Cipher Example:\n"
                f"Original: {text}\n"
                f"Key (rails): {key}\n"
                f"Encrypted: {example}\n\n"
                f"Explanation: Characters are written in a zigzag pattern on {key} 'rails' and then read off row by row."
            )
        print(f"====================================")
        print(f"        HELP - {encryption_type}")
        print(f"====================================")
        print(f"{detailed_explanation}")
        print(f"====================================")
        input("Press Enter to continue...")

class Cosmetics:
    @staticmethod
    def print_main_menu():
        print("===========================================")
        print("              WELCOME TO")
        print("    YEHUDA AND AMIRs CIPERING PROGRAM")
        print("===========================================")
        print("WHICH ENCRYPTION TYPE DO YOU WANT TO USE?")
        print("===========================================")
        print("1. Shift Cipher")
        print("2. Substitution Cipher (Atbash)")
        print("3. Modulo Cipher")
        print("4. Transposition Cipher")
        print("5. Zigzag Cipher")
        print("6. Quit")
        print("===========================================")

    @staticmethod
    def print_inner_menu(encryption_type):
        print("====================================")
        print(f"     {encryption_type} MENU")
        print("====================================")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Help")
        print("4. Quit")
        print("====================================")

    @staticmethod
    def print_locked_box():
        print(r"""
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
""")

    @staticmethod
    def print_open_box():
        print(r"""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
""")

def menu():
    while True:
        Helpers.clear_screen()
        Cosmetics.print_main_menu()
        choice = input("Select encryption type (1-6): ")
        if choice in ['1', '2', '3', '4', '5', '6']:
            return choice
        else:
            print("Invalid choice. Please select a number between 1 and 6.")
            input("Press Enter to continue...")

def inner_menu(encryption_type):
    while True:
        Helpers.clear_screen()
        Cosmetics.print_inner_menu(encryption_type)
        choice = input("Select an option (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Invalid option. Please select 1, 2, 3, or 4.")
            input("Press Enter to continue...")

def main():
    encryption = Encryption()
    while True:
        choice = menu()
        if choice == '6':
            print("Thank you for using the Encryption/Decryption program. Goodbye!")
            input("Press Enter to exit...")
            break
        elif choice == '1':
            encryption_type = "Shift Cipher"
            while True:
                option = inner_menu(encryption_type)
                if option == '4':
                    break
                elif option == '3':
                    Helpers.print_help(encryption_type)
                    continue
                text = input("Enter text: ")
                try:
                    key = int(input("Enter key: "))
                except ValueError:
                    print("Invalid key. Please enter a numeric value.")
                    input("Press Enter to continue...")
                    continue
                if option == '1':
                    print("Encrypted:", encryption.shift_encrypt(text, key))
                    Cosmetics.print_locked_box()
                elif option == '2':
                    print("Decrypted:", encryption.shift_decrypt(text, key))
                    Cosmetics.print_open_box()
                input("Press Enter to continue...")
        elif choice == '2':
            encryption_type = "Substitution Cipher (Atbash)"
            while True:
                option = inner_menu(encryption_type)
                if option == '4':
                    break
                elif option == '3':
                    Helpers.print_help(encryption_type)
                    continue
                text = input("Enter text: ")
                if option == '1':
                    print("Encrypted:", encryption.atbash_encrypt_decrypt(text))
                    Cosmetics.print_locked_box()
                elif option == '2':
                    print("Decrypted:", encryption.atbash_encrypt_decrypt(text))
                    Cosmetics.print_open_box()
                input("Press Enter to continue...")
        elif choice == '3':
            encryption_type = "Modulo Cipher"
            while True:
                option = inner_menu(encryption_type)
                if option == '4':
                    break
                elif option == '3':
                    Helpers.print_help(encryption_type)
                    continue
                text = input("Enter text: ")
                try:
                    key = int(input("Enter key: "))
                except ValueError:
                    print("Invalid key. Please enter a numeric value.")
                    input("Press Enter to continue...")
                    continue
                if option == '1':
                    print("Encrypted:", encryption.modulo_encrypt(text, key))
                    Cosmetics.print_locked_box()
                elif option == '2':
                    print("Decrypted:", encryption.modulo_decrypt(text, key))
                    Cosmetics.print_open_box()
                input("Press Enter to continue...")
        elif choice == '4':
            encryption_type = "Transposition Cipher"
            while True:
                option = inner_menu(encryption_type)
                if option == '4':
                    break
                elif option == '3':
                    Helpers.print_help(encryption_type)
                    continue
                text = input("Enter text: ")
                if option == '1':
                    print("Encrypted:", encryption.transposition_encrypt(text))
                    Cosmetics.print_locked_box()
                elif option == '2':
                    print("Decrypted:", encryption.transposition_decrypt(text))
                    Cosmetics.print_open_box()
                input("Press Enter to continue...")
        elif choice == '5':
            encryption_type = "Zigzag Cipher"
            while True:
                option = inner_menu(encryption_type)
                if option == '4':
                    break
                elif option == '3':
                    Helpers.print_help(encryption_type)
                    continue
                text = input("Enter text: ")
                try:
                    key = int(input("Enter key: "))
                except ValueError:
                    print("Invalid key. Please enter a numeric value.")
                    input("Press Enter to continue...")
                    continue
                if option == '1':
                    print("Encrypted:", encryption.zigzag_encrypt(text, key))
                    Cosmetics.print_locked_box()
                elif option == '2':
                    print("Decrypted:", encryption.zigzag_decrypt(text, key))
                    Cosmetics.print_open_box()
                input("Press Enter to continue...")
        Helpers.clear_screen()

if __name__ == "__main__":
    main()
