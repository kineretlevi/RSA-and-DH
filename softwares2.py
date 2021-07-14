
# Recursive function to return gcd of a and b
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

# Common divisor according to the extended Euclidus algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x

# Function to return LCM of two numbers
def lcm(a,b):
    return (a / gcd(a,b))* b

# Function that calculates Euler's Totient
def euiler(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result

#Function that check if the number is prime
def checkPrime(num):
    if (num == 2):
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+2,2):
        if (num % i == 0):
            return False
    return True

# Function that calculates the keys of RSA
def calkey(p,q):
    e = 65537
    mylcm = int(lcm(p-1,q-1))
    phlcm = euiler(mylcm)
    if gcd(phlcm, e) != 1:
        print("Error in calculating keys")
    else:
        
        gcd1,x,y  = egcd(e, phlcm)
        # print("i am y:", y)
        # print("i am x:", x)
        d = int(x)
        
    return e,d


def modularExponentiation(i, n, base):
    j = 1
    if n < 0:
        i = 1 / i
        n = -n
    if n == 0:
        return 1
    while n > 1:
        if n % 2 == 0:
            i = (i * i) % base
            n = n / 2
        else:
            j = (i * j) % base
            i = (i * i) % base
            n = (n-1) / 2
    return (i * j) % base


def cipher(message, e, n):
    cipherText = modularExponentiation(message, e, n)
    return cipherText

def plain(cipher, d, n):
    plainText = modularExponentiation(cipher, d, n)
    return plainText

################ Second qestion ##############
def miller_rabin(n, k):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = rand(2, n - 1)
        
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

### random
def rand(min,max):
    A = min; # any number in (0, RAND_MAX)
    C = max; # any number in [0, RAND_MAX)
    RAND_MAX = 100000

    prev = 0; #seed. any number in [0, RAND_MAX)
    prev = ( prev * A + C ) % RAND_MAX
    return int(prev)



def prime():
    a = 2
    n = int(input("Please enter the amount of bit size you want: "))
    k = int(input("Please enter the amount of rounds you want: "))
    while (k == 0):
        k = int(input("Wrong amount of rounds please enter again: "))
    
    pnum = 2**n - 1
    if pnum == 1:
        return pnum
    while miller_rabin(pnum,k) == False:
            pnum = pnum - 2
    return pnum,a,n,k

def generatingKeys(p,a,n,k):
    Akey = int(input("Please enter the public key you want for Alice: "))   #Alice secret number
    Bkey = int(input("Please enter the public key you want for Bob: "))     #Bob secret number
    while Akey > n | miller_rabin(Akey,k) == False | Bkey > n | miller_rabin(Bkey,k) == False:
        Akey = int(input("Wrong number, please enter again secret key for Alice: "))
        Bkey = int(input("Wrong number, please enter again secret key for Bob: "))
    
    generatedkA = int(pow(a,Akey,p))   #Alice public key
    generatedkB = int(pow(a,Bkey,p))   #Bob public key

    print("Alice public key : ", Akey)
    print("Bob public key : ", Bkey)

    secretK = int(pow(Bkey,Akey,p))
    return secretK



if __name__ == '__main__':
    print("**********First Question**********")
    size = 4
    p = 31
    q = 37
    n = p*q
    count=0
    e,d = calkey(p, q)
    print("The private key is: (" + str(n) + "," + str(e) + "," + str(int(d)) + ")")
    print("The public key is: (" + str(n) + "," + str(e) + ")")
    message = 37
    print("The original message is:", message)
    cipherMessage = cipher(message, int(e), int(n))
    print("The cipher message is :" ,cipherMessage )
    print("The message is : ", plain(cipherMessage, int(d),int(n))) 
    print("**********Second Question**********")
    p,a,n,k = prime()
    secret = generatingKeys(p,a,n,k)
    print("The generating secret key is: ", secret)
  