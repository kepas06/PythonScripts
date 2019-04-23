# def mod_fast(a, b, n):
#     x=1
#     lst =[]
#     while x<=b: 
#         lst.append(x)
#         x=x*2
    
#     lst2 = []
#     for x in lst:
        
def mod_simple(a, b, n):
    r = 1
    for x in range(b):
        #print(x)
        #print(r)
        r = r * a % n

        # print(result)
        # print("")

    return n


# def diff_helman1(p, g, a):
   
#     A = mod_simple(g, a, p)
#     print(A)


# def diff_helman(p, g, a, B):
   
#     A = mod_simple(g, a, p)

#     Ka = mod_simple(B, a, p)

#     print(A, Ka)



def hellman()
#man in the middle
#ewa nie pozwala ustalic wspolnego klucza ylko przechywtujac kawałek klucza Alicji i Boba zmieniajac efektywnie ewa nzwiązuje klucz z Aalicją i z Bobem

# diff_helman1(1229, 1543, 5,10)
# diff_helman1(1229, 1543, 5)
    # Ka = mod_simple(B,a,p),
    # Kb = mod_simple(A,b)




#protokol diffiego helmana

#potrzebujemy alicja B
#4cyfrowe liczby 
#screenshot