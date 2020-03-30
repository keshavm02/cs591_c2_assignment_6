import unittest
from Problem3 import *


class MyTestCase(unittest.TestCase):
    def test_string_multiplication(self):
        output = multiplyStrings("0","0")
        expected = "0"
        self.assertEqual(output, expected)

        output = multiplyStrings("0","1")
        expected = "0"
        self.assertEqual(output, expected)

        output = multiplyStrings("2", "0")
        expected = "0"
        self.assertEqual(output, expected)

        output = multiplyStrings("1","1")
        expected = "1"
        self.assertEqual(output, expected)

        output = multiplyStrings("1", "7656789")
        expected = "7656789"
        self.assertEqual(output, expected)

        output = multiplyStrings("12435465768", "1")
        expected = "12435465768"
        self.assertEqual(output, expected)

        output = multiplyStrings("424", "25")
        expected = str(424*25)
        self.assertEqual(output,expected)

        output = multiplyStrings('29018437546','57468938')
        expected = str(29018437546*57468938)
        self.assertEqual(output,expected)




    def test_string_to_int(self):
        output = string_to_int('3')
        expected = int('3')
        self.assertEqual(output, expected)

        output = string_to_int('0')
        expected = int('0')
        self.assertEqual(output, expected)

        output = string_to_int('1234')
        expected = int('1234')
        self.assertEqual(output, expected)

        output = string_to_int('2143546576')
        expected = int('2143546576')
        self.assertEqual(output, expected)

        output = string_to_int('1000')
        expected = int('1000')
        self.assertEqual(output, expected)

        output = string_to_int('0001')
        expected = int('0001')
        self.assertEqual(output, expected)

    def test_int_to_string(self):
        output = int_to_string(7)
        expected = str(7)
        self.assertEqual(output, expected)

        output = int_to_string(2)
        expected = str(2)
        self.assertEqual(output, expected)

        output = int_to_string(8)
        expected = str(8)
        self.assertEqual(output, expected)

        output = int_to_string(237)
        #print(output)
        expected = str(237)
        self.assertEqual(output, expected)

        output = int_to_string(3386)
        #print(output)
        expected = str(3386)
        self.assertEqual(output, expected)

        output = int_to_string(9876543567)
        # print(output)
        expected = str(9876543567)

        output = int_to_string(00000000)
        # print(output)
        expected = str(00000000)
        self.assertEqual(output, expected)

        output = int_to_string(100000000)
        # print(output)
        expected = str(100000000)
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
