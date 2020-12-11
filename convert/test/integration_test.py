import unittest
from get_valute import *

class IntegrationTest(unittest.TestCase):
    def test_not_digit_data(self):
        rub = 'abc'
        valute = get_valute()
        self.assertEqual(convert_rubles(rub, valute)[0], "Это должно быть положительное число")
        self.assertEqual(convert_rubles(rub, valute)[1], 0)
        rub ="1136361a"
        self.assertEqual(convert_rubles(rub, valute)[0], "Это должно быть положительное число")
        self.assertEqual(convert_rubles(rub, valute)[1], 0)

    def test_not_positive_number(self):
        rub = -10
        valute = get_valute()
        self.assertEqual(convert_rubles(rub, valute)[0], "Вы не можете вводить неположительное число")
        self.assertEqual(convert_rubles(rub, valute)[1], 0)
        rub = 0
        self.assertEqual(convert_rubles(rub, valute)[0], "Вы не можете вводить неположительное число")
        self.assertEqual(convert_rubles(rub, valute)[1], 0)

if __name__ == '__main__':
    unittest.main()
