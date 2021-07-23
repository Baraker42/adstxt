import os

#funkce pro přepsání textového dokumentu do listu
def transcript(txt):
    with open(txt) as f:
        lines=f.readlines()
    newlist=[]
    for i in lines:
        if "#" not in i:
            newlist.append(i)
    return newlist

#porovná ads.txt ze stránky s našimi a vytvoří nový soubor s ads, které na stránce chybí
def check_ads():
    newads=[]
    for i in firstads:
        if i not in secondads:
            newads.append(i)
            file= open("ads.txt", "a")
            file.write(i)

    file.close()

#vytvoří list s našemi ads.txt
firstads=transcript("nase.txt")
#vytvoří lsit s klientskými ads.txt
secondads=transcript("klient.txt")



#zkontroluje jestli existuje ads.txt soubor, pokud ano vymaže ho a vytvoří nový
try:
    with open("ads.txt") as f:
        lines=f.readlines()
    os.remove("ads.txt")
    check_ads()

except FileNotFoundError:
    check_ads()


