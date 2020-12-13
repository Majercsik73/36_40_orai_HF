# 0. feladat
import random
print("A 13.e osztály tanulóinak hiányzásai: ")
print()
hy = []
def hianyzas(hy):
    for i in range(0,31):
        hy.append(random.randint(0,201))
    return hy
print(hianyzas(hy))
print()
