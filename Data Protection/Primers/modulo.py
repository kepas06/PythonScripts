#potegowanie modulo

# x = 59**3*61**4*2*3*5*7*3*5*7
# y = x**2562142
# print(y)


# 1 liczba A mod N = ab
# B mod N = bi
# AB mod N = ?..


# A = A1*N + ab
# B = B1*N + bi
# AB = A1*B1*n2 + a1N*b + b1N*a + a*bina*B mod = (a*b ) mod N 
# 123456*78332 mod10 = 6*2 mod 10 = 2 


# funkcja of mod simple(a,b,n)

# funkcja mod fast 
# a^b mod n


def mod_simple(a, b, n):
    r = 1
    for x in range(b):
        #print(x)
        #print(r)
        r = r * a % n

        # print(result)
        # print("")

    print(r)
        

mod_imple(3, 9, 10) 

# def print_mod(a, b, n):
#     lista = mod_imple(a, b, n)

#     for x in lista:
#         print(x)


# print_mod(256, 40, 100) 
