## Pro správnou funkčnost je třeba mít nainstalovaný python https://www.python.org/
## Jedná se o testovací verzi, radši trochu kontrolovat, že je to v pořádku. 
## Stáhni si zip soubor pomocí zeleného tlačítka Code
### Ze stránky, kterou chceš porovnat, si překopíruješ aktuální ads.txt do souboru klient.txt
### Nepřejmenovávat txt soubory jinak to nebude fungovat
### Hlídat si, že nase.txt obsahuje aktuální ads.txt
### Po spuštění ads.py / upgrade.py se vytvoří nový soubor ads.txt, který obsahuje pouze řádky, které na stránce chybí
#### Nápady a bugy hlásit prosím :-)

V repozitáři se nachází 3 verze programu:<br>
  -ads.py, která vyžaduje přítomnost souborů nase.txt a klient.txt<br>
  -upgrade.py, která si nase.txt nahraje z aktuálního souboru pomocí url<br>
  -Ralph.py, který po spuštění vyvolá konzoli, do které se zadá adresa s klientskými ads a Ralph se o vše postará(je potřeba mít nainstalovaný Tkinter<br>
  <br>
  (Ralph.exe má svůj vlastní repozitář(https://github.com/Baraker42/Ralph)
