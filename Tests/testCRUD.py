import datetime

from Domain.cheltuiala import getNrApartament, getSuma, getData, getTip
from Logic.CRUD import adaugaCheltuiala, getByNrApartament, stergeCheltuiala, modificaCheltuiala


def testAdaugaCheltuiala():
    lista = []
    lista = adaugaCheltuiala('1', 5, 200.0, datetime.date(2021, 10, 4), 'intretinere', lista)

    assert len(lista) == 1
    assert getNrApartament(getByNrApartament(5, lista)) == 5
    assert getSuma(getByNrApartament(5, lista)) == 200.0
    assert getData(getByNrApartament(5, lista)) == datetime.date(2021, 10, 4)
    assert getTip(getByNrApartament(5, lista)) == 'intretinere'


def testGetByNrApartament():
    lista = []
    lista = adaugaCheltuiala('1', 5, 200.0, datetime.date(2021, 10, 4), 'intretinere', lista)
    lista = adaugaCheltuiala('2', 12, 50.0, datetime.date(2021, 10, 2), 'canal', lista)

    assert getByNrApartament(5, lista) is not None
    assert getByNrApartament(12, lista) is not None
    assert getByNrApartament(10, lista) is None


def testStergeCheltuiala():
    lista = []
    lista = adaugaCheltuiala('1', 5, 200.0, datetime.date(2021, 10, 4), 'intretinere', lista)
    lista = adaugaCheltuiala('2', 12, 50.0, datetime.date(2021, 10, 2), 'canal', lista)

    lista = stergeCheltuiala('1', lista)

    assert len(lista) == 1
    assert getByNrApartament(5, lista) is None
    assert getByNrApartament(12, lista) is not None
    try:
        lista = stergeCheltuiala('8', lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert getByNrApartament(12, lista) is not None
    except Exception:
        assert False


def testModificaCheltuiala():
    lista = []
    lista = adaugaCheltuiala('1', 5, 200.0, datetime.date(2021, 10, 4), 'intretinere', lista)
    lista = adaugaCheltuiala('2', 12, 50.0, datetime.date(2021, 10, 2), 'canal', lista)

    lista = modificaCheltuiala('1', 5, 150.0, datetime.date(2021, 10, 10), 'alte cheltuieli', lista)

    cheltuialaUpdatata = getByNrApartament(5, lista)
    assert getNrApartament(cheltuialaUpdatata) == 5
    assert getSuma(cheltuialaUpdatata) == 150.0
    assert getData(cheltuialaUpdatata) == datetime.date(2021, 10, 10)
    assert getTip(cheltuialaUpdatata) == 'alte cheltuieli'

    cheltuialaNeupdatata = getByNrApartament(12, lista)
    assert getNrApartament(cheltuialaNeupdatata) == 12
    assert getSuma(cheltuialaNeupdatata) == 50.0
    assert getData(cheltuialaNeupdatata) == datetime.date(2021, 10, 2)
    assert getTip(cheltuialaNeupdatata) == 'canal'

    lista = []
    lista = adaugaCheltuiala('1', 5, 200.0, datetime.date(2021, 10, 4), 'intretinere', lista)
    try:
        lista = modificaCheltuiala('2', 8, 100.0, datetime.date(2021, 10, 15), 'canal', lista)
        assert False
    except ValueError:
        cheltuialaNeupdatata = getByNrApartament(5, lista)
        assert getNrApartament(cheltuialaNeupdatata) == 5
        assert getSuma(cheltuialaNeupdatata) == 200.0
        assert getData(cheltuialaNeupdatata) == datetime.date(2021, 10, 4)
        assert getTip(cheltuialaNeupdatata) == 'intretinere'
