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

# 1. feladat
legtobb = hy[0]
def legrosszabb(legtobb):
    for i in range(0,len(hy)):
        if legtobb < hy[i]:
            legtobb = hy[i]
    return legtobb
print("A legmagasabb hiányzás az osztályban: " + str(legrosszabb(legtobb)))
print()
