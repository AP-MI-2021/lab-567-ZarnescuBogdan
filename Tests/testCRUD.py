from Domain.cheltuiala import getNrApartament, getSuma, getData, getTip
from Logic.CRUD import adaugaCheltuiala, getByNrApartament, stergeCheltuiala, modificaCheltuiala


def testAdaugaCheltuiala():
    lista = []
    lista = adaugaCheltuiala(5, 200.0, 2021-10-4, 'intretinere', lista)

    assert len(lista) == 1
    assert getNrApartament(getByNrApartament(5, lista)) == 5
    assert getSuma(getByNrApartament(5, lista)) == 200.0
    assert getData(getByNrApartament(5, lista)) == 2021-10-4
    assert getTip(getByNrApartament(5, lista)) == 'intretinere'

def testStergeCheltuiala():
    lista = []
    lista = adaugaCheltuiala(5, 200.0, 2021-10-4, 'intretinere', lista)
    lista = adaugaCheltuiala(12, 50.0, 2021-10-2, 'canal', lista)

    lista = stergeCheltuiala(5, lista)

    assert len(lista) == 1
    assert getByNrApartament(5, lista) is None
    assert getByNrApartament(12, lista) is not None

    lista = stergeCheltuiala(8, lista)

    assert len(lista) == 1
    assert getByNrApartament(12, lista) is not None

def testModificaCheltuiala():
    lista = []
    lista = adaugaCheltuiala(5, 200.0, 2021-10-4, 'intretinere', lista)
    lista = adaugaCheltuiala(12, 50.0, 2021-10-2, 'canal', lista)

    lista = modificaCheltuiala(5, 150.0, 2021-10-10, 'alte cheltuieli', lista)

    cheltuialaUpdatata = getByNrApartament(5, lista)
    assert getNrApartament(cheltuialaUpdatata) == 5
    assert getSuma(cheltuialaUpdatata) == 150.0
    assert getData(cheltuialaUpdatata) == 2021-10-10
    assert getTip(cheltuialaUpdatata) == 'alte cheltuieli'

    cheltuialaNeupdatata = getByNrApartament(12, lista)
    assert getNrApartament(cheltuialaNeupdatata) == 12
    assert getSuma(cheltuialaNeupdatata) == 50.0
    assert getData(cheltuialaNeupdatata) == 2021-10-2
    assert getTip(cheltuialaNeupdatata) == 'canal'

    lista = []
    lista = adaugaCheltuiala(5, 200.0, 2021-10-4, 'intretinere', lista)

    lista = modificaCheltuiala(8, 100.0, 2021-10-15, 'canal', lista)

    cheltuialaNeupdatata = getByNrApartament(5, lista)
    assert getNrApartament(cheltuialaNeupdatata) == 5
    assert getSuma(cheltuialaNeupdatata) == 200.0
    assert getData(cheltuialaNeupdatata) == 2021-10-4
    assert getTip(cheltuialaNeupdatata) == 'intretinere'
