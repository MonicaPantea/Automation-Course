''' Exercitiul 1:
Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
Faceti acelasi lucru cu un for each
Faceti acelasi lucru cu un while
'''

# metoda 1:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    print('Masina mea preferata este', masina)

# metoda 2:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    print(f'Masina mea preferata este {masina}')

# metoda 3:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

masina = 0
while masina < len(masini):
    print(f'Masina mea preferata este {masini[masina]}')
    masina += 1

''' 
Exercitiul 2:
Aceeasi lista
Folositi un for
In for
   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
Printati varianta finala a listei
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in range(1, len(masini) - 1):
    masini[masina] = masini[masina].upper()
print(masini)

''' 
Exercitiul 3:
Aceeasi lista,
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin for each
Daca masina e mercedes (if)
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel
   Printam Am gasit masina X. Mai cautam
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Mercedes':
        print('am gasit masina dorita de dvs')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam')

''' 
Exercitiul 4:
Aceasi lista
Vine un cumparator bogat dar indecis.
Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
Daca masina e Trabant sau Lastun
   Folositi un cuvant cheie care sa dea skip la ce urmeaza
Printati S-ar putea sa va placa masina x
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {masina}')

''' 
Exercitiul 5:
Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
Salvati aceste masini in masini_vechi
Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        masini_vechi.append(masina)
        masini.remove(masina)
masini.append('Tesla')
print('Modele vechi:', masini_vechi)
print('Modele noi:', masini)

for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        masini_vechi.append(masina)
        index = masini.index(masina)
        masini[index] = 'Tesla'
        print('Modele vechi:', masini_vechi)
        print('Modele noi:', masini)

''' 
Exercitiul 6:
Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun
Iterati prin lista
'''

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
buget = 15000
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f'Pentru un buget sub {buget} puteti cumpara masina {masina}')

''' 
Exercitiul 7:
Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
x = 0  # de cate ori apare cifra 3. de fiecare data cand se ia valoarea 3 se adauga 1 la var x
for numar in numere:
    if numar == 3:
        x = x + 1
print(f'Numarul 3 apare de {x} ori')

''' 
Exercitiul 8:
Avand lista
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)
'''
# metoda 1
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for x in numere:
    suma = suma + x
print(suma)

# metoda 2
total = 0
for x in range(len(numere)):
    total = total + numere[x]
    print('Suma numerelor din lista este:', total)

''' 
Exercitiul 9:
Avand lista
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)
'''

# metoda 1
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere.sort(reverse=True)
print('Numarul cel mai mare din lista este:', numere[::len(numere)])

# metoda 2
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max = numere[0]
for numar in numere:
    if numar > max:
        max = numar
print(f'Cel mai mare numar din lista este: {max}')

''' 
Exercitiul 10:
Avand lista
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for numar in numere:
    if numar > 0:
        index = numere.index(numar)
        numere[index] = -abs(numar)
    if numar < 0:
        index = numere.index(numar)
        numere[index] = abs(numar)
print(numere)

''' 
Exercitiul 11:
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Iterati prin lista alte_numere
Populati corect celelalte liste
Afisati cele 4 liste la final
'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    if numar % 2 > 0:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    if numar < 0:
        numere_negative.append(numar)
print(numere_negative)
print(numere_pozitive)
print(numere_pare)
print(numere_impare)

''' 
Exercitiul 12:
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterati prin lista 2d
Printati ‘Cifra curenta este x’
(hint: nested for - adica for in for)
'''

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este: {tastatura_telefon[i][j]}')
