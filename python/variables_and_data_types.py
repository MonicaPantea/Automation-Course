'''
Exercitiul 1:
Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
string, int, float, bool
'''

masina = 'Ford'
an_de_fabricatie = 2020
pret = 13.520
inmatriculata = True
print(masina, an_de_fabricatie, pret, inmatriculata)

'''
Exercitiul 2:
Utilizat functia type pentru a verifica daca au tipul de date asteptat
'''

x = '15'
y = 15
z = 15.3
a = False
print(type(x))
print(type(y))
print(type(z))
print(type(a))

'''
Exercitiul 3:
Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
Verificati tipul acesteia
'''

x = 25.4
x = round(x)
print(x)
print(type(x))

'''
Exercitiul 4:
Folositi print() si printati in consola 4 propozitii folosind cele 4 variabile. 
(rezolvati nepotrivirile de tip prin ce modalitate doriti)
'''
# propozitia 1
specie = 'S. aureus'
dimensiune = 1.5
incubare = 37
patogen_uman = True
print(f'Specia:{specie} are dimensiunea:{dimensiune} de micrometri,'
      f' creste la temperatura de:{incubare} grede celsius si este patogen uman:{patogen_uman}')

# propozitia 2
ingredient_principal = 'tei'
zahar = 1.5
apa = 100
efect_calmant = True
print(f'Ceaiul de tei se prepara din:{ingredient_principal} doua lingurite de planta uscata, '
      f'zahar:{zahar} lingurite, apa:{apa} ml si are efect calmant:{efect_calmant}')

# propozitia 3
filmul = 'Mumia'
ora = 20.35
durata = 2
film_romantic = False
print(f'Filmul:{filmul} incepe la ora:{ora}, dureaza:{durata} ore si este un film romantic:{film_romantic}')

# propozitia 4
nume = 'Oscar'
prenume = 'Gigel'
varsta = 45
inaltime = 1.58
greutate = 93
joaca_baschet = False
print(f'Vecinul:{nume} {prenume} are:{varsta} de ani, o inaltime de:{inaltime} metri, '
      f'o greutate de:{greutate} kg si in fiecare seara joaca basket:{joaca_baschet}')

'''
Exercitiul 5:
Citeste de la tastatura numele
Citeste de la tastatura prenumele
Afiseaza 'Numele complet are x caractere'
'''

x = input('Numele tau este:')
print(x)
y = input('Prenumele tau este:')
print(y)
print(f'Numele complet are:{len(x + y)} caractere')

'''
Exercitiul 6:
Citeste de la tastatura lungimea
Citeste de la tastatura latimea
Afiseaza 'Aria dreptunghiului este x'
'''

a = input('lungimea este:')
print(a)
b = input('latimea este:')
print(b)
arie = int(a) * int(b)
print(f'Aria dreptunghiului este:{arie} centimetri')

'''
Exercitiul 7:
Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
Cititi de la tastatura un int x
Afiseaza stringul fara ultimele x caractere
ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
'''

a = 'Coral is either the stupidest animal or the smartest rock'
print(len(a))
x = int(input('Tasteaza un numar:'))
if x >40:
      print(a)
else:
      print(a[0:57 - x])

'''
Exercitiul 8:
Acelasi string
Declara un string nou care sa fie format din primele 5 caractere + ultimele 5
'''

a = 'Coral is either the stupidest animal or the smartest rock'
print(len(a))
print(a[0:5] + a[52:58])

'''
Exercitiul 9:
Acelasi string
Afisati de cate ori apare cuvantul 'the'
'''

txt = 'Coral is either the stupidest animal or the smartest rock'
x = 'the'
print(txt.count(x))

'''
Exercitiul 10:
Acelasi string
Inlocuieste the cu THE peste tot
Printeaza rezultatul
'''

txt = 'Coral is either the stupidest animal or the smartest rock'
txt2 = txt.replace('the', 'THE')
print(txt2)

'''
Exercitiul 11:
Acelasi string
Salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
(hint: este o functie care te ajuta sa faci asta)
Folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
output: 'Coral is either the stupidest animal or the smartest ' 
'''

txt = 'Coral is either the stupidest animal or the smartest rock'
print(len(txt) - 3)
print(txt[:52])

'''
Exercitiul 12:
Citeste de la tastatura un string
Verifica daca primul si ultimul caracter sunt la fel
Se va folosi un assert
'''

x = input('tasteaza ceva: ')
assert x[0] == x[len(x)-1]
print('foarte bne')

'''
Exercitiul 13:
Avand stringul '0123456789'
Afisati doar numerele pare 
Acum afisati doar numerele impare
(hint: folositi slicing, controlati din pas)
'''

w = '0123456789'
print(w[0:9:2])
print(w[1:10:2])

'''
Exercitiul 14:
Acelasi string de mai sus
Verificati daca acest string contine doar numere
hint: merge cu slicing? probabil ca nu... ce mai stim atunci legat de string?
poate gasim o functie ajutatoare
'''

txt ='0123456789'
x = txt.isnumeric()
print(x)

'''
Exercitiul 15:
Citeste un user de la tastatura
Citeste o parola
Afiseaza: 'Parola pt user x este ***** si are x caractere'
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
eg: parola abc => ***
parola abcd => ****
'''

user = input('user: ')
parola = input('parola: ')
x = len(parola)
print(f'Parola pentru user:{user} este:{parola} si are:{x} caractere')

'''
Exercitiul 16:
Folosind assert, verificati daca un string este palindrom
'''

cuvantul = input('Cuvantul e palindrom: ')
cuvantul_invers = cuvantul[::-1]
assert cuvantul == cuvantul_invers
print('cuvantul e palindrom')
