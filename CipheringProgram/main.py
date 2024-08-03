from encryption import Encryption
from helpers import Helpers
from cosmetics import Cosmetics

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
            print("Thank you for using Yehuda and Amir's ciphering program. Goodbye!")
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
