from Domain.cheltuiala import creeazaCheltuiala, getNrApartament, getId


def adaugaCheltuiala(id, nrApartament, suma, data, tip, lista):
    '''
    Adauga o cheltuiala intr-o lista.
    :param id: string
    :param nrApartament: int
    :param suma: float
    :param data: date
    :param tip: string: intretinere, canal, alte cheltuieli
    :param lista: lista de cheltuieli
    :return: o lista continand atat elementele vechi, cat si noua cheltuiala
    '''
    if getById(id, lista) is not None:
        raise ValueError('Id-ul exista deja!')
    cheltuiala = creeazaCheltuiala(id, nrApartament, suma, data, tip)
    return lista + [cheltuiala]


def getById(id, lista):
    '''
    Gaseste o cheltuiala cu id-ul dat intr-o lista.
    :param id: string
    :param lista: lista de cheltuieli
    :return: cheltuiala cu id-ul dat din lista sau None, daca aceasta nu exista
    '''
    for cheltuiala in lista:
        if getId(cheltuiala) == id:
            return cheltuiala
    return None


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


def stergeCheltuiala(id, lista):
    '''
    Sterge o cheltuiala cu nr. apartamentului dat din lista.
    :param id: string
    :param lista: lista de cheltuieli
    :return: o lista de cheltuieli fara elementul cu nr. apartamentului dat
    '''
    if getById(id, lista) is None:
        raise ValueError('Id-ul dat nu exista!')
    return [cheltuiala for cheltuiala in lista if getId(cheltuiala) != id]


def modificaCheltuiala(id, nrApartament, suma, data, tip, lista):
    '''
    Modifica o cheltuiala cu id-ul dat.
    :param id: string
    :param nrApartament: int
    :param suma: float
    :param data: date
    :param tip: string: intretinere, canal, alte cheltuieli
    :param lista: o lista de cheltuieli
    :return: lista modificata
    '''
    if getById(id, lista) is None:
        raise ValueError('Id-ul dat nu exista!')
    listaNoua = []
    for cheltuiala in lista:
        if getId(cheltuiala) == id:
            cheltuialaNoua = creeazaCheltuiala(id, nrApartament, suma, data, tip)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua
