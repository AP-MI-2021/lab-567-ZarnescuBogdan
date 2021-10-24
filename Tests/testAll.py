from Tests.testCRUD import testAdaugaCheltuiala, testStergeCheltuiala, testModificaCheltuiala
from Tests.testDomain import testCheltuiala
from Tests.testFunctionalitati import testStergeToateCheltuielile


def runAllTests():
    testCheltuiala()
    testAdaugaCheltuiala()
    testStergeCheltuiala()
    testModificaCheltuiala()
    testStergeToateCheltuielile()