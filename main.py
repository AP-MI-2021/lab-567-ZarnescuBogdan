import datetime

from Logic.CRUD import adaugaCheltuiala
from Tests.testAll import runAllTests
from UserInterface.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugaCheltuiala(5, 200.0, datetime.date(2021, 10, 15), 'intretinere', lista)
    lista = adaugaCheltuiala(3, 80.0, datetime.date(2021, 10, 3), 'canal', lista)
    runMenu(lista)


main()
