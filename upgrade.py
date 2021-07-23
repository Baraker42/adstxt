#import potřebných modulů
import urllib.request
import os

#definice funkcí
#funkce pro přepis ads.txt nebo url do listu
def transcript(line):
    newlist=[]
    for i in line:
        if isinstance(i, bytes):
            i=i.decode('utf-8')
        if "#" not in i:
                newlist.append(i)
    return newlist

#funkce pro porovnání ads.txt souborů
def check_ads():
    newads=[]
    for i in newlist:
        if i not in secondlist:
            newads.append(i)
            file= open("ads.txt", "a")
            file.write(i)

    file.close()

#načte url
response = urllib.request.urlopen("https://cdn.performax.cz/yi/ads-txt/px-uni-ads.txt")


#načte textový soubor s klientskými ads
with open("klient.txt") as f:
    lines=f.readlines()

#provede přepis z url do listu
newlist = transcript(response)

#provede přepis z klient.txt do listu
secondlist = transcript(lines)

#zkontroluje jestli existuje ads.txt soubor, pokud ano vymaže ho a vytvoří nový, aby nedocházelo k přepisování
try:
    with open("ads.txt") as f:
        lines=f.readlines()
    os.remove("ads.txt")
    check_ads()
except FileNotFoundError:
    check_ads()

