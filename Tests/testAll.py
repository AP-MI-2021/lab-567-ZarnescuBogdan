from Tests.testCRUD import testAdaugaCheltuiala, testStergeCheltuiala, testModificaCheltuiala, testGetByNrApartament
from Tests.testDomain import testCheltuiala
from Tests.testFunctionalitati import testStergeToateCheltuielile, testAdunaValoareCheltuieliDupaData, \
    testCeleMaiMariCheltuieli, testOrdonareDescrescatorDupaSuma, testSumeLunarePerApartament
from Tests.testUndoRedo import testUndoRedo


def runAllTests():
    testCheltuiala()
    testAdaugaCheltuiala()
    testGetByNrApartament()
    testStergeCheltuiala()
    testModificaCheltuiala()
    testStergeToateCheltuielile()
    testAdunaValoareCheltuieliDupaData()
    testCeleMaiMariCheltuieli()
    testOrdonareDescrescatorDupaSuma()
    testSumeLunarePerApartament()
    testSumeLunarePerApartament()
    testUndoRedo()
