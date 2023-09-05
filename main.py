import unittest




def umnojenie(a: int, b: int):
    if type(a) != int:
        return 'Error'
    return a * b


def plus(a: int, b: int):
    if type(a) != int:
        return 'Error'
    return a + b

def minus(a: int, b: int):
    if type(a) != int:
        return 'Error'
    return a - b


def devide(a: int, b: int):
    if type(a) != int:
        return 'Error'
    return a / b




class Test(unittest.TestCase):
    def test_umnojenie(self):
        self.assertEqual(umnojenie(12, 2), 24, 'Error(')

    def test_plus(self):
        self.assertEqual(plus(33, 77), 110, 'Wait what?')

    def test_minus(self):
        self.assertEqual(minus(33, 11), 22, 'Error?')


    def test_devide(self):
        self.assertEqual(devide(33, 11), 3, 'Error!')



