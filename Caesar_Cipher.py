#this will be the new caesar cipher class.
class CaesarCipher:
    def __init__(self):
        self.lines = []#list

    def read_file(self, filename):
        with open(filename, "r") as f:#f acts like a variable name
            self.lines = f.readlines()#store each line as a string in the list

    def encrypt_line(self, line:str, shifts:int) -> str:
        result = ""#return
        is_upper = False

        temp_char = ''
        for char in line:

            if not char.isalpha():
                result += char
                continue

            if char.isupper():
                is_upper = True
                temp_char = char.lower()
            else:
                temp_char = char

            alphabet_index = ord(temp_char) - ord('a')
            shifted_index = (alphabet_index + shifts) % 26
            temp_char = chr(shifted_index + ord('a'))

            if is_upper:
                temp_char = temp_char.upper()

            result += temp_char
            
        return result
        
    def decrypt_line(self, line:str, shifts:int) -> str:
        result = ""
        is_upper = False

        temp_char = ''
        for char in line:

            if not char.isalpha():
                result += char
                continue

            if char.isupper():
                is_upper = True
                temp_char = char.lower()
            else:
                temp_char = char

            alphabet_index = ord(temp_char) - ord('a')
            shifted_index = (alphabet_index - shifts) % 26
            temp_char = chr(shifted_index + ord('a'))

            if is_upper:
                temp_char = temp_char.upper()

            result += temp_char
        
        return result      
