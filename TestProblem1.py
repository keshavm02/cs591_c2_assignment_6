import unittest

class TestProblem1(unittest.TestCase):
    def testProtocol(self):
        url = 'https://www.google.com/some-path'
        protocol = getProtocol(url)
        self.assertEqual(protocol, 'https')

if __name__ == "__main__":
    unittest.main()