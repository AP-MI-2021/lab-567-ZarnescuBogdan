from Domain.cheltuiala import getNrApartament
from Logic.CRUD import getByNrApartament


def stergeToateCheltuielile(nrApartament, lista):
    '''
    Sterge toate cheltuielile pentru un apartament dat.
    :param nrApartament: int
    :param lista: lista de cheltuieli
    :return: lista in care cheltuielile apartamentului dat s-au sters
    '''
    if getByNrApartament(nrApartament, lista) is None:
        raise ValueError('Numarul apartamentului dat nu exista!')
    return [cheltuiala for cheltuiala in lista if getNrApartament(cheltuiala) != nrApartament]


def adaugaCheltuieli(cheltuieli, lista):
    '''
    Adauga inapoi toate cheltuielile care au fost sterse la operatia care sterge toate cheltuielile pentru un apartament dat.
    (Ajuta la operatia de Undo.)
    :param cheltuieli: lista cu cheltuielile care trebuie adaugate
    :param lista: lista de cheltuieli in care vom adauga cheltuielile care au fost sterse anterior.
    :return: lista in care cheltuielile apartamentului dat au fost adaugate inapoi
    '''
    rezultat = []
    for cheltuiala in lista:
        rezultat.append(cheltuiala)
    for cheltuialaDeAdaugat in cheltuieli:
        rezultat.append(cheltuialaDeAdaugat)
    return rezultat
