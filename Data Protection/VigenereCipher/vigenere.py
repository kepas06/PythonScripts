# -*- coding: utf-8 -*-
from collections import Counter
from decimal import *
import os


class VigenereCipher():

    def __init__(self, myDict):   
        self.dict = myDict
        self.cipher_text = []
        self.decoded_cipher = []
        self.cipher_text_coded = ''
        self.to_decode = []


    def input(self, choice, container):

        """ Wprowadzanie pliku do zakodowania """

        file = open(choice)
        with file as file_handle:
            for line in file_handle:
                container += line.upper()
        file.close()

    def encode(self,key, container):

        """ Szyfrowanie danych  """

        key_val = [] 
        counter = 0
 
        key_val = [self.dict.index(x.upper()) if x.upper() in self.dict else x for x in key ]
        text_val = [self.dict.index(x) if x in self.dict else x for x in container  ]
   
        for x in text_val:
            if counter == len(key_val):
                counter = 0
            if isinstance(x,str):
                x_val = x
                self.cipher_text.append(x_val)
            else:
                x_val = (key_val[counter] + x) % 27
                self.cipher_text.append(x_val)
            counter+=1

        self.cipher_text_coded = [ self.dict[x] if isinstance(x,int) else x  for x in self.cipher_text]
        
        f = open("encoded.txt", 'w')
        f.write(''.join(self.cipher_text_coded))
        f.close()
        return self.cipher_text_coded

    def decode(self, key, container):

        """ Odkodowywanie Danych  """
        
        key_val = [self.dict.index(x.upper()) for x in key if x.upper() in self.dict]
        text_val = [self.dict.index(x) if x in self.dict else x for x in container ]

        counter = 0

        for x in text_val:
            if counter == len(key_val):
                counter = 0
            if isinstance(x,str):
                self.decoded_cipher.append(x)
                counter -= 1
            elif isinstance(x,int):
                self.decoded_cipher.append(((x - key_val[counter] )) % 27 )
             
            counter += 1

        self.decoded_cipher_values = [ self.dict[x] if isinstance(x, int) else x for x in  self.decoded_cipher]


        
        f = open("decoded.txt", 'w')
        f.write(''.join(self.decoded_cipher_values))
        f.close()
        return self.decoded_cipher_values


    def friedman_method(self, containerPattern, containerCipher ):
        container_pattern = [x for x in containerPattern if x in self.dict ]
        container_cipher = [x for x in containerCipher if x in self.dict ]
  

        commonPat = self.mostCommon(container_pattern)

        sumUp = float(sum([ x[1]*(x[1]-1) for x in commonPat]))
        sumDown = float(sum([x[1] for x in commonPat]) *( sum([x[1] for x in commonPat]) - 1))

        icPattern = float(sumUp/sumDown)

        lst = []
        lstOfIc = []

        cipher_string = ''.join(container_cipher)

          
        for x in range(2,20):
            h = x
            tables = [[ x for x in cipher_string[i::h]] for i in range(h)]
            lst.append(tables)
        

        avg = 0
        for x in lst:
            for y in x:
                avg += self.indexOfCoincidence(y)
                
            elem = [len(x),(avg/len(x))]
            lstOfIc.append(elem)
            avg = 0
        
        print(icPattern)
        print(lstOfIc)



    def indexOfCoincidence(self,text):

        lst = self.mostCommon(text)
        nominator = float(sum([ x[1]*(x[1]-1) for x in lst]))
        denominator = float(sum([x[1] for x in lst]) * ( sum([x[1] for x in lst]) -1 ))
        result = float(nominator/denominator)
        return result
    


    def mostCommon(self, text):

        """ Znajdywanie najczęściej występujących znakow """

        if isinstance(text,list):
            text = ''.join(text)

        lst = Counter(text)
        d = {}
        for key, value in lst.items():
            d[key] = value

        sort_val = sorted(d.items(), key=lambda kv: kv[1], reverse = True)
        
        return sort_val

        
    def frequency(self,container):

        " Znajdywanie częstotliwosci występowania danych liter "

        most = self.mostCommon(container)
        s = sum(x[1] for x in most)
        mostCommonByAll = [(x[0], self.fine_division(x[1], s)) for x in most]

        print(mostCommonByAll)
        return(mostCommonByAll)



    def fine_division(self, n, s):
        return round((Decimal(n) / Decimal(s)) * Decimal(100), 4)



    