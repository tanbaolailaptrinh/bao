def extended_euclidean(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = extended_euclidean(b, a % b)
        return (gcd, y, x - (a // b) * y)

def mod_inv(a, m):
    gcd, x, y = extended_euclidean(a, m)
    if gcd != 1:
        return None
    else:
        return x % m
print(mod_inv(2,8))
print(mod_inv(3,7))
print(mod_inv(7,3))