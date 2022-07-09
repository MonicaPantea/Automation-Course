'''
Exercitiul 1:
Verifica si afiseaza daca x este numar natural sau nu
'''

x = int(input('Scrie un numar: '))
if x <= 0:
    print('Numarul ales nu este natural.')
else:
    print('Ai ales un numar natural.')

'''
Exercitiul 2:
Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
'''

x = int(input('Scrie un numar: '))
if x < 0:
    print('Numarul este negativ.')
elif x==0:
    print('Numarul este neutru.')
else:
    print('Numarul este pozitiv.')

'''
Exercitiul 3:
Verifica si afiseaza daca x este intre -2 si 13
'''

x = int(input('Scrie un numar: '))
if -2 < x < 13:
    print('Numarul ales este corect.')
else:
    print('Numarul ales este incorect.')

'''
Exercitiul 4:
Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
'''

x = int(input('Scrie primul numar: '))
y = int(input('Scrie al doilea numar: '))
if x - y < 5:
    print('diferenta dintre cele doua numere este mai mica decat 5.')
else:
    print('diferenta dintre cele doua numere este mai mare decat 5.')

'''
Exercitiul 5:
Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
'''

x = int(input('scrie un numar: '))
if not x >= 5:
    print('In afara intervalului 5 - 27')
elif not x <= 27:
    print('In afara intervalului 5 - 27')
else:
    print('In intervalul 5 - 27')


'''
Exercitiul 6:
x si y (int) 
Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
'''

x = int(input('Scrie primul numar: '))
y = int(input('Scrie al doilea numar: '))
if x == y:
    print('Numere egale')
elif x > y:
    print('X mai mare ca Y')
else:
    print('Y mai mare ca X')

'''
Exercitiul 7: 
x, y, z - laturile unui triunghi
Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
'''

x = int(input('Scrie dimensiunea: Latura 1: '))
y = int(input('Scrie dimensiunea: Latura 2: '))
z = int(input('Scrie dimensiunea: Latura 3: '))
if x == y == z:
    print('Triunghi ECHILATERAL')
elif x == y or x == z or z == y:
    print('Triunghi ISOSCEL')
else:
    print('Triunghi ECHILATERAL')

'''
Exercitiul 8:
Citeste o litera de la tastatura Verifica si afiseaza daca este vocala sau nu
'''

x = input('o litera: ')
lista = ['a', 'e', 'i', 'o', 'u']
if x in lista:
    print('Vocala')
else:
    print('consoana')

'''
Exercitiul 9:
Transforma si printeaza notele din sistem romanesc in:
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''

x = float(input('Introdu nota: '))
if x > 9:
    print('A')
elif x > 8:
    print('B')
elif x > 7:
    print('C')
elif x > 6:
    print('D')
elif x > 4:
    print('E')
else:
    print('F')

'''
Exercitiul 10:
Verifica daca x are minim 4 cifre (x e int)
ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''

x = input('Tasteaza un numar:')
if len(x) >= 4:
    print('Numarul are minim 4 cifre')
else:
    print('Numarul nu are minim 4 cifre')

'''
Exercitiul 11: 
Verifica daca x are exact 6 cifre
'''

x = input('Tasteaza un numar:')
if len(x) == 6:
    print('Numarul are 6 cifre')
else:
    print('Numarul nu are 6 cifre')

'''
Exercitiul 12: 
Verifica daca x este numar par sau impar (x e int)
'''

x = int(input('Tasteaza un numar:'))
if x % 2 == 0:
    print('Numarul este par')
else:
    print('Numarul este impar')

'''
Exercitiul 13:
x, y, z (int). Afiseaza care este cel mai mare dintre ele?
'''

x = int(input('x:'))
y = int(input('y:'))
z = int(input('z:'))

if x > y >z:
    print('x este mai mare')
elif y > x >z:
    print('y este mai mare')
else:
    print('z este mai mare')

'''
Exercitiul 14:
x, y, z - reprezinta unghiurile unui triunghi
Verifica si afiseaza daca triunghiul este valid sau nu
'''

x = int(input('Introdu masura primului unghi:'))
y = int(input('Introdu masura unghiului 2:'))
z = int(input('Introdu masura unghiului 3:'))
if x > 0 and y > 0 and z > 0 and x + y + z <= 180:
    print('Triunghi valid')
else:
    print('Triunghi invalid')

