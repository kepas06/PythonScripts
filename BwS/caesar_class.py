class CaesarCypher():

    dataContainer = []
    encoded = ""
    decoded = ""

    def __init__(self, myDict, shift, option):
        self.shift = shift
        self.dict = myDict
        self.option = option

    def input(self):
        print("Odczytaj Plik")   
        choice = str(input())
        file = open(choice)
        with file as file_handle:
            for line in file_handle:
                self.dataContainer += line.upper()
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

    def decode(self, direction):
        for x in self.dataContainer:
            if direction == 'right':
                if x not in self.dict:
                    self.decoded += x
                else:
                    pos = (self.dict.index(x))
                    nPos = (pos - self.shift) % len(self.dict)
                    self.decoded += self.dict[nPos]
            elif direction == 'left':
                if x not in self.dict:
                    self.decoded += x
                else:
                    pos = (self.dict.index(x))
                    nPos = (pos + self.shift) % len(self.dict)
                    self.decoded += self.dict[nPos]

        print(self.decoded)
        return self.decoded

    def write_results(self):
        if self.option == "encode":
            f = open("encoded.txt", 'w')
            f.write("Twoja zakodowana wersja to: " + self.encoded)
            f.close()
        if self.option == "decode":
            f = open("decoded.txt", 'w')
            f.write("Twoja odkodowana wersja to: " + self.decoded)
            f.close()  