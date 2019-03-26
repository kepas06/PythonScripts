import string
from vigenere import VigenereCipher


def main():
    lst  = [' ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
 
    #final_table = [lst[i:]+lst[:i] for i in range(len(lst))]
    obj = VigenereCipher(lst)
    obj.input('to_code.txt')
    obj.encode('kasztan')
    obj.decode('kasztan')
    obj.frequency()
    

if __name__ == "__main__":
    main()