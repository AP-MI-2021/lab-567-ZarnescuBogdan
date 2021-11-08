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
    #return [id, nrApartament, suma, data, tip]
    return {
        'id': id,
        'nrApartament': nrApartament,
        'suma': suma,
        'data': data,
        'tip': tip
    }


def getId(cheltuiala):
    '''
    Da id-ul cheltuielii.
    :param cheltuiala: dictionar care reprezinta o cheltuiala
    :return: id-ul cheltuielii
    '''
    #return cheltuiala[0]
    return cheltuiala['id']


def getNrApartament(cheltuiala):
    '''
    Da nr. de apartament al cheltuielii.
    :param cheltuiala: dictionar care reprezinta o cheltuiala
    :return: nr. de apartament al cheltuielii
    '''
    #return cheltuiala[1]
    return cheltuiala['nrApartament']


def getSuma(cheltuiala):
    '''
    Da suma cheltuielii.
    :param cheltuiala: dictionar care reprezinta o cheltuiala
    :return: suma cheltuielii
    '''
    #return cheltuiala[2]
    return cheltuiala['suma']


def getData(cheltuiala):
    '''
    Da data cheltuielii.
    :param cheltuiala: dictionar care reprezinta o cheltuiala
    :return: data cheltuielii
    '''
    #return cheltuiala[3]
    return cheltuiala['data']


def getTip(cheltuiala):
    '''
    Da tipul cheltuielii.
    :param cheltuiala: dictionar care reprezinta o cheltuiala
    :return: tipul cheltuielii: intretinere, canal, alte cheltuieli
    '''
    # return cheltuiala[4]
    return cheltuiala['tip']


def toString(cheltuiala):
    return 'Id: {}, NrApartament: {}, Suma: {}, Data: {}, Tip: {}'.format(
        getId(cheltuiala),
        getNrApartament(cheltuiala),
        getSuma(cheltuiala),
        getData(cheltuiala),
        getTip(cheltuiala)
    )
