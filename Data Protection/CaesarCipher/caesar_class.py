# -*- coding: utf-8 -*-
from collections import Counter
from decimal import *
import os


class CaesarCypher():

    def __init__(self, myDict):   
        self.dict = myDict
        self.dataContainer = []
        self.patternContainer = []
        self.encoded = ""
        self.decoded = ""
        self.possibleKey = 0

    def input(self, choice):

        """ Wprowadzanie pliku do zakodowania """

        file = open(choice)
        num_of_char = os.stat(choice).st_size

        if num_of_char > 1000:
            with file as file_handle:
                for line in file_handle:
                    self.dataContainer += line.upper()
            file.close()
        else:
            print("plik jest zbyt maly")

    def input_pattern(self, choice):

        """ Wprowadzanie pliku wzorcowego dla dekodowanego pliku """

        file = open(choice)
        num_of_char = os.stat(choice).st_size

        if num_of_char > 10000:
            with file as file_handle:
                for line in file_handle:
                    self.patternContainer += line.upper()
            file.close()
        else:
            print("plik jest zbyt maly jako wzorzec ")

    def encode(self, shift):

        """ Szyfrowanie danych  """

        for x in self.dataContainer: 
            if x in self.dict:   
                pos = self.dict.index(x)
                nPos = (pos + shift) % len(self.dict)
                self.encoded += self.dict[nPos]
            else:
                self.encoded += x

        f = open("encoded.txt", 'w')
        f.write(self.encoded)
        f.close()
        return self.encoded

    def decode(self, direction, shift):

        """ Odkodowywanie Danych  """

        if self.possibleKey != 0:
            shift = self.possibleKey

        for x in self.dataContainer:
            if direction == 'right':
                if x not in self.dict:
                    self.decoded += x
                else:
                    pos = self.dict.index(x)
                    nPos = (pos - shift) % len(self.dict)
                    self.decoded += self.dict[nPos]
            elif direction == 'left':
                if x not in self.dict:
                    self.decoded += x
                else:
                    pos = (self.dict.index(x))
                    nPos = (pos + shift) % len(self.dict)
                    self.decoded += self.dict[nPos]

        f = open("decoded.txt", 'w')
        f.write(self.decoded)
        f.close()
        return self.decoded

    def mostCommon(self, text):

        """ Znajdywanie najczęściej występujących znakow """

        lst = Counter(text)
        d = {}
        for key, value in lst.items():
            d[key] = value

        sort_val = sorted(d.items(), key=lambda kv: kv[1], reverse = True)
        return sort_val

    def fine_division(self, n, s):
        return round((Decimal(n) / Decimal(s)) * Decimal(100), 4)

    def comparsion(self, alph):

        """ Znajdowanie podobienst w wystepowaniu poszczegolnych 
            liter we wzorcu i dekodowanym pliku.Jezeli dana litera
            wystepowała najczesciej, jest prawdopodobnym 
            ( o ile mamy odpowiedni wzorzec ) obliczenie klucza przesuniecia
            dla gdy porownamy najczesciej wystepujace znaki w tekscie  """

        patMComm = self.mostCommon(self.patternContainer)
        cipMComm = self.mostCommon(self.dataContainer)

        s = sum(x[1] for x in patMComm)
        s2 = sum(x[1] for x in cipMComm)

        patMComm = [(x[0], self.fine_division(x[1], s)) for x in patMComm]
        cipMComm = [(x[0], self.fine_division(x[1], s2)) for x in cipMComm]

        n1 = 0
        n2 = 0
        counter = 0

        print(patMComm)
        print("")
        print(cipMComm)

        for x in alph:
            if x == patMComm[0][0]:
                n1 = alph.index(x)
            elif x == cipMComm[0][0]:
                n2 = alph.index(x)

        for x in range(n1, len(alph)):
            if x == n2:
                self.possibleKey = x
            counter += 1

        if self.possibleKey == 0:
            for x in alph:
                if alph.index(x) == n2:
                    self.possibleKey = counter     
                    break
                counter += 1
        else:
            return self.possibleKey

        print("")
        print(" mozliwy klucz to: " + str(self.possibleKey))
        return self.possibleKey
