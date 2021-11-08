from Domain.cheltuiala import getData, creeazaCheltuiala, getNrApartament, getSuma, getTip, getId


def adunaValoareCheltuieliDupaData(data, valoare, lista):
    '''
    Aduna o valoare data la toate cheltuielile dintr-o data.
    :param data: date
    :param valoare: float
    :param lista: lista de cheltuieli
    :return: lista noua in care la cheltuielile dintr-o data s-a adunat o valoare data
    '''
    if valoare < 0:
        raise ValueError('Valoarea de adunat trebuie sa fie un numar pozitiv!')
    listaNoua = []
    for cheltuiala in lista:
        if getData(cheltuiala) == data:
            cheltuialaNoua = creeazaCheltuiala(
                getId(cheltuiala),
                getNrApartament(cheltuiala),
                getSuma(cheltuiala) + valoare,
                getData(cheltuiala),
                getTip(cheltuiala)
            )
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua


def scadeValoareCheltuieliDupaData(data, valoare, lista):
    '''
    Scade o valoare data la toate cheltuielile dintr-o data.
    (Ajuta la operatia de Undo.)
    :param data: date
    :param valoare: float
    :param lista: lista de cheltuieli
    :return: lista noua in care la cheltuielile dintr-o data s-a scazut o valoare data
    '''
    if valoare < 0:
        raise ValueError('Valoarea de adunat trebuie sa fie un numar pozitiv!')
    listaNoua = []
    for cheltuiala in lista:
        if getData(cheltuiala) == data:
            cheltuialaNoua = creeazaCheltuiala(
                getId(cheltuiala),
                getNrApartament(cheltuiala),
                getSuma(cheltuiala) - valoare,
                getData(cheltuiala),
                getTip(cheltuiala)
            )
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua
