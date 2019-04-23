import time


def is_prime(n):
    if n < 2: 
        
        return False
    if n % 2 == 0:             
        return n == 2  # return False
    k = 3
    
    while k*k <= n:
        if n % k == 0:
            return False
        k += 2
    return True


# Test the above function
counter = 0
start = time.time()


for x in range(20000000, 21000000):
    if is_prime(x):
        counter += 1

print(counter)
end = time.time()
print(end - start)



# for x in range(200000000000, 200000000100):
#     if is_prime(x):
#         print(x)
#         counter += 1

# print(counter)
    
