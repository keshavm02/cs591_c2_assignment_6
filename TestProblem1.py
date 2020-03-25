import unittest

class TestProblem1(unittest.TestCase):
    def __init__(self): pass
    
    def testProtocol(self):
        url = 'https://www.google.com/some-path'
        protocol = getProtocol(url)
        self.assertEqual(protocol, 'https')