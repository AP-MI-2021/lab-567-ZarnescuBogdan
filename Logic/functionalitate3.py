from Domain.cheltuiala import getSuma, getTip


def celeMaiMariCheltuieli(lista):
    '''
    Determina cele mai mari cheltuieli pentru fiecare tip de cheltuiala.
    :param lista: lista de cheltuieli
    :return: cele mai mari cheltuieli pentru fiecare tip de cheltuiala
    '''
    rezultat = {}
    for cheltuiala in lista:
        tip = getTip(cheltuiala)
        suma = getSuma(cheltuiala)
        if tip in rezultat:
            if suma > rezultat[tip]:
                rezultat[tip] = suma
        else:
            rezultat[tip] = suma
    return rezultat
