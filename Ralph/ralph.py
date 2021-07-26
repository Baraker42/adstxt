import urllib.request
import os
from tkinter import *

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
    for i in ourlist:
        if i not in clientlist:
            newads.append(i)
            file= open("ads.txt", "a")
            file.write(i)
        else:
            continue
    try:
        file.close()
    except:
        all_rigth = Label(root, fg="green", text="Na webu jsou všechna potřebná ads.txt" )
        all_rigth.grid(row=4, column=0)


def wiggum(i):
    print(i)
    global clientlist
    client_ads = urllib.request.urlopen(i)
    clientlist = transcript(client_ads)
    our_ads = urllib.request.urlopen("https://cdn.performax.cz/yi/ads-txt/px-uni-ads.txt")

    #provede přepis z url do listu
    global ourlist

    ourlist = transcript(our_ads)



    try:

        with open("ads.txt") as f:
            lines=f.readlines()
        os.remove("ads.txt")
        check_ads()
    except FileNotFoundError:
        check_ads()

    done_info.grid(row=4,column=0)



#zkontroluje jestli existuje ads.txt soubor, pokud ano vymaže ho a vytvoří nový, aby nedocházelo k přepisování



root =Tk()
root.title("Ralph")
root.tk.call('wm', 'iconphoto', root._w,PhotoImage(file='ralph.png'))
entry=Label(root,text="Vložte klientské url s ads.txt")
url_entry=Entry(root,width=50,borderwidth=5)
url_button=Button(root, text="Vložit", command=lambda:wiggum(url_entry.get()))
#global done_info
done_info=Label(root,fg="black", text="Hotovo!",font=("bold"))


entry.grid(row=1,column=0, columnspan=2)
url_entry.grid(row=3, column=0)
url_button.grid(row=3, column=1)
root.mainloop()