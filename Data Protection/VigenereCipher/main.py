import string
from vigenere import VigenereCipher


def main():
    lst  = [' ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    pattern_container = []
    cipher_container = []
    #final_table = [lst[i:]+lst[:i] for i in range(len(lst))]
    obj = VigenereCipher(lst)
    obj.input('pattern.txt', pattern_container)
    obj.input('to_code.txt', cipher_container)




    # obj.decode('ZAB')
    obj.friedman_method(pattern_container,cipher_container)
  
    

if __name__ == "__main__":
    main()