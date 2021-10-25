def creeazaCheltuiala(nrApartament, suma, data, tip):
    '''
    Creeaza un dictionar care reprezinta o cheltuiala.
    :param nrApartament: int
    :param suma: float
    :param data: date
    :param tip: string
    :return: un dictionar care contine o cheltuiala
    '''
    return {
        'nrApartament': nrApartament,
        'suma': suma,
        'data': data,
        'tip': tip
    }


def getNrApartament(cheltuiala):
    '''
    Da nr. de apartament al cheltuielii.
    :param cheltuiala: dictionar care reprezinta o cheltuiala
    :return: nr. de apartament al cheltuielii
    '''
    return cheltuiala['nrApartament']


def getSuma(cheltuiala):
    '''
    Da suma cheltuielii.
    :param cheltuiala: dictionar care reprezinta o cheltuiala
    :return: suma cheltuielii.
    '''
    return cheltuiala['suma']


def getData(cheltuiala):
    '''
    Da data cheltuielii.
    :param cheltuiala: dictionar care reprezinta o cheltuiala
    :return: data cheltuielii
    '''
    return cheltuiala['data']


def getTip(cheltuiala):
    '''
    Da tipul cheltuielii.
    :param cheltuiala: dictionar care reprezinta o cheltuiala
    :return: tipul cheltuielii: intretinere, canal, alte cheltuieli
    '''
    return cheltuiala['tip']


def toString(cheltuiala):
    return 'NrApartament: {}, Suma: {}, Data: {}, Tip: {}'.format(
        getNrApartament(cheltuiala),
        getSuma(cheltuiala),
        getData(cheltuiala),
        getTip(cheltuiala)
    )
