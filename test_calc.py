import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEquals(calc.add(10, 5), 15)
        self.assertEquals(calc.add(1, -1), 0)
        self.assertEquals(calc.add(-1, -1), -2)

    def test_sub(self):
        self.assertEquals(calc.sub(10, 5), 5)
        self.assertEquals(calc.sub(-1, 1), -2)
        self.assertEquals(calc.sub(-1, -1), 0)

    def test_multi(self):
        self.assertEquals(calc.multi(10, 5), 50)
        self.assertEquals(calc.multi(1, -1), -1)
        self.assertEquals(calc.multi(-1, -1), 1)

    def test_div(self):
        self.assertEquals(calc.div(10, 5), 2)
        self.assertEquals(calc.div(1, -1), -1)
        self.assertEquals(calc.div(-1, -1), 1)
        self.assertRaises(ValueError, calc.div, 10, 0)

if __name__ == '__main__':
    unittest.main()