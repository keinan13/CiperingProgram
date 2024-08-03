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
