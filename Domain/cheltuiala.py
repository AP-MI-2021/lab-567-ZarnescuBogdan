def creeazaCheltuiala(id, nrApartament, suma, data, tip):
    '''
    Creeaza un dictionar care reprezinta o cheltuiala.
    :param id: string
    :param nrApartament: int
    :param suma: float
    :param data: date
    :param tip: string
    :return: un dictionar care contine o cheltuiala
    '''
    '''return {
        'id': id,
        'nrApartament': nrApartament,
        'suma': suma,
        'data': data,
        'tip': tip
    }'''
    return [id, nrApartament, suma, data, tip]


def getId(cheltuiala):
    '''
    Da id-ul cheltuielii.
    :param cheltuiala: dictionar care reprezinta o cheltuiala
    :return: id-ul cheltuielii
    '''
    # return cheltuiala['id']
    return cheltuiala[0]


def getNrApartament(cheltuiala):
    '''
    Da nr. de apartament al cheltuielii.
    :param cheltuiala: dictionar care reprezinta o cheltuiala
    :return: nr. de apartament al cheltuielii
    '''
    # return cheltuiala['nrApartament']
    return cheltuiala[1]


def getSuma(cheltuiala):
    '''
    Da suma cheltuielii.
    :param cheltuiala: dictionar care reprezinta o cheltuiala
    :return: suma cheltuielii
    '''
    # return cheltuiala['suma']
    return cheltuiala[2]


def getData(cheltuiala):
    '''
    Da data cheltuielii.
    :param cheltuiala: dictionar care reprezinta o cheltuiala
    :return: data cheltuielii
    '''
    # return cheltuiala['data']
    return cheltuiala[3]


def getTip(cheltuiala):
    '''
    Da tipul cheltuielii.
    :param cheltuiala: dictionar care reprezinta o cheltuiala
    :return: tipul cheltuielii: intretinere, canal, alte cheltuieli
    '''
    # return cheltuiala['tip']
    return cheltuiala[4]


def toString(cheltuiala):
    return 'Id: {}, NrApartament: {}, Suma: {}, Data: {}, Tip: {}'.format(
        getId(cheltuiala),
        getNrApartament(cheltuiala),
        getSuma(cheltuiala),
        getData(cheltuiala),
        getTip(cheltuiala)
    )
