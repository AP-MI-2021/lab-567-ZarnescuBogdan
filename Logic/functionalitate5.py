from Domain.cheltuiala import getNrApartament, getSuma, getData


def sumeLunarePerApartament(lista):
    '''
    Determina suma lunara pentru fiecare apartament.
    :param lista: lista de cheltuieli
    :return: suma lunara pentru fiecare apartament
    '''
    rezultat = {}
    for cheltuiala in lista:
        nrApartament = getNrApartament(cheltuiala)
        suma = getSuma(cheltuiala)
        data = getData(cheltuiala)
        an = data.year
        luna = data.month
        if nrApartament in rezultat:
            if an in rezultat[nrApartament]:
                if luna in rezultat[nrApartament][an]:
                    rezultat[nrApartament][an][luna] += suma
                else:
                    rezultat[nrApartament][an][luna] = suma
            else:
                rezultat[nrApartament][an] = {luna: suma}
        else:
            rezultat[nrApartament] = {an: {luna: suma}}
    return rezultat
