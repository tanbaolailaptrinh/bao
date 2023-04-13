a = 25
b = 45
#This is a way to find gcd normal
def gcd(a, b):
    if a == b:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(b, a - b)

#This is a way to find gcd with euclidean
print(gcd(a, b))


def gcd_el(a, b):
    if b == 0:
        return a

    else:
        return gcd_el(b, a % b)


print(gcd_el(a, b))














