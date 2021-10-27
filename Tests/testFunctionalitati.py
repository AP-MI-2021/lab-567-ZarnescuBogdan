import datetime

from Domain.cheltuiala import getSuma, getData, getNrApartament, getTip, getId
from Logic.CRUD import adaugaCheltuiala, getByNrApartament
from Logic.functionalitate1 import stergeToateCheltuielile
from Logic.functionalitate2 import adunaValoareCheltuieliDupaData
from Logic.functionalitate3 import celeMaiMariCheltuieli
from Logic.functionalitate4 import ordonareDescrescatorDupaSuma
from Logic.functionalitate5 import sumeLunarePerApartament


def testStergeToateCheltuielile():
    lista = []
    lista = adaugaCheltuiala('1', 1, 100.0, datetime.date(2021, 10, 20), 'alte cheltuieli', lista)
    lista = adaugaCheltuiala('2', 2, 150.0, datetime.date(2021, 10, 15), 'intretinere', lista)
    lista = adaugaCheltuiala('3', 1, 50.0, datetime.date(2021, 10, 4), 'canal', lista)

    lista = stergeToateCheltuielile(1, lista)

    assert len(lista) == 1
    assert getSuma(getByNrApartament(2, lista)) == 150.0
    assert getData(getByNrApartament(2, lista)) == datetime.date(2021, 10, 15)


def testAdunaValoareCheltuieliDupaData():
    lista = []
    lista = adaugaCheltuiala('1', 1, 100.0, datetime.date(2021, 10, 20), 'alte cheltuieli', lista)
    lista = adaugaCheltuiala('2', 2, 140.0, datetime.date(2021, 10, 15), 'intretinere', lista)
    lista = adaugaCheltuiala('3', 1, 50.0, datetime.date(2021, 10, 4), 'canal', lista)

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
    lista = adaugaCheltuiala('1', 1, 100.0, datetime.date(2021, 10, 20), 'alte cheltuieli', lista)
    lista = adaugaCheltuiala('2', 2, 140.0, datetime.date(2021, 10, 15), 'intretinere', lista)
    lista = adaugaCheltuiala('3', 1, 50.0, datetime.date(2021, 10, 4), 'canal', lista)

    rezultat = celeMaiMariCheltuieli(lista)

    assert len(rezultat) == 3
    assert rezultat['canal'] == 50.0
    assert rezultat['intretinere'] == 140.0


def testOrdonareDescrescatorDupaSuma():
    lista = []
    lista = adaugaCheltuiala('1', 1, 100.0, datetime.date(2021, 10, 20), 'alte cheltuieli', lista)
    lista = adaugaCheltuiala('2', 2, 140.0, datetime.date(2021, 10, 15), 'intretinere', lista)
    lista = adaugaCheltuiala('3', 1, 50.0, datetime.date(2021, 10, 4), 'canal', lista)

    rezultat = ordonareDescrescatorDupaSuma(lista)

    assert getId(rezultat[0]) == '2'
    assert getId(rezultat[1]) == '1'
    assert getId(rezultat[2]) == '3'


def testSumeLunarePerApartament():
    lista = []
    lista = adaugaCheltuiala('1', 5, 200.0, datetime.date(2021, 10, 15), 'intretinere', lista)
    lista = adaugaCheltuiala('2', 3, 80.0, datetime.date(2021, 10, 3), 'canal', lista)
    lista = adaugaCheltuiala('3', 5, 300.0, datetime.date(2020, 8, 25), 'canal', lista)
    lista = adaugaCheltuiala('4', 5, 350.0, datetime.date(2021, 9, 20), 'alte cheltuieloi', lista)
    lista = adaugaCheltuiala('5', 5, 150.0, datetime.date(2021, 10, 1), 'alte cheltuieloi', lista)

    rezultat = sumeLunarePerApartament(lista)

    assert rezultat[5][2021][10] == 350.0
    assert rezultat[3][2021][10] == 80.0
