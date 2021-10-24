from Domain.cheltuiala import creeazaCheltuiala, getNrApartament, getSuma, getData, getTip


def testCheltuiala():
    cheltuiala = creeazaCheltuiala(5, 200.0, 2021-10-4, 'intretinere')

    assert getNrApartament(cheltuiala) == 5
    assert getSuma(cheltuiala) == 200.0
    assert getData(cheltuiala) == 2021-10-4
    assert getTip(cheltuiala) == 'intretinere'