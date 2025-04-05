# product of prime number number at xth and yth position and substact 1 from it.


# x, y = map(input().split(), lambda x: int(x)) ? wrong way

inp = input()

x , y = (inp.split())
x = int(x)
y = int(y)
print(x ,y, type(x),type(y))

def nthPrimeNumber(n):
    prime = []
    start = 2
    while len(prime) < n:
        if isPrime(start):
            prime.append(start)
        start +=1
    print("All prime", prime)    
    return prime[len(prime)-1]

def isPrime(num):
    if num < 2:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
    return True               
        
xth = nthPrimeNumber(x)
yth = nthPrimeNumber(y)
print("xth = ", xth , "yth =", yth)
print("Answer :", (xth * yth) -1 ) 