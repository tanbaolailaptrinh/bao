import random
from sympy import isprime
from cryptography.fernet import Fernet
import time

#RSA
#generate prime number
start_time = time.perf_counter()
def generate_prime_number(n_bits):
    while True: # this function uses a while True loop to repeatedly generate prime numbers until finding a prime number that meets the requirement
        p = random.randint(2**(n_bits-1), 2**n_bits-1) #the function uses the random.randint function to generate an integer p within the range from $2^{n_bits-1}$ to $2^{n_bits}-1$ (including both endpoints).
        if isprime(p): #the function checks whether the generated number p is a prime number or not using the isprime function from the sympy library
            return p #If p is a prime number, the function returns that number using the return statement
p = generate_prime_number(1115) 
print(p)
q = generate_prime_number(1025)
n = p * q
totient = (p-1) * (q-1)
e = 65537
d = pow(e, -1,totient) #d = e ^ - 1 mod totient
message = 123456789
def rsa_encrypt(m, e, n):
    c = pow(m, e, n) #m ^ e mod n
    return c

def rsa_decrypt(c, d, n):
    m = pow(c, d, n) #c ^ d mod n
    return m

encrypted_message = rsa_encrypt(message,e,n) 
print("ecrypted_message: ", encrypted_message)
decrypted_message = rsa_decrypt(encrypted_message, d, n)
print("Decrypted message:", decrypted_message)
end_time= time.perf_counter()
elapsed_time = end_time - start_time
print(f"Time to run this program are: {elapsed_time: .4f} second")