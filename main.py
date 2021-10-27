import datetime

from Logic.CRUD import adaugaCheltuiala
from Tests.testAll import runAllTests
from UserInterface.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugaCheltuiala('1', 5, 200.0, datetime.date(2021, 10, 15), 'intretinere', lista)
    lista = adaugaCheltuiala('2', 3, 80.0, datetime.date(2021, 10, 3), 'canal', lista)
    lista = adaugaCheltuiala('3', 5, 300.0, datetime.date(2020, 8, 25), 'canal', lista)
    lista = adaugaCheltuiala('4', 5, 350.0, datetime.date(2021, 9, 20), 'alte cheltuieloi', lista)
    lista = adaugaCheltuiala('5', 5, 150.0, datetime.date(2021, 10, 1), 'alte cheltuieloi', lista)
    runMenu(lista)


main()
