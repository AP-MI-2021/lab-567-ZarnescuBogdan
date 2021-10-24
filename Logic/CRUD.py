from Domain.cheltuiala import creeazaCheltuiala, getNrApartament


def adaugaCheltuiala(nrApartament, suma, data, tip, lista):
    '''
    Adauga o cheltuiala intr-o lista.
    :param nrApartament: int
    :param suma: float
    :param data: date
    :param tip: string: intretinere, canal, alte cheltuieli
    :param lista: lista de cheltuieli
    :return: o lista continand atat elementele vechi, cat si noua cheltuiala
    '''
    cheltuiala = creeazaCheltuiala(nrApartament, suma, data, tip)
    return lista + [cheltuiala]


def getByNrApartament(nrApartament, lista):
    '''
    Gaseste o cheltuiala cu nr. apartamentului dat intr-o lista.
    :param nrApartament: int
    :param lista: lista de cheltuieli
    :return: cheltuiala cu nr. apartamentului dat din lista sau None, daca aceasta nu exista
    '''
    for cheltuiala in lista:
        if getNrApartament(cheltuiala) == nrApartament:
            return cheltuiala
    return None


def stergeCheltuiala(nrApartament, lista):
    '''
    Sterge o cheltuiala cu nr. apartamentului dat din lista.
    :param nrApartament: int
    :param lista: lista de cheltuieli
    :return: o lista de cheltuieli fara elementul cu nr. apartamentului dat
    '''
    return [cheltuiala for cheltuiala in lista if getNrApartament(cheltuiala) != nrApartament]


def modificaCheltuiala(nrApartament, suma, data, tip, lista):
    '''
    Modifica o cheltuiala cu nr. apartamentului dat.
    :param nrApartament: int
    :param suma: float
    :param data: date
    :param tip: string: intretinere, canal, alte cheltuieli
    :param lista: o lista de cheltuieli
    :return: lista modificata
    '''
    listaNoua = []
    for cheltuiala in lista:
        if getNrApartament(cheltuiala) == nrApartament:
            cheltuialaNoua = creeazaCheltuiala(nrApartament, suma, data, tip)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua
