# 0. feladat
import random
print("A 13.e osztály tanulóinak hiányzásai: ")
print()
hy = []
def hianyzas(hy):
    for i in range(0,60):
        hy.append(random.randint(0,40))
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
print("A legmagasabb hiányzási óraszám az osztályban: " + str(legrosszabb(legtobb)))
print()

# 2. feladat
atlag = 0
def atlaghy(atlag):
    ossz = 0
    for i in range(0,len(hy)):
        ossz += hy[i]
        atlag = round(ossz/60)
    return atlag
print("Az osztály hiányzásainak átlagos óraszáma: " + str(atlaghy(atlag)))
print()

# 3. feladat

hiany = []
def atlag(hiany):
    for i in range(0,len(hy)):
        if hy[i] == atlaghy(atlag):
            hiany.append(i+1)
    return hiany
if len(atlag(hiany)) == 0:
    print("Nem volt olyan diák, akinek a hiányzása, az átlaggal lenne egyenlő!")
else:
    print("A következő sorszámú diák(ok)nak volt az átlag hiányzással megegyező hiányzása: " + str(atlag(hiany)))
print()

# 4. feladat 
