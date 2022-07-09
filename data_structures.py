'''
Exercitiul 1:
Declara o lista note_muzicale in care sa pui do re mi etc pana la do
Afiseaz-o
Inverseaza ordinea folosind slicing si suprascrie aceasta lista
Printeaza varianta actuala (inversata)
Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea.
(Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
'''

note = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note[::-1])

note = ['do', 'si', 'la', 'sol', 'fa', 'mi', 're', 'do']
note.reverse()
print(note)

'''
Exercitiul 2:
De cate ori apare ‘do’?
'''

note = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
x = 'do'
print(note.count(x))

'''
Exercitiul 3: 
Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]. 
Gasiti 2 variante sa le uniti intr-o singura lista.
'''

list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
list_3 = list_1 + list_2
print(list_3)

list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
list_1.extend(list_2)
print(list_1)

'''   
Exercitiul 4: 
Sortati si afisati lista generata la ex anterior
Stergeti numarul 0 folosind o functie
Afisati iar lista
'''

list_3 = [3, 1, 0, 2, 6, 5, 4]
list_3.sort()
print(list_3)

list_3.remove(0)
print(list_3)

'''
Exercitiul 5: 
Folosind un if verificati lista generata la ex3 si afisati
Lista este goala
Lista nu este goala
'''
list_3 = [3, 1, 0, 2, 6, 5, 4]

if len(list_3) == 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

'''
Exercitiul 6: 
Folositi o functie care sa stearga lista de la ex3
'''

list_3.clear()
print(list_3)

'''
Exercitiul 7:
Copy paste la ex 5. Verificati inca o data.
Acum ar trebui sa se afiseze ca lista e goala
'''

list_3 = [3, 1, 0, 2, 6, 5, 4]

if len(list_3) > 0:
    print('Lista nu este goala')
else:
    print('Lista  este goala')

''' 
Exercitiul 8: Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folositi o functie ca sa afisati Elevii (cheile)
'''
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())

''' 
Exercitiul 9: 
Printati cei 3 elevi si notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o veti lua folosindu-va de cheie
'''

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print('Ana a luat nota ' + str(dict1.get('Ana')))
print('Gigel a luat nota ' + str(dict1.get('Gigel')))
print('Dorel a luat nota ' + str(dict1.get('Dorel')))

'''
Exercitiul 10: Dorel facut contestatie si a primit 6
Modificati nota lui Dorel in 6
Printati nota dupa modificare
'''

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
dict1['Dorel'] = 6
print(dict1.get('Dorel'))

'''
Exercitiul 11: Gigel se transfera din clasa
Cautati o functie care sa il stearga
Vine un coleg nou. Adaugati Ionica, cu nota 9
Printati noii elevi
'''

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.pop('Gigel'))
dict1['Ionica'] = 9
print(dict1)

''' 
Exercitiul 12: 
Set
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
Adaugati in zilele_sapt ‘luni’
Afisati zile_sapt
'''

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)

'''
Ecercitiul 13:
Folositi un if si verificati daca 
Weekend este un subset al zilelor din sapt
Weekend nu este un subset al zilelor din sapt
'''

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
if weekend.issubset(zile_sapt):
    print('Weekend e subset.')
else:
    print('Weekend nu e subset.')

'''
Exercitiul 14: 
Afisati diferentele dintre aceste 2 seturi
'''

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
diferente = zile_sapt.difference(weekend)
print(diferente)

'''
Exercitiul 15: 
Afisati intersectia elementelor din aceste 2 seturi
'''

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
intersectie = zile_sapt.intersection(weekend)
print(intersectie)

''' 
Exercitiul 16: 
Ne imaginam o echipa de fotbal pt teren sintetic.
3 Schimbari maxime admise
Declara o Lista cu 5 jucatori
Schimbari_efectuate = va jucati voi cu valori diferite
Schimbari_max = 3
Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
Efectuam schimbarea
Stergem jucatorul scos din lista
Adaugam jucatorul intrat
Afisam a intra x, a iesit y, mai aveti z schimbari
Daca jucatorul nu e in teren:
Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Afisati ‘mai aveti z schimbari’
'''

jucatori_in_teren = ['Vlad', 'Costel', 'Viorel', 'Marian', 'Gogu']
jucatori_suspendati = []

if 'Costel' and 'Gogu' in jucatori_in_teren:
    jucatori_suspendati.append('Gogu')
    jucatori_suspendati.append('Costel')
    print('Gogu si Costel ies din teren!')
if 'Vlad' in jucatori_in_teren:
    jucatori_suspendati.append('Vlad')
    print('Iese si Vlad din teren! Mai puteti face o singura schimbare! ')
if 'Gogu' and 'Costel'in jucatori_suspendati:
    jucatori_in_teren.append('Gogu')
    jucatori_in_teren.append('Costel')
    jucatori_suspendati.append('Viorel')
    print('Gogu si Costel se intorc in teren, iar Viorel este scos afara!')

print(f'Jucatori suspendati la sfarsitul jocului:{jucatori_suspendati}')
print(f'Jucatori ramasi in teren la sfarsitul jocului:{jucatori_in_teren}')
