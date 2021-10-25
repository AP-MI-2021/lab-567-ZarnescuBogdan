import datetime

from Domain.cheltuiala import getSuma, getData, getNrApartament, getTip
from Logic.CRUD import adaugaCheltuiala, getByNrApartament
from Logic.functionalitate1 import stergeToateCheltuielile
from Logic.functionalitate2 import adunaValoareCheltuieliDupaData
from Logic.functionalitate3 import celeMaiMariCheltuieli


def testStergeToateCheltuielile():
    lista = []
    lista = adaugaCheltuiala(1, 100.0, datetime.date(2021, 10, 20), 'alte cheltuieli', lista)
    lista = adaugaCheltuiala(2, 150.0, datetime.date(2021, 10, 15), 'intretinere', lista)
    lista = adaugaCheltuiala(1, 50.0, datetime.date(2021, 10, 4), 'canal', lista)

    lista = stergeToateCheltuielile(1, lista)

    assert len(lista) == 1
    assert getSuma(getByNrApartament(2, lista)) == 150.0
    assert getData(getByNrApartament(2, lista)) == datetime.date(2021, 10, 15)


def testAdunaValoareCheltuieliDupaData():
    lista = []
    lista = adaugaCheltuiala(1, 100.0, datetime.date(2021, 10, 20), 'alte cheltuieli', lista)
    lista = adaugaCheltuiala(2, 140.0, datetime.date(2021, 10, 15), 'intretinere', lista)
    lista = adaugaCheltuiala(1, 50.0, datetime.date(2021, 10, 4), 'canal', lista)

    lista = adunaValoareCheltuieliDupaData(datetime.date(2021, 10, 20), 50, lista)

    cheltuialaUpdatata = getByNrApartament(1, lista)
    assert getNrApartament(cheltuialaUpdatata) == 1
    assert getSuma(cheltuialaUpdatata) == 150.0
    assert getData(cheltuialaUpdatata) == datetime.date(2021, 10, 20)
    assert getTip(cheltuialaUpdatata) == 'alte cheltuieli'

    cheltuialaNeupdatata = getByNrApartament(2, lista)
    assert getNrApartament(cheltuialaNeupdatata) == 2
    assert getSuma(cheltuialaNeupdatata) == 140.0
    assert getData(cheltuialaNeupdatata) == datetime.date(2021, 10, 15)
    assert getTip(cheltuialaNeupdatata) == 'intretinere'


def testCeleMaiMariCheltuieli():
    lista = []
    lista = adaugaCheltuiala(1, 100.0, datetime.date(2021, 10, 20), 'alte cheltuieli', lista)
    lista = adaugaCheltuiala(2, 140.0, datetime.date(2021, 10, 15), 'intretinere', lista)
    lista = adaugaCheltuiala(1, 50.0, datetime.date(2021, 10, 4), 'canal', lista)

    '''assert celeMaiMariCheltuieli(lista) == [{'nrApartament': 2, 'suma': 140.0, 'data': datetime.date(2021, 10, 15), 'tip': 'intretinere'},
                                            {'nrApartament': 1, 'suma': 50.0, 'data': datetime.date(2021, 10, 4), 'tip': 'canal'},
                                            {'nrApartament': 1, 'suma': 100.0, 'data': datetime.date(2021, 10, 20), 'tip': 'alte cheltuieli'}]'''
    assert getNrApartament(celeMaiMariCheltuieli(lista)[0]) == 2
    assert getNrApartament(celeMaiMariCheltuieli(lista)[1]) == 1
    assert getNrApartament(celeMaiMariCheltuieli(lista)[2]) == 1
    assert getTip(celeMaiMariCheltuieli(lista)[0]) == 'intretinere'
    assert getTip(celeMaiMariCheltuieli(lista)[1]) == 'canal'
    assert getTip(celeMaiMariCheltuieli(lista)[2]) == 'alte cheltuieli'
    assert getSuma(celeMaiMariCheltuieli(lista)[0]) == 140.0
    assert getSuma(celeMaiMariCheltuieli(lista)[1]) == 50.0
    assert getSuma(celeMaiMariCheltuieli(lista)[2]) == 100.0
