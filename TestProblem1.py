import unittest
from Problem1 import *

class TestProblem1(unittest.TestCase):
    def testProtocol(self):
        url = 'https://www.google.com/some-path'
        splitter = URL_Splitting(url)
        protocol = splitter.getProtocol()
        self.assertEqual(protocol, 'https')

if __name__ == "__main__":
    unittest.main()