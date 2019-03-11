import string
from caesar_class import CaesarCypher

def myDict():
    lst = [x for x in string.ascii_uppercase]
    lst.append(' ')
    return lst


def main():
    alph = myDict()

    obj = CaesarCypher(alph, 35)
    obj.input('to_code.txt')
    obj.encode()

    obj2 = CaesarCypher(alph, 35)
    obj2.input('encoded.txt')
    obj2.decode('right')



if __name__ == "__main__":
    main()
