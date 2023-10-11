import math

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

determinan = b**2 - 4*a*c

if determinan > 0:
    jenis_akar = "Akar berbeda"
    x1 = (-b + math.sqrt(determinan)) / (2*a)
    x2 = (-b - math.sqrt(determinan)) / (2*a)
    
elif determinan == 0:
    jenis_akar = "Akar kembar"
    x = -b / (2*a)
  
else:
    jenis_akar = "Akar imajiner"
    x1 = f"-{b} + √{-determinan} / 2*{a}"
    x2 = f"-{b} - √{-determinan} / 2*{a}"

print("\nPersamaan kuadrat:", f"{a}x² + {b}x + {c}")
print("Determinan:", determinan)
print("Merupakan akar", jenis_akar)

if determinan > 0:
    print(f"Akar x1 = {x1}")
    print(f"Akar x2 = {x2}")
elif determinan == 0:
    print(f"Akar = {x}")
else:
    print(f"Akar x1 = {x1}")
    print(f"Akar x2 = {x2}")