import datetime

from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala


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
        commandLine = input('Dati comanda(trebuie separate prin ";" , elementele prin ",", iar data este de forma: "year-month-day"): ')
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
            elif command[0] == 'showall':
                for cheltuiala in lista:
                    print(toString(cheltuiala))
            elif command[0] == 'delete':
                if len(command) == 2:
                    id = command[1]
                    lista = stergeCheltuiala(id, lista)
                else:
                    print('Eroare: Nu ati introdus corect comanda de stergere!')
            else:
                print('Comanda gresita! Reincercati!')
