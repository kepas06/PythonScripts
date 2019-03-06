from collections import Counter

def mostCommon(text):
    lst = (Counter(text))
    lst1 = []
    for x in lst:
        if lst[x] >= 2:
            lst1.append((x,lst[x]))

    lst2 = sorted(lst1, key = lambda x:x[1],reverse=True)
    print(lst2)



if __name__ == '__main__':
    mostCommon("znowu w zyciu mi nie wyszlo, aaa bbb ccc, aaaaa ")