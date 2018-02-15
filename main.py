import unittest as unit


# translate symbol in numeric
def translate_symbol(upper, middle, lower, val):
    val_str = ''

    if val == 9:
        val_str = lower + upper
        val -= 9

    if val >= 5:
        val_str = middle
        val -= 5

    if val == 4:
        val_str = lower + middle
        val -= 4

    while val > 0:
        val_str += lower
        val -= 1

    return val_str


# translate number into numeric
def translate(num):
    numeric = ''
    if num <= 0:
        return 'There is no numeral for this number'

    else:
        for x in range(num // 1000):
            numeric += 'M'

        numeric += translate_symbol('M', 'D', 'C', (num % 1000) // 100)
        numeric += translate_symbol('C', 'L', 'X', (num % 100) // 10)
        numeric += translate_symbol('X', 'V', 'I', num % 10)

        return numeric


# main function that returns solution
def answer(number=None):
    try:
        if number == None:
            number = int(input())
        else:
            number = int(number)

    except Exception as error:
        return 'This is not a number'

    else:
        return translate(number)


# unit-tests
class MyTests(unit.TestCase):

    def test_letters(self):
        ans = answer('some_letters')
        self.assertEqual(ans, 'This is not a number')

    def test_minus(self):
        ans = answer(-5)
        self.assertEqual(ans, 'There is no numeral for this number')

    def test_zero(self):
        ans = answer(0)
        self.assertEqual(ans, 'There is no numeral for this number')

    def test_num1(self):
        ans = answer(1990)
        self.assertEqual(ans, 'MCMXC')

    def test_num2(self):
        ans = answer(2008)
        self.assertEqual(ans, 'MMVIII')

    def test_num3(self):
        ans = answer(900)
        self.assertEqual(ans, 'CM')

    def test_num4(self):
        ans = answer(4)
        self.assertEqual(ans, 'IV')

    def test_num5(self):
        ans = answer(2)
        self.assertEqual(ans, 'II')

    def test_num6(self):
        ans = answer(8)
        self.assertEqual(ans, 'VIII')

    def test_num7(self):
        ans = answer(31)
        self.assertEqual(ans, 'XXXI')


# launching unit-tests
unit.main()
