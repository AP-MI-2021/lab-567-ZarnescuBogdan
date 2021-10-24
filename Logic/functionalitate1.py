from Domain.cheltuiala import getNrApartament


def stergeToateCheltuielile(nrApartament, lista):
    '''
    Sterge toate cheltuielile pentru un apartament dat.
    :param nrApartament: int
    :param lista: lista de cheltuieli
    :return: lista in care cheltuielile apartamentului dat s-au sters
    '''
    listaNoua = []
    for cheltuiala in lista:
        if getNrApartament(cheltuiala) != nrApartament:
            listaNoua.append(cheltuiala)
    return listaNoua