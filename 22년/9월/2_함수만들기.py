def add(a,b,c):
    return a+b+c

def isPrime(x):
    for i in range(2, x//2 + 1):
        if x%i==0:
            return False
    else : return True
    
a, b, c = 1, 2, 4

print(add(a,b,c))




print(isPrime(21))
a=[12,13,7,9,19]
for y in a:
    if isPrime(y):
        print(y, end=' ')