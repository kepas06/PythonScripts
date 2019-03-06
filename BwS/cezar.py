import string

def myDict():
    lst = [x for x in string.ascii_uppercase]
    lst.append(' ')
    return lst

class CaesarCypher():

    dataContainer = []
    encoded = ""
    decoded = ""

    def __init__(self,myDict,shift,option):
        self.shift = shift
        self.dict = myDict
        self.option = option

    def input(self):
        print("enter the file")
         = input()
        choice
        file = open(choice)
        with file as file_handle:
            for line in file_handle:
                self.dataContainer+=line.upper()
        file.close()

    def encode(self):
        for x in self.dataContainer: 
            if x in self.dict:   
                pos = self.dict.index(x)
                nPos = (pos + self.shift) % len(self.dict)
                self.encoded += self.dict[nPos]
            else:
                self.encoded += x
        return self.encoded

    def decode(self,direction):
        for x in self.dataContainer:
            if direction == 'right':
                pos = (self.dict.index(x))
                nPos = (pos - self.shift) % len(self.dict)
                self.decoded += self.dict[nPos]
            elif direction == 'left':
                pos = (self.dict.index(x))
                nPos = (pos + self.shift) % len(self.dict)
                self.decoded += self.dict[nPos]
            elif x not in self.dict:
                self.decoded += x
        print(self.decoded)
        return self.decoded
    
    def write_results(self):
        if self.option == "encode":
            f = open("encoded.txt", 'w+')
            f.write("Twoja zakodowana wersja to: " + self.encoded)
            f.close()
        if self.option == "decoded":
            f = open("decoded.txt", 'w+')
            f.write("Twoja odkodowana wersja to: " + self.decoded)
            f.close()  

def main():
     alph = myDict()
     
     while True:
         print("Wybierz opcje 1. encoded - zakodowanie 2. decoded zaszyfrowanie")
         choice = input()
         if choice == 'encoded':
             obj.CaesarCypher(alph,3)
             obj.input()
             obj.encode()
             obj.write_results
             print("czy chciałbyś zakończyć  ? tak/nie")
             choice = input2 
             if()

    # obj.input()
    # obj.encode()
    # obj.decode('left')



    

if __name__ == "__main__":
    main()
    

        
