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

def calkey(keysize):
    p = 373
    q = 211
    e = 257
    n = p*q
    mylcm = lcm(p-1,q-1)
    print("i am lcm:" , mylcm)
    gcd,x,y  = egcd(e, mylcm)
    print("i am y:", y)
    print("i am x:", x)
    d = int(x)
    print("i am d:", d)
    return n,e,d


def modularExponentiation(i, n, m):
    j = 1
    if n < 0:
        i = 1 / i
        n = -n
    if n == 0:
        return 1
    while n > 1:
        if n % 2 == 0:
            i = (i * i) % m
            n = n / 2
        else:
            j = (i * j) % m
            i = (i * i) % m
            n = (n-1) / 2
    return (i * j) % m


def cipher(n,e,message):
    cipherText = modularExponentiation(message, e, n)
    return cipherText

def plain(n,d, cipher):
    plainText = modularExponentiation(cipher, d, n)
    return plainText


if __name__ == '__main__':
    size = int(input("Please enter the size of the key you want"))
    n,e,d = calkey(size)
    print("The private key is: (" + str(n) + "," + str(e) + "," + str(int(d)) + ")")
    print("The public key is: (" + str(n) + "," + str(e) + ")")
    message = int(input("Please enter the message you want to encript"))
    print("The original message is:", message)
    cipherMessage = cipher(int(n),int(e),message)
    print("The cipher message is :" ,cipherMessage )
    print("The message is : ", plain(int(n),int(d),cipherMessage)) 
    print("i")