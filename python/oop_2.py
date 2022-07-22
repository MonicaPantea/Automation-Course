'''
ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
ENCAPSULATION
Latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)
Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
Raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte
(optional, doar daca ati ales sa implementati metoda abstracta aria)
POLYMORPHISM
Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
Creati un obiect de tip Patrat si jucati-va cu metodele lui
Creati un obiect de tip Cerc si jucati-va cu metodele lui
'''


# clasa parinte
from abc import abstractmethod


class FormaGeometrica:
    pi = 3.14


    @abstractmethod
    def aria(self):
        raise NotImplementedError


def descriere(self):
    print('Cel mai probabil am colturi')


# clase copil care mostenesc  cele 2 metode si constanta pi ale clasei parinte

class Patrat(FormaGeometrica):
    __latura = None

    def __init__(self, __latura):
        self.__latura = __latura

    def calculeaza_aria(self):
        print(f'Aria patratului este: {self.__latura **2}')

    def getter_latura(self):
        print(f'Getter method called. Latura este: {self.__latura}')
        return self.__latura

    def setter_latura(self, a):
        print(f'Setter method called. Latura a fost modificata. Noua valoare este: {a}')
        self.__latura = a

    def deleter_latura(self):
        del self.__latura

    def descriere(self):
        print('Cel mai probabil am colturi')


class Cerc(FormaGeometrica):
    __raza = None

    def __init__(self, __raza):
        self.__raza = __raza


    def calculeaza_aria(self):
        print(f'Aria cercului este: {self.pi * self.__raza ** 2}')

    def getter_raza(self):
        print(f'Getter method called. Raza este: {self.__raza}')
        return self.__raza

    def setter_raza(self, a):
        print(f'Setter method called. Raza a fost modificata. Noua valoare este: {a}')
        self.__raza = a

    def deleter_raza(self):
        del self.__raza

    def descriere(self):
        print('Eu nu am colturi')


cerc1 = Cerc(5)
cerc1.descriere()
cerc1.calculeaza_aria()
cerc1.getter_raza()
cerc1.setter_raza(6)
cerc1.deleter_raza()


patrat = Patrat(12)
patrat.descriere()
patrat.calculeaza_aria()
patrat.getter_latura()
patrat.setter_latura(6)
patrat.deleter_latura()
