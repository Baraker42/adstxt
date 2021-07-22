import os
#otevře náš soubor s našimi ads.txt
with open("nase.txt") as f:
    lines=f.readlines()

#uloží do nově vytvořeného listu
firstads=[]
for i in lines:
    if "#" not in i:
        firstads.append(i)

#otevře soubor ads.txt k porovnání a uloží do nového listu
with open("klient.txt") as s:
    lines2=s.readlines()

secondads=[]
for i in lines2:
    if "#" not in i:
        secondads.append(i)

#porovná ads.txt ze stránky a vytvoří nový soubor s ads, které na stránce chybí
try:
    with open("ads.txt") as f:
        lines=f.readlines()
    os.remove("ads.txt")
    counter=0
    newads=[]
    for i in firstads:
        if firstads[counter] not in secondads:
            newads.append(firstads[counter])
            file= open("ads.txt", "a")
            file.write(firstads[counter])
        counter +=1

    file.close()
except FileNotFoundError:
    counter=0
    newads=[]
    for i in firstads:
        if firstads[counter] not in secondads:
            newads.append(firstads[counter])
            file= open("ads.txt", "a")
            file.write(firstads[counter])
        counter +=1

    file.close()


