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
