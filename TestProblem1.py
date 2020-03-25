import unittest
from Problem1 import *

class TestProblem1(unittest.TestCase):
    def testProtocol(self):
        url = 'https://www.google.com/some-path'
        splitter = URL_Splitting(url)
        protocol = splitter.getProtocol()
        self.assertEqual(protocol, 'https')

        url = 'ftp://bu.edu/'
        splitter = URL_Splitting(url)
        protocol = splitter.getProtocol()
        self.assertEqual(protocol, 'ftp')

        url = 'http://www.facebook.com/home.php/'
        splitter = URL_Splitting(url)
        protocol = splitter.getProtocol()
        self.assertEqual(protocol, 'http')

        url = 'https://docs.python.org/3/'
        splitter = URL_Splitting(url)
        protocol = splitter.getProtocol()
        self.assertEqual(protocol, 'https')

    def testDomain(self):
        url = 'https://www.google.com/some-path'
        splitter = URL_Splitting(url)
        domain = splitter.getDomain()
        self.assertEqual(domain, 'www.google.com')

        url = 'ftp://bu.edu/'
        splitter = URL_Splitting(url)
        domain = splitter.getDomain()
        self.assertEqual(domain, 'bu.edu')

        url = 'http://www.facebook.com/home.php/'
        splitter = URL_Splitting(url)
        domain = splitter.getDomain()
        self.assertEqual(domain, 'www.facebook.com')

        url = 'https://docs.python.org/3/'
        splitter = URL_Splitting(url)
        domain = splitter.getDomain()
        self.assertEqual(domain, 'docs.python.org')

    def testPath(self):
        url = 'https://www.google.com/some-path'
        splitter = URL_Splitting(url)
        path = splitter.getPath()
        self.assertEqual(path, 'some-path')

        url = 'ftp://bu.edu/'
        splitter = URL_Splitting(url)
        path = splitter.getPath()
        self.assertEqual(path, '')

        url = 'http://www.facebook.com/home.php/'
        splitter = URL_Splitting(url)
        path = splitter.getPath()
        self.assertEqual(path, 'home.php')

        url = 'https://docs.python.org/3/'
        splitter = URL_Splitting(url)
        path = splitter.getPath()
        self.assertEqual(path, '3')

if __name__ == "__main__":
    unittest.main()