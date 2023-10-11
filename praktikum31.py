a = float(input("panjang sisi a: "))
b = float(input("panjang sisi b: "))
c = float(input("panjang sisi c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Jenis segitiga: Segitiga sama sisi")
    elif a == b or a == c or b == c:
        print("Jenis segitiga: Segitiga sama kaki")
    elif a**2 + b**2 == c**2 or c**2 - a**2 == b**2 or + c**2 - a**2 == a**2:
        print("Jenis segitiga: Segitiga siku-siku")
    else:
        print("Jenis segitiga: Segitiga sembarang")
else:
    print("Tidak membentuk segitiga")