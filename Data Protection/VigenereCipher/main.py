import string
from vigenere import VigenereCipher


def main():
    lst  = [' ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    pattern_container = []
    cipher_container = []
  
    #final_table = [lst[i:]+lst[:i] for i in range(len(lst))]
    obj = VigenereCipher(lst)


   
    obj.input('pattern.txt', pattern_container)
    #obj.input('decoded.txt', cipher_container)
    obj.input('to_code.txt', cipher_container)  
    #obj.decode('abc',cipher_container)
    
    
    coded = obj.encode('ekl',cipher_container)
    obj.decode('ekl')
    #print(pattern_container)
    #print(cipher_container)
    #print(pattern_container)

    #coded = obj.encode('ZABC',cipher_container)
    #decoded = obj.decode('ZABC')


    #obj.decode('ZABC',cipher_container)
    obj.friedman_method(pattern_container,coded)
  
    

if __name__ == "__main__":
    main()