import datetime

from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, getById


def testUndoRedo():
    undoOperations = []
    redoOperations = []
    lista = []

    rezultat = adaugaCheltuiala('1', 1, 100, datetime.date(2021, 10, 10), 'canal', lista)
    undoOperations.append([
        lambda: stergeCheltuiala('1', lista),
        lambda: adaugaCheltuiala('1', 1, 100, datetime.date(2021, 10, 10), 'canal', lista)
    ])
    redoOperations.clear()
    lista = rezultat

    rezultat = adaugaCheltuiala('2', 1, 100, datetime.date(2021, 10, 11), 'canal', lista)
    undoOperations.append([
        lambda: stergeCheltuiala('2', lista),
        lambda: adaugaCheltuiala('2', 1, 100, datetime.date(2021, 10, 11), 'canal', lista)
    ])
    redoOperations.clear()
    lista = rezultat

    rezultat = adaugaCheltuiala('3', 1, 100, datetime.date(2021, 10, 12), 'canal', lista)
    undoOperations.append([
        lambda: stergeCheltuiala('3', lista),
        lambda: adaugaCheltuiala('3', 1, 100, datetime.date(2021, 10, 12), 'canal', lista)
    ])
    redoOperations.clear()
    lista = rezultat

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is not None

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    assert len(lista) == 1
    assert getById('1', lista) is not None

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    assert len(lista) == 0

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    assert len(lista) == 0

    rezultat = adaugaCheltuiala('1', 1, 100, datetime.date(2021, 10, 10), 'canal', lista)
    undoOperations.append([
        lambda: stergeCheltuiala('1', lista),
        lambda: adaugaCheltuiala('1', 1, 100, datetime.date(2021, 10, 10), 'canal', lista)
    ])
    redoOperations.clear()
    lista = rezultat

    rezultat = adaugaCheltuiala('2', 1, 100, datetime.date(2021, 10, 11), 'canal', lista)
    undoOperations.append([
        lambda: stergeCheltuiala('2', lista),
        lambda: adaugaCheltuiala('2', 1, 100, datetime.date(2021, 10, 11), 'canal', lista)
    ])
    redoOperations.clear()
    lista = rezultat

    rezultat = adaugaCheltuiala('3', 1, 100, datetime.date(2021, 10, 12), 'canal', lista)
    undoOperations.append([
        lambda: stergeCheltuiala('3', lista),
        lambda: adaugaCheltuiala('3', 1, 100, datetime.date(2021, 10, 12), 'canal', lista)
    ])
    redoOperations.clear()
    lista = rezultat

    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()

    assert len(lista) == 3

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    assert len(lista) == 1
    assert getById('1', lista) is not None

    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()

    assert len(lista) == 2
    assert getById('2', lista) is not None

    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()

    assert len(lista) == 3
    assert getById('3', lista) is not None

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    assert len(lista) == 1
    assert getById('1', lista) is not None
    assert getById('2', lista) is None

    rezultat = adaugaCheltuiala('4', 1, 100, datetime.date(2021, 10, 14), 'canal', lista)
    undoOperations.append([
        lambda: stergeCheltuiala('4', lista),
        lambda: adaugaCheltuiala('4', 1, 100, datetime.date(2021, 10, 14), 'canal', lista)
    ])
    redoOperations.clear()
    lista = rezultat

    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()

    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('4', lista) is not None

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    assert len(lista) == 1
    assert getById('1', lista) is not None
    assert getById('4', lista) is None

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    assert len(lista) == 0
    assert getById('1', lista) is None

    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()

    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()

    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('4', lista) is not None

    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()

    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('4', lista) is not None
