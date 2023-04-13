#Find invers_modulo n by euclidean
def inverse_modulo(n, m): #this function have 2 parameters n and m, which represent the number and the modulus,
    a, b, x1, x2, y1, y2 = n, m, 1, 0, 0, 1 #value
    while b != 0:
        q = a // b #Quotient of divison a and b   0
        r = a % b  #remainder of divison a and b  3
        x = x1 - q * x2  
        y = y1 - q * y2  
        a, b, x1, x2, y1, y2 = b, r, x2, x, y2, y 
    if a == 1:
        return x1 % m
    else:
        return None
    # 7 = 2 * 3 + 1 --> 1 = 7 - 3 * 2 
    # 3 = 2 * 1 + 1 --> 1 = 3 - 2 * 1
    # 2 = 2 * 1 + 0 --> 0 = 2 - 2 * 0
print(inverse_modulo(2,8))
print(inverse_modulo(3,7))
print(inverse_modulo(7,3))