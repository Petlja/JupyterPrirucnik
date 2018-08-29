# JupyterPrirucnik
Priručnik za _Jupyter_

Deo kursa računarstva i informatike (16 časova) za 8. razred osnovne škole u Srbiji koji se odnosi na vizuelizaciju i obradu podataka.

_Jupyter_ radne sveske iz ovog kursa možete pogledati kako rade na: https://mybinder.org/v2/gh/Petlja/JupyterPrirucnik.git/master

Ukoliko želite da imate sačuvane promene koje ste prethodni put uneli u radne sveske, a nemate na svom računaru instalirano okruženje za _Jupyter_, možete koristiti servis poput https://notebooks.azure.com/ . U konkretnom navedenom servisu, kada otvorite svoj nalog i ulogujete se, prilikom kreiranja nove biblioteke (opcija _New Library_) nudi vam se mogućnost da biblioteku kreirate iz _GitHub_ repozitorijuma (etiketa _From GitHub_ u prozoru koji je iskače nakon što izaberete opciju _New Library_).

## Struktura
Svaki čas je u jednoj _Jupyter_ radnoj svesci; sveske imaju imena J01, J02, ..., J16.

1. čas -- opšta priča o _Jupyter_ radnoj svesci, podsećanje na _Python_, biblioteke funkcija.

Narednih 15 časova su grupisani u pakete po tri časa. Svaki paket ima strukturu:

- 2 časa obrade gradiva (_lecture/demonstration_)
- 1 čas ponavljanje gradiva (_reflexion_)

Svaki čas obrade gradiva ima tri segmenta, za svaki od njih je planirano oko 10 minuta vremena,
tako da se jedan čas kako je ovde isplanirano može realizovati kao jedan čas realne nastave.
Naravno, ovo je potrebno izbaždariti.

Paketi:

- 2, 3. i 4. čas: kretanje kroz _Jupyter_ radnu svesku, predstavljanje nizova podataka _Python_ listama, vizuelizacija nizova podataka
linijskim i stubičastim dijagramima. Moto: "Pusti neka računar radi za tebe". Prvi korak ka obradi podataka pre vizuelizacije.

- 5, 6. i 7. čas: Linijski, stubičasti i sektorski dijagrami; najjednostavnije analize niza podataka (prosek, frekvencijska analiza).

- 8, 9. i 10. čas: Rad sa tabelarno predstavljenim podacima; biblioteka _pandas_ i struktura podataka _DataFrame_. Formiranje tabele na osnovu podataka predstavljenih listom. Rad sa kolonama i vrstama tabele. Vizuelizacija tabelarno predstavljenih podataka.

- 11, 12. i 13. čas: Dodavanje vrste i/ili kolone tabeli, iteriranje po vrstama i kolonama tabele, učitavanje tabela iz lokalnih datoteka i iz udaljenih resursa.

- 14, 15. i 16. čas: Sortiranje i filtriranje podataka, frekvencijska analiza podataka. _Jupyter_ i _Excel_

## Instalacija

Sa sajta anaconda.com iz odeljka [Downloads](https://www.anaconda.com/download/) preuzmite distribuciju Anakonde za vašu platformu (Windows, Linux ili macOS) i instalirajte je. Distribucija Anakonde sadrži najnoviju verziju programskog jezika _Python 3_, interaktivno okruženje _Jupyter_, kao i sve biblioteke potrebne za ovaj kurs.
