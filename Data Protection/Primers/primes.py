# import numpy
import math  
  
def slowPrime(a,b ):


    print("Pierwsze pomiedzy ",a,"a",b,"sa:")

    for num in range(a,b + 1):

        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num)
    # for num in range(a,b+1):
    #     if num > 1:
    #         for i in range (2,num):
    #             if math.sqrt(num) % i ==0:
    #                 break
    #             else:
    #                 print(num)




#slowPrime(100,5000)

def primers(a,b):
    for num in range(a,b + 1):

        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                return num

def isPrime(num,rng):
    x = math.sqrt(num)
    for _ in range(rng):
        if x % _ == 0:
            print("tak")
        else:
            print("nie")

def betterPrime(a,b):
    for x in range(a,b):
        print(x,isPrime(x,b))


betterPrime(5000,10000)

# dwa dla do drugiej -1 