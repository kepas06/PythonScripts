def sum_digits(n):
    x = sum(int(digit) for digit in str(n))
    #print(x)
    return x

dupa
def allPrimers(start,end):
    lst = [] 
    for x in range(start,end+1):
        is_prime = True
        val = sum_digits(x)
        for num in range(2,val):
            if val % num == 0:
                is_prime = False
        
        if is_prime:
            lst.append(x)

                
    print(lst) 

if __name__ == '__main__':
    allPrimers(243,743)


