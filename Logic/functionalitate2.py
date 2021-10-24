from Domain.cheltuiala import getData, creeazaCheltuiala, getNrApartament, getSuma, getTip


def adunaValoareCheltuieliDupaData(data, valoare, lista):
    '''
    Aduna o valoare data la toate cheltuielile dintr-o data.
    :param data: date
    :param valoare: float
    :param lista: lista de cheltuieli
    :return: lista noua in care la cheltuielile dintr-o data s-a adunat o valoare data
    '''
    listaNoua = []
    for cheltuiala in lista:
        if getData(cheltuiala) == data:
            cheltuialaNoua = creeazaCheltuiala(
                getNrApartament(cheltuiala),
                getSuma(cheltuiala) + valoare,
                getData(cheltuiala),
                getTip(cheltuiala)
            )
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua
