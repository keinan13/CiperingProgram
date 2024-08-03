import os
from encryption import Encryption

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
