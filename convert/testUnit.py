import unittest
from get_valute import *

class TestStringMethods(unittest.TestCase):
    def test_getting_valute(self):
        responseCheck = requests.get(URL_CONST)
        valutesCheck = json.loads(responseCheck.text)
        k = get_valute()
        dollarCheck = valutesCheck['Valute']['USD']['Value']
        self.assertEqual(k[0], dollarCheck)
        euroCheck = valutesCheck['Valute']['EUR']['Value']
        self.assertEqual(k[3], euroCheck)
        belRubCheck = valutesCheck['Valute']['BYN']['Value']
        self.assertEqual(k[1], belRubCheck)
        grivCheck = valutesCheck['Valute']['UAH']['Value']
        self.assertEqual(k[2], grivCheck)

    def test_convert_rub(self):
        responseCheck = requests.get(URL_CONST)
        valutesCheck = json.loads(responseCheck.text)

        dollarCheck = valutesCheck['Valute']['USD']['Value']
        euroCheck = valutesCheck['Valute']['EUR']['Value']
        belRubCheck = valutesCheck['Valute']['BYN']['Value']
        grivCheck = valutesCheck['Valute']['UAH']['Value']
        rubles = 100
        string = "USD  " + str(round(rubles / dollarCheck, 2)) + '\n' + "BYN  " + str(round(rubles / belRubCheck, 2)) + '\n' + "UAH  " + str(round(rubles / grivCheck, 2)) + '\n' + "EUR  " + str(round(rubles / euroCheck, 2)) + '\n'
        valutes = get_valute()
        self.assertEqual(convert_rubles(rubles, valutes)[0], string)

    def test_conver_byn(self):
        responseCheck = requests.get(URL_CONST)
        valutesCheck = json.loads(responseCheck.text)

        dollarCheck = valutesCheck['Valute']['USD']['Value']
        euroCheck = valutesCheck['Valute']['EUR']['Value']
        belRubCheck = valutesCheck['Valute']['BYN']['Value']
        grivCheck = valutesCheck['Valute']['UAH']['Value']
        byn = 100
        string = "USD  " + str(round(belRubCheck * byn / dollarCheck, 2)) + '\n' + "EUR  " + str(round(belRubCheck * byn / euroCheck, 2)) + '\n' + "UAH  " + str(round(belRubCheck * byn / grivCheck, 2)) + '\n' + "RUB  " + str(round(belRubCheck * byn, 2)) + '\n'

        valutes = get_valute()
        self.assertEqual(convert_bel_rub(byn, valutes)[0], string)

    def test_convert_uah(self):
        responseCheck = requests.get(URL_CONST)
        valutesCheck = json.loads(responseCheck.text)

        dollarCheck = valutesCheck['Valute']['USD']['Value']
        euroCheck = valutesCheck['Valute']['EUR']['Value']
        belRubCheck = valutesCheck['Valute']['BYN']['Value']
        grivCheck = valutesCheck['Valute']['UAH']['Value']
        uah = 100
        string = "USD  " + str(round(uah * grivCheck / dollarCheck, 2)) + '\n' + "BYN  " + str(round(uah * grivCheck / belRubCheck, 2)) + '\n' + "EUR  " + str(round(uah * grivCheck / euroCheck, 2)) + '\n' + "RUB  " + str(round(uah * grivCheck, 2)) + '\n'

        valutes = get_valute()
        self.assertEqual(convert_uah(uah, valutes)[0], string)

    def test_convert_dollar(self):
        responseCheck = requests.get(URL_CONST)
        valutesCheck = json.loads(responseCheck.text)

        dollarCheck = valutesCheck['Valute']['USD']['Value']
        euroCheck = valutesCheck['Valute']['EUR']['Value']
        belRubCheck = valutesCheck['Valute']['BYN']['Value']
        grivCheck = valutesCheck['Valute']['UAH']['Value']
        dollar = 100
        string = "UAH  " + str(round(dollar * dollarCheck / grivCheck, 2)) + '\n' + "BYN  " + str(round(dollar * dollarCheck / belRubCheck, 2)) + '\n' + "EUR  " + str(round(dollar * dollarCheck / euroCheck, 2)) + '\n' + "RUB  " + str(round(dollar * dollarCheck, 2)) + '\n'

        valutes = get_valute()
        self.assertEqual(convert_dollar(dollar, valutes)[0], string)

    def test_convert_euro(self):
        responseCheck = requests.get(URL_CONST)
        valutesCheck = json.loads(responseCheck.text)

        dollarCheck = valutesCheck['Valute']['USD']['Value']
        euroCheck = valutesCheck['Valute']['EUR']['Value']
        belRubCheck = valutesCheck['Valute']['BYN']['Value']
        grivCheck = valutesCheck['Valute']['UAH']['Value']
        euro = 100
        string = "USD  " + str(round(euroCheck * euro / dollarCheck, 2)) + '\n' + "BYN  " + str(round(euroCheck * euro / belRubCheck, 2)) + '\n' + "UAH  " + str(round(euroCheck * euro / grivCheck, 2)) + '\n' +  "RUB  " + str(round(euroCheck * euro, 2)) + '\n'

        valutes = get_valute()
        self.assertEqual(convert_euro(euro, valutes)[0], string)


if __name__ == '__main__':
    unittest.main()

