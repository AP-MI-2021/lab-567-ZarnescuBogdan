import datetime

from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala
from Logic.functionalitate1 import stergeToateCheltuielile
from Logic.functionalitate2 import adunaValoareCheltuieliDupaData


def printCommandList():
    print('Comenzile disponibile sunt: add; update; delete; deleteap; showall; exit.')


def printHelp():
    print('add - Adauga o cheltuiala noua.')
    print('update - Modifica o cheltuiala.')
    print('delete - Sterge o cheltuiala dupa Id.')
    print('deleteap - Sterge toate cheltuielile pentru un apartament.')
    print('showall - Afiseaza toate cheltuielile.')
    print('exit - Iese din meniul acesta.')


def stringToDate(dataAsString):
    try:
        dataAsList = dataAsString.split('-')
        year = int(dataAsList[0])
        month = int(dataAsList[1])
        day = int(dataAsList[2])
        return datetime.date(year, month, day)
    except ValueError as ve:
        print(f'Eroare: {ve}')
        return None


def runCommand(lista):
    while True:
        printCommandList()
        commandLine = input('Dati comanda(daca sunt mai multe comenzi, acestea trebuie separate prin ";" , '
                            'elementele prin ",", iar data este de forma: "year-month-day"): ')
        commandLine = commandLine.split(';')
        if commandLine[0] == 'exit':
            break
        for command in commandLine:
            command = command.split(',')
            if command[0] == 'add':
                if len(command) == 6:
                    try:
                        id = command[1]
                        nrApartament = int(command[2])
                        suma = float(command[3])
                        data = stringToDate(command[4])
                        if data is None:
                            raise ValueError('Data nu a fost introdusa corespunzator!')
                        tip = command[5]
                        lista = adaugaCheltuiala(id, nrApartament, suma, data, tip, lista)
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
                else:
                    print('Eroare: Nu ati introdus corect numarul de parametri ai cheltuielii!')
            elif command[0] == 'update':
                if len(command) == 6:
                    try:
                        id = command[1]
                        nrApartament = int(command[2])
                        suma = float(command[3])
                        data = stringToDate(command[4])
                        if data is None:
                            raise ValueError('Data nu a fost introdusa corespunzator!')
                        tip = command[5]
                        lista = modificaCheltuiala(id, nrApartament, suma, data, tip, lista)
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
            elif command[0] == 'delete':
                if len(command) == 2:
                    id = command[1]
                    lista = stergeCheltuiala(id, lista)
                else:
                    print('Eroare: Nu ati introdus corect comanda de stergere!')
            elif command[0] == 'deleteap':
                if len(command) == 2:
                    try:
                        nrApartament = int(command[1])
                        lista = stergeToateCheltuielile(nrApartament, lista)
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
            elif command[0] == 'addallfromdate':
                if len(command) == 3:
                    try:
                        data = stringToDate(command[1])
                        if data is None:
                            raise ValueError('Data nu a fost introdusa corespunzator!')
                        valoare = float(command[2])
                        lista = adunaValoareCheltuieliDupaData(data, valoare, lista)
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
            elif command[0] == 'showall':
                for cheltuiala in lista:
                    print(toString(cheltuiala))
            elif command[0] == 'help':
                printHelp()
            else:
                print('Comanda gresita! Reincercati!')
