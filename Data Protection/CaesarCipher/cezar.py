import string
from caesar_class import CaesarCypher

def myDict():
    lst = [x for x in string.ascii_uppercase]
    lst.append(' ')
    return lst



def main():
    alph = myDict()

    obj = CaesarCypher(alph)
    obj.input('to_code.txt')
    obj.input_pattern('to_code2.txt')
    
    obj.comparsion(alph)
    obj.decode('right',3)
    

if __name__ == "__main__":
    main()
