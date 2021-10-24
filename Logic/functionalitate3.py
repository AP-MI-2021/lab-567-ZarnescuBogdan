from Domain.cheltuiala import getSuma, creeazaCheltuiala, getNrApartament, getData, getTip


def celeMaiMariCheltuieli(lista):
    '''
    Determina cele mai mari cheltuieli pentru fiecare tip de cheltuiala.
    :param lista: lista de cheltuieli
    :return: o lista noua in care sunt puse cele mai mari cheltuieli pentru fiecare tip de cheltuiala
    '''
    listaCheltuieliMaxime = []
    maxIntretinere = -1
    maxCanal = -1
    maxAlteCheltuieli = -1
    for cheltuiala in lista:
        if getTip(cheltuiala) == 'intretinere' and getSuma(cheltuiala) > maxIntretinere:
            maxIntretinere = getSuma(cheltuiala)
        elif getTip(cheltuiala) == 'canal' and getSuma(cheltuiala) > maxCanal:
            maxCanal = getSuma(cheltuiala)
        elif getTip(cheltuiala) == 'alte cheltuieli' and getSuma(cheltuiala) > maxAlteCheltuieli:
            maxAlteCheltuieli = getSuma(cheltuiala)
    for cheltuiala in lista:
        if getTip(cheltuiala) == 'intretinere' and getSuma(cheltuiala) == maxIntretinere:
            cheltuialaMaxIntretinere = creeazaCheltuiala(
                getNrApartament(cheltuiala),
                getSuma(cheltuiala),
                getData(cheltuiala),
                getTip(cheltuiala)
            )
            listaCheltuieliMaxime.append(cheltuialaMaxIntretinere)
            break
    for cheltuiala in lista:
        if getTip(cheltuiala) == 'canal' and getSuma(cheltuiala) == maxCanal:
            cheltuialaMaxCanal = creeazaCheltuiala(
                getNrApartament(cheltuiala),
                getSuma(cheltuiala),
                getData(cheltuiala),
                getTip(cheltuiala)
            )
            listaCheltuieliMaxime.append(cheltuialaMaxCanal)
            break
    for cheltuiala in lista:
        if getTip(cheltuiala) == 'alte cheltuieli' and getSuma(cheltuiala) == maxAlteCheltuieli:
            cheltuialaMaxAlteCheltuieli = creeazaCheltuiala(
                getNrApartament(cheltuiala),
                getSuma(cheltuiala),
                getData(cheltuiala),
                getTip(cheltuiala)
            )
            listaCheltuieliMaxime.append(cheltuialaMaxAlteCheltuieli)
            break
    return listaCheltuieliMaxime
