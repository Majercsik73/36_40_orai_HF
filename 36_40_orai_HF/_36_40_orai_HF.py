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
print("A legmagasabb hiányzási óraszám az osztályban: " + str(legrosszabb(legtobb)))
print()

# 2. feladat
atlag = 0
def atlaghy(atlag):
    ossz = 0
    for i in range(0,len(hy)):
        ossz += hy[i]
        atlag = round(ossz/31)
    return atlag
print("Az osztály hiányzásainak átlagos óraszáma: " + str(atlaghy(atlag)))
print()

# 3. feladat

#atlagalatt = 0
#for i in range (0,len(hy)):
#    if(hy[i] < atlaghy(atlag)):
#        atlagalatt += 1
#print("A hónapban " + str(atlagalatt) + " diáknál volt átlag alatti a hiányzás!")
#print()
#print()

hiany = 0
def atlag(hiany):
    elem = 0
    for i in range(0,len(hy)):
        if hy[i] == atlaghy(atlag):
            elem += 1
    return (elem)
if atlag(hiany) > 0:
    print(str(atlag(hiany)) + " diáknak volt az átlag hiányzással megegyező hiányzása!")
else:
    print("Nem volt olyan diák, akinek a hiányzása az átlaggal lenne egyenlő")
print()

diak = 0
def atlagdiak(diak):
    for i in range(0,len(hy)):
        if hy[i] == atlaghy(atlag):
            diak = i+1
    return (diak)
if atlagdiak(diak) == 0:
    print(" ")
else:
    print("A " + str(atlagdiak(diak)) + " -dik számú diáknak volt az átlag hiányzással megegyező hiányzása!")
print()


#diak = 0
#for i in range(0,len(hy)):
#    if hy[i] == atlaghy(atlag):
#        diak = i
#print("A " + str(diak+1) + "-dik diáknak volt átlag körüli a hiányzása!")
#print()

#pont = 0
#melyik = []
#for i in range(0,31):
#    if (hy[i] >= atlag-30) or (hy[i] <= atlag+30):
#            pont = hy[i]
#print(pont)
#print(melyik)


# 4. feladat 
