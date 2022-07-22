'''
Exercitiul 1:
Functie care sa calculeze si sa returneze suma a 2 numere
'''

def suma(numar1, numar2):
    suma_a_2_nr = numar1 + numar2
    return suma_a_2_nr

''' 
Exercitiul 2:
Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
'''

def par_sau_impar(numar):
    if numar % 2 == 0:
        return True
    if numar % 2 > 0:
        return False

''' 
Exercitiul 3:
Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu) 
'''

def numar_caractere_nume(nume, prenume1, prenume2):
    x = len(nume + prenume1 + prenume2)
    return x

''' 
Exercitiul 4:
Functie care returneaza aria dreptunghiului
'''

import math
def arie_dreptunghi(a, b):
    arie = a * b
    return arie

''' 
Exercitiul 5:
Functie care returneaza aria cercului
'''

def aria_cercului(raza):
    aria = math.pi * raza**2
    return aria

''' 
Exercitiul 6:
Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
'''

def caracter_in_string(caracter_x, string):
    if caracter_x in string:
        return True
    if caracter_x not in string:
        return False

'''
Exercitiul 7:
Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
'''

def lista_numere(*numere):
    numere_pozitive = []
    for i in numere:
        if i > 0:
            numere_pozitive.append(i)
    return (numere_pozitive)


'''
Exercitiul 8:
Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale. 
'''

def care_nr_e_mai_mare(numar1, numar2):
    if numar1 > numar2:
        print('Primul numar este mai mare decat al doilea')
    if numar2 > numar1:
        print('Al doilea numar este mai mare decat primul')
    if numar1 == numar2:
        print('Numerele sunt egale')

'''
Exercitiul 9: 
Functie care primeste o luna din an si returneaza cate zile are acea luna
'''

from calendar import monthrange
def calendar(year, month):
    return monthrange(year,month)[1]

'''
Exercitiul 10: 
Functie calculator care sa returneze 4 valori 
Suma, diferenta, inmultirea, impartirea a 2 numere                 
In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
'''

def calculator(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return f'Suma este: {a }'\
    f'Diferenta este: {b }'\
    f'Inmultirea este: {c }'\
    f'SImpartirea este: {d }'\

'''
Exercitiul 12:
Functie care primeste 3 numere
Returneaza valoarea maxima dintre ele
'''

def cel_mai_mare_nr(a, b, c):
    if a != b and a != c and b != c:
        return max(a, b, c)

