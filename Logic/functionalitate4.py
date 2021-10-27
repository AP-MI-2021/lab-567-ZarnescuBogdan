from Domain.cheltuiala import getSuma


def ordonareDescrescatorDupaSuma(lista):
    '''
    Ordoneaza cheltuielile descrescator dupa suma.
    :param lista: lista de cheltuieli
    :return: cheltuielile ordonate descrescator dupa suma
    '''
    return sorted(lista, key=lambda cheltuiala: getSuma(cheltuiala), reverse=True)
