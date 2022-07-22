'''
Exercitiul 1:
Joc ghicit zarul
Cauta pe net si vezi cum se genereaza un numar random
Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll
Luati un nr ghicit de la utilizator
Verificati si afisati daca utilizatorul a ghicit
3 optiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
Ai ghicit. Felicitari? Ai ales x si zarul a fost y
'''

import random

x = random.randint(0, 1000)
y = int(input('Tasteaza un numar:'))
if x > y:
    print(f'Mai incearca! Ai ales numarul:{y} si numarul generat a fost:{x}')
elif x < y:
    print(f'Felicitari! Ai castigat! Ai ales numarul:{y} si numarul generat a fost:{x}')
else:
    print(f'Nu te bucura! E egalitate! Ai ales numarul:{y} si numarul generat a fost:{x}')

'''
Exercitiul 2:
Cazuri de test:
Pentru a se putea imbarca o persoana, este nevoie ca urmatoarele scenarii sa fie adevarate:
1. > 18 ani + tara de calatorie UE
2. > 18 ani + tara de calatorie NON UE + Pasaport
3. < 18 ani + tara de calatorie UE + un parinte + act de acord al celuilalt parinte
4. < 18 ani + Tara de calatorie UE + ambii parinti
5. < 18 ani + tara de calatorie NON UE + pasaport + un parinte + act de acord al celuilalt parinte
6. < 18 ani + tara de calatorie NON UE + pasaport + ambii parinti
'''

varsta = int(input('Introdu varsta: '))
tara_de_calatorie_UE = input('Calatoriti in UE? ')
passport = input('Pasaport:')
insotit_de_mama = input('Insotit de mama: ')
insotit_de_tata = input('Insotit de tata: ')
act_permisiunea_mama = input('Act de permisiune din partea mamei: ')
act_permisiunea_tata = input('Act de permisiune din partea tatalui: ')


if varsta > 18 and tara_de_calatorie_UE == 'da':
    print('Te poti imbarca!')
elif varsta > 18 and tara_de_calatorie_UE == 'nu' and passport == 'da':
    print('Te poti imbarca!')
elif varsta < 18 and tara_de_calatorie_UE == 'da' and insotit_de_tata == 'da' and act_permisiunea_mama == 'da':
    print('Te poti imbarca!')
elif varsta < 18 and tara_de_calatorie_UE == 'da' and insotit_de_mama == 'da' and act_permisiunea_tata == 'da':
    print('Te poti imbarca!')
elif varsta < 18 and tara_de_calatorie_UE == 'da' and insotit_de_mama == 'da' and insotit_de_tata == 'da':
    print('Te poti imbarca!')
elif varsta < 18 and tara_de_calatorie_UE == 'nu' and passport == 'da' and insotit_de_tata == 'da' and \
        act_permisiunea_mama == 'da':
    print('Te poti imbarca!')
elif varsta < 18 and tara_de_calatorie_UE == 'nu' and passport == 'da' and insotit_de_mama == 'da' and \
        act_permisiunea_tata == 'da':
    print('Te poti imbarca!')
elif varsta < 18 and tara_de_calatorie_UE == 'nu' and passport == 'da' and \
        insotit_de_mama == 'da' and insotit_de_tata == 'da':
    print('Te poti imbarca!')
else:
    print('Nu te poti imbarca!')
