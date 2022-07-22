'''Exercitiul 1:
Clasa Cerc
Atribute: raza, culoare
Constructor pt ambele atribute
Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria
diametru()
circumferinta()
'''
import math


class Cerc:
    raza = None
    culoare = None

    # constructor
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    # metode
    def descrie_cerc(self):
        print(f'raza: {self.raza}, culoarea: {self.culoare}')

    def aria(self):
        print(f'aria este: {math.pi * self.raza ** 2}')
        return f'aria este: {math.pi * self.raza ** 2}'

    def calculam_diametrul(self):
        print(f'diametrul este: {self.raza * 2}')

    def calculam_circumferinta(self):
        print(f'diametrul este: {math.pi * self.raza * 2}')


cerc = Cerc(20, 'alb')
cerc.descrie_cerc()
cerc.aria()
cerc.calculam_diametrul()
cerc.calculam_circumferinta()

'''
Exercitiul 2:
Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pt toate atributele
Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si
va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
'''

class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    # constructor
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    # metode
    def descrie(self):
        print(f'lungimea: {self.lungime}, latimea: {self.latime}, culoarea: {self.culoare} ')

    def calculam_aria(self):
        print(f'aria este: {self.latime * self.lungime}')

    def calculam_perimetrul(self):
        print(f'perimetrul este: {(2 * self.latime) + (2 * self.lungime)}')

    def schimbam_culoarea(self):
        self.culoare = 'albastru'


dreptunghi = Dreptunghi(22, 15, 'roz')
dreptunghi.descrie()
dreptunghi.calculam_aria()
dreptunghi.calculam_perimetrul()
dreptunghi.schimbam_culoarea()
dreptunghi.descrie()

'''
Exercitiul 3:
Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''

class Angajat:
    nume = None
    prenume = None
    salariu = None

    #constructor

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    #metode

    def descrie(self):
        print(f'Nume: {self.nume}, prenume: {self.prenume}')

    def salariu_lunar(self):
        print(f'salariul este de: {self.salariu} lei, net pe luna.')

    def salariu_anual(self):
        print(f'salariul anual este: {self.salariu * 12}, lei')

    def marire_salariu(self):
        crestere_salariala = 0.1 * self.salariu
        print(f'noul salariu, dupa marire, este: {self.salariu + crestere_salariala} lei, net pe luna')

angajat = Angajat('Popescu', 'Ion', 2000)
angajat.descrie()
angajat.salariu_lunar()
angajat.salariu_anual()
angajat.marire_salariu()

'''
Exercitiul 4:
Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate
Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''

class Cont:
    iban = None
    titular_cont = None
    sold = None
    suma_tranzactionata = None

    # constructor
    def __init__(self, iban, titular_cont, sold, suma_tranzactionata):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
        self.suma_tranzactionata = suma_tranzactionata

    # metode
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self):
        print(f'Din contul titularului {self.titular_cont}, s-au debitat {self.suma_tranzactionata} lei. '
              f'Soldul este: {self.sold - self.suma_tranzactionata} lei')

    def creditare_cont(self):
        print(f'In contul titularului {self.titular_cont}, s-au creditat {self.suma_tranzactionata} lei. '
              f'Soldul este: {self.sold + self.suma_tranzactionata} lei')


titular_cont = Cont(23659871, 'Popescu Marian', 253000, 2569)
titular_cont.afisare_sold()
titular_cont.debitare_cont()
titular_cont.creditare_cont()

'''
Exercitiul 5:
Clasa Factura
Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie),
numar, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)
genereaza_factura() - va printa tabelar daca reusiti
Factura seria x numar y
Data: generati automat data de azi
Produs | cantitate | pret bucata | Total
Telefon |      7       |       700       | 49000
'''

from tabulate import tabulate
from datetime import datetime, date


class Factura:
    seria = 'FCT '
    numar = None
    nume_produs = None
    cantitate = None
    pret_bucata = None
    telefon = None

    # constructor
    def __init__(self, numar, nume_produs, cantitate, pret_bucata, telefon):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_bucata = pret_bucata
        self.telefon = telefon

    # metode
    def schimba_cantitatea(self):
        self.cantitate = int(input('modifica cantitate: '))

    def schimba_pretul(self):
        self.pret_bucata = int(input('modifica pret: '))

    def schimba_nume_produs(self):
        self.nume_produs = input('modifica nume produs: ')

    def genereaza_factura(self):
        total = self.pret_bucata * self.cantitate
        factura = [[self.nume_produs, self.pret_bucata, self.cantitate, total],
                   ['Telefon: ', self.telefon],
                   ['Data: ', date.today()],
                   ['Factura serie/ numar: ', self.seria, self.numar]]
        print(tabulate(factura, headers=['Produs', 'Pret per bucata', 'Cantitate', 'Total']))


factura_luna_mai = Factura(2516, 'Biscuiti', 6, 5, '0765.245.987')
factura_luna_mai.genereaza_factura()
factura_luna_mai.schimba_cantitatea()
factura_luna_mai.schimba_pretul()
factura_luna_mai.schimba_nume_produs()
factura_luna_mai.genereaza_factura()

'''
Exercitiul 6:
Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
descrie() (se vor printa toate atributele, inafara de culori_disponibile)
inmatriculare() - va schimba atributul inmatriculata in True
vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, a
ltfel afisati o eroare
accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare
decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza 0
'''

class Masina:
    marca = 'Dacia'
    model = None
    viteza_maxima = None
    viteza_actuala = 0
    culoare = 'Gri'
    culori_disponibile = {'Alb', 'Negru', 'Argintiu', 'Visiniu', 'Portocaliu', 'Verde', 'Maro'}
    inmatriculata = False

    #constructor
    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    #metode
    def descrie(self):
        print(f'Marca: {self.marca}, model:  {self.model}, viteza maxima: {self.viteza_maxima}, '
              f'culoare: {self.culoare}, inmatriculata: {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True
        print(f'Inmaticulata: {self.inmatriculata}')

    def vopseste(self):
        noua_culoare = input('Adauga noua culoare: ')
        if noua_culoare in self.culori_disponibile:
            print(f'Culoarea masinii alese se va schimba din gri in {noua_culoare}.')
        else:
            print('Aceasta culoare nu este disponibila. Masina va ramane culoarea gri.')

    def accelereaza(self):
        i = 0
        while i in range(self.viteza_maxima):
            print('Masina accelereaza!')
            i += 10
            if i == self.viteza_maxima:
                print('Opreste masina!')

    def franeaza(self):
        if self.viteza_maxima:
            print('Franeaza!')
        for i in range(self.viteza_maxima):
            if i == self.viteza_actuala:
                print('Masina s-a oprit!')


masina = Masina('Duster', 100)
masina.descrie()
masina.inmatriculare()
masina.vopseste()
masina.accelereaza()
masina.franeaza()

