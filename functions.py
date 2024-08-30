def modulo(a, m):
    """An operation that divides a by m and returns the remainder of it. (%)"""
    #print(f"{a} mod {m}:")
    return a % m 

def congruence(a,m, b):
    """A function to verify if a and b are congruent modulo m. b can be given or not. All the relations are
    printed."""
    
    if b == None:
        b = modulo(a,m)
        print(b)
        print()

    else:
        b = b

    congruence_check = (a-b) % m
    if congruence_check == 0:
        congruents = True

        print(f"{a} ≡ {b} (mod {m})")
        k = (a-b)/m
        print(f"{a} - {b} = {k}*{m}")
        print(f"{a} = {k}*{m} + {b}")
        print()
        r1 = modulo(a,m)
        p = (a-r1)/m
        print(f"{a} = {p}*{m} + {r1}")
        r2 = modulo(b,m)
        q = (b-r2)/m
        print(f"{b} = {q}*{m} + {r2}")
        print(f"p = {p}")
        print(f"q = {q}")
        print(f"r1 = {r1}")
        print(f"r2 = {r2}")
        k = p - q
        print(f"k = {k}")


    else:
        congruents = False
        print("a and b are not congruent modulus m! You need to review the value given to b")

    return congruents