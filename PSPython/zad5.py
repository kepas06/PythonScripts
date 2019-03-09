import re

def phoneNum(string):
    regExpres = re.compile(r"[+]\d\d[\s]\d\d\d[\s-]\d\d\d[\s-]\d\d\d")
    find = re.findall(regExpres,string)
    print(find)

raw = open('reg5.txt')
data = raw.read()
raw.close()

if __name__ == '__main__':
    phoneNum(data)
