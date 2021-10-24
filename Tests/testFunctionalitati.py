from Domain.cheltuiala import getSuma
from Logic.CRUD import adaugaCheltuiala, getByNrApartament
from Logic.functionalitate1 import stergeToateCheltuielile


def testStergeToateCheltuielile():
    lista = []
    lista = adaugaCheltuiala(1, 100.0, 2021-10-20, 'alte cheltuieli', lista)
    lista = adaugaCheltuiala(2, 150.0, 2021-10-15, 'intretinere', lista)
    lista = adaugaCheltuiala(1, 50.0, 2021-10-4, 'canal', lista)

    lista = stergeToateCheltuielile(1, lista)

    assert len(lista) == 1
    assert getSuma(getByNrApartament(2, lista)) == 150.0