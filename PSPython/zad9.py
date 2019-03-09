from collections import Counter

def mostCommonTen(text):
    data = " "
    
    myfile = open(text,'a+')
    data=myfile.read().replace('\n', '')
        
    splited = data.split()
    c = (Counter(splited))
    lst = c.most_common()
    topTen=[ lst[x] for x in range(10)]
    print(topTen)
 
    myfile.write('\n'.join('%s %s' % x for x in topTen))

if __name__ == '__main__':
    mostCommonTen('zad9.txt')