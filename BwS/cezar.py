import string
from caesar_class import CaesarCypher

def myDict():
    lst = [x for x in string.ascii_uppercase]
    lst.append(' ')
    return lst


def main():
    alph = myDict()

    while True:
        print("Wybierz opcje")
        print("1. encoded - zakodowanie 2. decoded zaszyfrowanie")
        choice = str(input())
        if choice == 'encode':
            print("wybierz przesuniecie")
            shift = input()
            obj = CaesarCypher(alph, shift, choice)
            obj.input()
            obj.encode()
            obj.write_results()
            print("czy chcialbys zakonczyc  ? tak/nie")
            choice2 = str(input()) 
            if choice2 == 'tak':
                break
        elif choice == 'decode':
            print("wybierz przesuniecie i kierunek right/left")
            shift = input()
            direction = input()        
            obj = CaesarCypher(alph, shift, choice)
            obj.input()
            obj.decode(direction)
            obj.write_results()
            print("czy chcialbys zakonczyc  ? tak/nie")
            choice2 = str(input())
            if choice == 'tak':
                break


if __name__ == "__main__":
    main()
