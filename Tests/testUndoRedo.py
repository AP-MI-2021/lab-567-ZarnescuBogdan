import datetime

from Domain.cheltuiala import getNrApartament, getSuma, getData, getTip
from Logic.CRUD import getById, getByNrApartament
from UserInterface.console import uiAdaugaCheltuiala, undo, redo, uiStergeCheltuiala, uiModificaCheltuiala, \
    uiStergeToateCheltuielile, uiAdunaValoareCheltuieliDupaData


def testUndoRedo():
    #1 lista initiala goala
    lista = []
    undoOperations = []
    redoOperations = []

    #2 adaugam un obiect
    obiect = ['1', 1, 100, datetime.date(2021, 10, 11), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)

    #3 adaugam inca un obiect
    obiect = ['2', 2, 200, datetime.date(2021, 10, 12), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)

    #4 adaugam inca un obiect
    obiect = ['3', 3, 300, datetime.date(2021, 10, 13), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)

    assert len(lista) == 3

    #5 undo scoate ultimul obiect adaugat
    lista = undo(lista, undoOperations, redoOperations)

    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is not None
    assert getById('3', lista) is None

    #6 inca un undo scoate penultimul obiect adaugat
    lista = undo(lista, undoOperations, redoOperations)

    assert len(lista) == 1
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None

    #7 inca un undo scoate si primul element adaugat
    lista = undo(lista, undoOperations, redoOperations)

    assert len(lista) == 0
    assert getById('1', lista) is None
    assert getById('2', lista) is None
    assert getById('3', lista) is None

    #8 inca un undo nu face nimic
    lista = undo(lista, undoOperations, redoOperations)

    assert len(lista) == 0
    assert getById('1', lista) is None
    assert getById('2', lista) is None
    assert getById('3', lista) is None

    #9 adaugam trei obiecte
    obiect = ['1', 1, 100, datetime.date(2021, 10, 11), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)
    obiect = ['2', 2, 200, datetime.date(2021, 10, 12), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)
    obiect = ['3', 3, 300, datetime.date(2021, 10, 13), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)

    assert len(lista) == 3

    #10 redo nu face nimic
    lista = redo(lista, undoOperations, redoOperations)

    assert len(lista) == 3
    assert getById('1', lista) is not None
    assert getById('2', lista) is not None
    assert getById('3', lista) is not None

    #11 doua undo-uri scot ultimele 2 obiecte
    lista = undo(lista, undoOperations, redoOperations)
    lista = undo(lista, undoOperations, redoOperations)

    assert len(lista) == 1
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None

    #12 redo anuleaza ultimul undo, daca ultima operatie e undo
    lista = redo(lista, undoOperations, redoOperations)

    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is not None
    assert getById('3', lista) is None

    #13 redo anuleaza si primul undo
    lista = redo(lista, undoOperations, redoOperations)

    assert len(lista) == 3
    assert getById('1', lista) is not None
    assert getById('2', lista) is not None
    assert getById('3', lista) is not None

    #14 doua undo-uri scot ultimele 2 obiecte
    lista = undo(lista, undoOperations, redoOperations)
    lista = undo(lista, undoOperations, redoOperations)

    assert len(lista) == 1
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None

    #15 adaugam un obiect
    obiect = ['4', 4, 400, datetime.date(2021, 10, 14), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)

    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None
    assert getById('4', lista) is not None

    #16 redo nu face nimic, deoarece ultima operatie nu este un undo
    lista = redo(lista, undoOperations, redoOperations)

    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None
    assert getById('4', lista) is not None

    #17 undo anuleaza adaugarea lui o4
    lista = undo(lista, undoOperations, redoOperations)

    assert len(lista) == 1
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None
    assert getById('4', lista) is None

    #18 undo anuleaza adaugarea lui o1 - practic se continua sirul de undo de la pct 14
    lista = undo(lista, undoOperations, redoOperations)

    assert len(lista) == 0

    #19 se anuleaza ultimele 2 undo-uri
    lista = redo(lista, undoOperations, redoOperations)
    lista = redo(lista, undoOperations, redoOperations)

    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None
    assert getById('4', lista) is not None

    #20 redo nu face nimic
    lista = redo(lista, undoOperations, redoOperations)

    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None
    assert getById('4', lista) is not None

    #21 testUndoRedo - stergere cheltuiala
    lista = []
    obiect = ['1', 1, 100, datetime.date(2021, 10, 11), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)
    obiect = ['2', 2, 200, datetime.date(2021, 10, 12), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)
    obiect = ['3', 3, 300, datetime.date(2021, 10, 13), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)

    obiect = ['2']
    lista = uiStergeCheltuiala(lista, undoOperations, redoOperations, obiect)

    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is not None

    lista = undo(lista, undoOperations, redoOperations)

    assert len(lista) == 3
    assert getById('1', lista) is not None
    assert getById('2', lista) is not None
    assert getById('3', lista) is not None

    lista = redo(lista, undoOperations, redoOperations)

    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is not None

    #22 testUndoRedo - modificare cheltuiala
    lista = []
    obiect = ['1', 1, 100, datetime.date(2021, 10, 11), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)
    obiect = ['2', 2, 200, datetime.date(2021, 10, 12), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)
    obiect = ['3', 3, 300, datetime.date(2021, 10, 13), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)

    obiect = ['2', 10, 1000, datetime.date(2021, 10, 20), 'intretinere']
    lista = uiModificaCheltuiala(lista, undoOperations, redoOperations, obiect)

    assert len(lista) == 3
    assert getNrApartament(getById('2', lista)) == 10
    assert getSuma(getById('2', lista)) == 1000.0
    assert getData(getById('2', lista)) == datetime.date(2021, 10, 20)
    assert getTip(getById('2', lista)) == 'intretinere'

    lista = undo(lista, undoOperations, redoOperations)

    assert len(lista) == 3
    assert getNrApartament(getById('2', lista)) == 2
    assert getSuma(getById('2', lista)) == 200.0
    assert getData(getById('2', lista)) == datetime.date(2021, 10, 12)
    assert getTip(getById('2', lista)) == 'canal'

    lista = redo(lista, undoOperations, redoOperations)

    assert len(lista) == 3
    assert getNrApartament(getById('2', lista)) == 10
    assert getSuma(getById('2', lista)) == 1000.0
    assert getData(getById('2', lista)) == datetime.date(2021, 10, 20)
    assert getTip(getById('2', lista)) == 'intretinere'

    #23 testUndoRedo - stergerea tuturor cheltuielilor pentru un apartament dat
    lista = []
    obiect = ['1', 1, 100, datetime.date(2021, 10, 11), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)
    obiect = ['2', 2, 200, datetime.date(2021, 10, 12), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)
    obiect = ['3', 3, 300, datetime.date(2021, 10, 13), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)
    obiect = ['4', 3, 400, datetime.date(2021, 10, 14), 'intretinere']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)
    obiect = ['5', 3, 500, datetime.date(2021, 10, 15), 'alte cheltuieli']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)

    obiect = [3]
    lista = uiStergeToateCheltuielile(lista, undoOperations, redoOperations, obiect)

    assert len(lista) == 2
    assert getByNrApartament(1, lista) is not None
    assert getByNrApartament(2, lista) is not None
    assert getByNrApartament(3, lista) is None

    lista = undo(lista, undoOperations, redoOperations)

    assert len(lista) == 5
    assert getByNrApartament(1, lista) is not None
    assert getByNrApartament(2, lista) is not None
    assert getByNrApartament(3, lista) is not None

    lista = redo(lista, undoOperations, redoOperations)

    assert len(lista) == 2
    assert getByNrApartament(1, lista) is not None
    assert getByNrApartament(2, lista) is not None
    assert getByNrApartament(3, lista) is None

    #24 testUndoRedo - adunarea unei valori la toate cheltuielile dintr-o data citita
    lista = []
    obiect = ['1', 1, 100, datetime.date(2021, 10, 11), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)
    obiect = ['2', 2, 200, datetime.date(2021, 10, 11), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)
    obiect = ['3', 3, 300, datetime.date(2021, 10, 13), 'canal']
    lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)

    obiect = [datetime.date(2021, 10, 11), 50]
    lista = uiAdunaValoareCheltuieliDupaData(lista, undoOperations, redoOperations, obiect)

    assert getSuma(getById('1', lista)) == 150.0
    assert getSuma(getById('2', lista)) == 250.0
    assert getSuma(getById('3', lista)) == 300.0

    lista = undo(lista, undoOperations, redoOperations)

    assert getSuma(getById('1', lista)) == 100.0
    assert getSuma(getById('2', lista)) == 200.0
    assert getSuma(getById('3', lista)) == 300.0

    lista = redo(lista, undoOperations, redoOperations)

    assert getSuma(getById('1', lista)) == 150.0
    assert getSuma(getById('2', lista)) == 250.0
    assert getSuma(getById('3', lista)) == 300.0
