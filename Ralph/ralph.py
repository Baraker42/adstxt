import urllib.request
import os
from tkinter import *

#funkce pro přepis z bytes do utf-8
def transcript(line):
    newlist=[]
    for i in line:
        if isinstance(i, bytes):
            i=i.decode('utf-8')

        #tady dochází ke sjednocení řádků, aby mohlo docházet ke správnému porovnání
        if "#" not in i:
            if "\n" not in i:
                i=i+"\n"
            #při určitém řádkování se objeví \r\r na konci řádku a nemůže dojít k jeho správnému porovnání, tato část skriptu to řeší
            if "\r" in i:
                i=i.replace("\r\r","")
            i=i.replace(" ","")
            newlist.append(i)

    return newlist

#nová featura která kontroluje, zda na stránce nejsou duplicitní ads.txt
def duplicity_test(newlist):
    dubble_list=[]
    for i in newlist:
        counter=(newlist.count(i))
        if counter > 1 and i not in dubble_list and i != "\n":
            note=(str(counter)+"x"+" " + i)
            dubble_list.append(i)
            file=open(duplicity,"a")
            file.write(note)


    return dubble_list

#funkce pro porovnání ads.txt souborů
def check_ads():
    newads=[]
    for i in ourlist:

        if i not in clientlist and i != "\n":
            i=i.replace(",",", ")
            newads.append(i)
            file= open(ads, "a")
            file.write(i)
        else:
            continue
    
    try:
        file.close()
    except:
        all_rigth = Label(root, fg="green", text="Na webu jsou všechna potřebná ads.txt" )
        all_rigth.grid(row=4, column=0)

#funkce připraví text, který slouží k pojmenování souboru, aby byl větší pořádek v souboru, kde se používá a nedocházelo zbytečně k přepisování
def make_client_tag(i):
    client_url = i.split("/")
    checkbox=["http:","ads.txt","www","https:","ads","txt"]
    for i in client_url:
        if i not in checkbox and len(i) > 4:
            client_tag=i.replace(".","")
    return client_tag

#hlavní funkce Ralpha, ze které se volá všechno ostatní
def wiggum(i):
    print (i)
    global clientlist

    #tato část skriptu výrazně zjednodušuje vyhledávání, protože stačí napsat čast adresy bez https a ads.txt
    try:
        client_ads = urllib.request.urlopen(i)
    except ValueError:
        make_url="https://"+i+"/ads.txt"
    try:
        client_ads = urllib.request.urlopen(make_url)
    except:
        no_https="http://"+i+"/ads.txt"
        client_ads = urllib.request.urlopen(no_https)

    #volá funkce, které přepíšou klientské url do listu a připraví text pro pojmenování souboru
    clientlist = transcript(client_ads)
    
    client_tag = make_client_tag(i)

    #připraví tagy pro ads.txt a duplicitu
    global ads
    global duplicity
    ads = client_tag+".txt"
    duplicity = client_tag +"_duplicity.txt"

    #provede přepis z url do listu pro naše ads.txt
    our_ads = urllib.request.urlopen("https://cdn.performax.cz/yi/ads-txt/px-uni-ads.txt")
    global ourlist
    ourlist = transcript(our_ads)
    
#vytvoří txt, které obsahuje ads.txt, které má klient na svém webu vícekrát a pokud už nějaký existuje, tak ho vymaže
    try:
        with open(duplicity) as f:
            lines=f.readlines()
        os.remove(duplicity)
        duplicity_test(clientlist)
    except FileNotFoundError:
        duplicity_test(clientlist)


#vytvoří txt s ads.txt které klientovi na webu chybí a pokud už nějaký existuje, tak ho vymaže
    try:
        with open(ads) as f:
            lines=f.readlines()
        os.remove(ads)
        check_ads()
    except FileNotFoundError:
        check_ads()

    done_info.grid(row=4,column=0)

    print("Díky za spolupráci")






#základní uživatelské rozhraní Ralpha
root =Tk()
root.title("Ralph")
root.tk.call('wm', 'iconphoto', root._w,PhotoImage(file='ralph.png'))
entry=Label(root,text="Vložte klientské url s ads.txt nebo pouze základní stránku")
url_entry=Entry(root,width=50,borderwidth=5)
url_button=Button(root, text="Vložit", command=lambda:wiggum(url_entry.get()))
#global done_info
done_info=Label(root,fg="black", text="Hotovo!",font=("bold"))


entry.grid(row=1,column=0, columnspan=2)
url_entry.grid(row=3, column=0)
url_button.grid(row=3, column=1)
root.mainloop()