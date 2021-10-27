import datetime

from Domain.cheltuiala import creeazaCheltuiala, getNrApartament, getSuma, getData, getTip


def testCheltuiala():
    cheltuiala = creeazaCheltuiala('1', 5, 200.0, datetime.date(2021, 10, 4), 'intretinere')

    assert getNrApartament(cheltuiala) == 5
    assert getSuma(cheltuiala) == 200.0
    assert getData(cheltuiala) == datetime.date(2021, 10, 4)
    assert getTip(cheltuiala) == 'intretinere'
