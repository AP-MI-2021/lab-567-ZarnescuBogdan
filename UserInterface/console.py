import datetime

from Domain.cheltuiala import toString, getNrApartament, getSuma, getData, getTip
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala, getById
from Logic.functionalitate1 import stergeToateCheltuielile, adaugaCheltuieli
from Logic.functionalitate2 import adunaValoareCheltuieliDupaData, scadeValoareCheltuieliDupaData
from Logic.functionalitate3 import celeMaiMariCheltuieli
from Logic.functionalitate4 import ordonareDescrescatorDupaSuma
from Logic.functionalitate5 import sumeLunarePerApartament


def printMenu():
    print('1. Adaugare cheltuiala.')
    print('2. Stergere cheltuiala.')
    print('3. Modificare cheltuiala.')
    print('4. Stergere cheltuieli pentru un apartament dat.')
    print('5. Adunare valoare data la toate cheltuielile dintr-o data.')
    print('6. Afisare cele mai mari cheltuieli pentru fiecare tip de cheltuiala.')
    print('7. Ordonare cheltuieli descrescator dupa suma.')
    print('8. Afisare sume lunare pentru fiecare apartament.')
    print('u. Undo.')
    print('r. Redo.')
    print('a. Afisare cheltuieli.')
    print('x. Iesire.')


def readDate():
    try:
        givenString = input('Dati data, cu elementele separate printr-o liniuta, de forma yyyy-mm-dd: ')
        numbersAsString = givenString.split('-')
        year = int(numbersAsString[0])
        month = int(numbersAsString[1])
        day = int(numbersAsString[2])
        return datetime.date(year, month, day)
    except ValueError as ve:
        print(f'Error: {ve}')
        return None


def uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect):
    try:
        if len(obiect) == 0:
            id = input('Dati id-ul: ')
            nrApartament = int(input('Dati nr. apartamentului: '))
            suma = float(input('Dati suma: '))
            data = readDate()
            if data is None:
                raise ValueError('Data nu a fost introdusa corespunzator!')
            tip = input('Dati tipul: ')
        else:
            id = obiect[0]
            nrApartament = int(obiect[1])
            suma = float(obiect[2])
            an = obiect[3].year
            luna = obiect[3].month
            zi = obiect[3].day
            data = datetime.date(an, luna, zi)
            tip = obiect[4]


        rezultat = adaugaCheltuiala(id, nrApartament, suma, data, tip, lista)
        undoOperations.append([
            lambda: stergeCheltuiala(id, rezultat),
            lambda: adaugaCheltuiala(id, nrApartament, suma, data, tip, lista)
        ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print(f'Error: {ve}')
        return lista


def uiStergeCheltuiala(lista, undoOperations, redoOperations, obiect):
    try:
        if len(obiect) == 0:
            id = input('Dati id-ul cheltuielii de sters: ')
        else:
            id = obiect[0]

        rezultat = stergeCheltuiala(id, lista)
        cheltuialaDeSters = getById(id, lista)
        undoOperations.append([
            lambda: adaugaCheltuiala(
                id,
                getNrApartament(cheltuialaDeSters),
                getSuma(cheltuialaDeSters),
                getData(cheltuialaDeSters),
                getTip(cheltuialaDeSters),
                rezultat
            ),
            lambda: stergeCheltuiala(id, lista)
        ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print(f'Error: {ve}')
        return lista


def uiModificaCheltuiala(lista, undoOperations, redoOperations, obiect):
    try:
        if len(obiect) == 0:
            id = input('Dati id-ul cheltuielii de modificat: ')
            nrApartament = int(input('Dati noul nr. de apartament: '))
            suma = float(input('Dati noua suma: '))
            data = readDate()
            if data is None:
                raise ValueError('Data nu a fost introdusa corespunzator!')
            tip = input('Dati noul tip: ')
        else:
            id = obiect[0]
            nrApartament = int(obiect[1])
            suma = float(obiect[2])
            an = obiect[3].year
            luna = obiect[3].month
            zi = obiect[3].day
            data = datetime.date(an, luna, zi)
            tip = obiect[4]

        rezultat = modificaCheltuiala(id, nrApartament, suma, data, tip, lista)
        cheltuialaVeche = getById(id, lista)
        undoOperations.append([
            lambda: modificaCheltuiala(
                id,
                getNrApartament(cheltuialaVeche),
                getSuma(cheltuialaVeche),
                getData(cheltuialaVeche),
                getTip(cheltuialaVeche),
                rezultat
            ),
            lambda: modificaCheltuiala(id, nrApartament, suma, data, tip, lista)
        ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print(f'Error: {ve}')
        return lista


def uiStergeToateCheltuielile(lista, undoOperations, redoOperations, obiect):
    try:
        if len(obiect) == 0:
            nrApartament = int(input('Dati nr. de apartament pentru care trebuie sterse toate cheltuielile: '))
        else:
            nrApartament = int(obiect[0])

        rezultat = stergeToateCheltuielile(nrApartament, lista)
        cheltuieliDeSters = []
        for cheltuiala in lista:
            if getNrApartament(cheltuiala) == nrApartament:
                cheltuieliDeSters.append(cheltuiala)
        undoOperations.append([
            lambda: adaugaCheltuieli(cheltuieliDeSters, rezultat),
            lambda: stergeToateCheltuielile(nrApartament, lista)
        ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print(f'Error: {ve}')
        return lista


def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiAdunaValoareCheltuieliDupaData(lista, undoOperations, redoOperations, obiect):
    try:
        if len(obiect) == 0:
            data = readDate()
            if data is None:
                raise ValueError('Data nu a fost introdusa corespunzator!')
            valoare = float(input(f'Dati valoarea care trebuie adunata la cheltuielile din data {data}: '))
        else:
            an = obiect[0].year
            luna = obiect[0].month
            zi = obiect[0].day
            data = datetime.date(an, luna, zi)
            valoare = obiect[1]

        rezultat = adunaValoareCheltuieliDupaData(data, valoare, lista)
        cheltuieliDeModificat = []
        for cheltuiala in lista:
            if getData(cheltuiala) == data:
                cheltuieliDeModificat.append(cheltuiala)
        undoOperations.append([
            lambda: scadeValoareCheltuieliDupaData(data, valoare, rezultat),
            lambda: adunaValoareCheltuieliDupaData(data, valoare, lista)
        ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print(f'Error: {ve}')
        return lista


def uiCeleMaiMariCheltuieli(lista):
    rezultat = celeMaiMariCheltuieli(lista)
    for tip in rezultat:
        print('Tipul {} are suma maxima {}'.format(tip, rezultat[tip]))


def uiOrdonareDescrescatorDupaSuma(lista):
    showAll(ordonareDescrescatorDupaSuma(lista))


def uiSumeLunarePerApartament(lista):
    rezultat = sumeLunarePerApartament(lista)
    for nrApartament in rezultat:
        for an in rezultat[nrApartament]:
            for luna in rezultat[nrApartament][an]:
                print('Apartamentul cu numarul {} are cheltuieli lunare in anul {}, luna {} in valoare de {}'.format(
                    nrApartament,
                    an,
                    luna,
                    rezultat[nrApartament][an][luna]))


def undo(lista, undoOperations, redoOperations):
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        print('Nu se poate face undo!')

    return lista


def redo(lista, undoOperations, redoOperations):
    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()
    else:
        print('Nu se poate face redo!')

    return lista


def runMenu(lista):
    undoOperations = []
    redoOperations = []
    obiect = []
    while True:
        printMenu()
        optiune = input('Dati optiunea: ')

        if optiune == '1':
            lista = uiAdaugaCheltuiala(lista, undoOperations, redoOperations, obiect)
        elif optiune == '2':
            lista = uiStergeCheltuiala(lista, undoOperations, redoOperations)
        elif optiune == '3':
            lista = uiModificaCheltuiala(lista, undoOperations, redoOperations)
        elif optiune == '4':
            lista = uiStergeToateCheltuielile(lista, undoOperations, redoOperations)
        elif optiune == '5':
            lista = uiAdunaValoareCheltuieliDupaData(lista, undoOperations, redoOperations)
        elif optiune == '6':
            uiCeleMaiMariCheltuieli(lista)
        elif optiune == '7':
            uiOrdonareDescrescatorDupaSuma(lista)
        elif optiune == '8':
            uiSumeLunarePerApartament(lista)
        elif optiune == 'u':
            lista = undo(lista, undoOperations, redoOperations)
        elif optiune == 'r':
            lista = redo(lista, undoOperations, redoOperations)
        elif optiune == 'a':
            showAll(lista)
        elif optiune == 'x':
            break
        else:
            print('Optiune gresita! Reincercati: ')
