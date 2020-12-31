# 0. feladat
import random
print("A 13.e osztály tanulóinak hiányzásai: ")
print()
hy = []
def hianyzas(hy):
    for i in range(0,60):
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
print(atlag(hiany))

if len(atlag(hiany)) >= 1:
    print(str(atlag(hiany)) + " sorszámú diák(ok)nak volt az átlag hiányzással megegyező hiányzása!")
else:
    print("Nem volt olyan diák, akinek a hiányzása az átlaggal lenne egyenlő!")



diak = 0
def atlagdiak(diak):
    for i in range(0,len(hy)):
        if (hy[i] >= atlaghy(atlag)-30) or (hy[i] <= atlaghy(atlag)+30):
#        if hy[i] == atlaghy(atlag):
            diak = i+1
            break
    return (diak)
if diak == 0:
    print(" ")
else:
    print("A " + str(atlagdiak(diak)) + " -dik számú diáknak volt az átlag hiányzással megegyező hiányzása!")
print()


diak = 0
for i in range(0,len(hy)):
    if hy[i] == atlaghy(atlag):
        diak = i+1
print("A " + str(diak) + "-dik diáknak volt átlag körüli a hiányzása!")
print()

#pont = 0
#melyik = []
#for i in range(0,31):
#    if (hy[i] >= atlag-30) or (hy[i] <= atlag+30):
#            pont = hy[i]
#print(pont)
#print(melyik)


# 4. feladat 
