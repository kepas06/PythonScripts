# -*- coding: utf-8 -*-
from collections import Counter
from decimal import *
import os


class VigenereCipher():

    def __init__(self, myDict):   
        self.dict = myDict
        self.dataContainer = []
        self.cipher_text = []
        self.decoded_cipher = []
        self.cipher_text_coded = ''


    def input(self, choice):

        """ Wprowadzanie pliku do zakodowania """

        file = open(choice)
        with file as file_handle:
            for line in file_handle:
                self.dataContainer += line.upper()
        file.close()


    def encode(self,key):

        """ Szyfrowanie danych  """

        key_val = [] 
        counter = 0
 
        key_val = [self.dict.index(x.upper()) if x.upper() in self.dict else x for x in key ]
        text_val = [self.dict.index(x) if x in self.dict else x for x in self.dataContainer    ]
   
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

    def decode(self, key):

        """ Odkodowywanie Danych  """

        key_val = [self.dict.index(x.upper()) for x in key if x.upper() in self.dict]
        text_val = [self.dict.index(x) if x in self.dict else x for x in self.cipher_text_coded ]
        
        counter = 0
        for x in text_val:
            if counter == len(key_val):
                counter = 0
            if isinstance(x,str):
                x_val = x
                self.decoded_cipher.append(x_val)
            else:
                self.decoded_cipher.append(((x - key_val[counter])) % 27 )
                
            
            counter += 1

        self.decoded_cipher_values = [ self.dict[x] if isinstance(x, int) else x  for x in  self.decoded_cipher]

        f = open("decoded.txt", 'w')
        f.write(''.join(self.decoded_cipher_values))
        f.close()
        return self.decoded_cipher_values

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
    def frequency(self):

        " Znajdywanie częstotliwosci występowania danych liter "

        most = self.mostCommon(self.dataContainer)
        s = sum(x[1] for x in most)
        mostCommonByAll = [(x[0], self.fine_division(x[1], s)) for x in most]

        print(mostCommonByAll)
        return(mostCommonByAll)



    def fine_division(self, n, s):
        return round((Decimal(n) / Decimal(s)) * Decimal(100), 4)



    