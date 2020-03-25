import unittest

class TestProblem1(unittest.TestCase):
    def __init__(): pass
    
    def testProtocol():
        url = 'https://www.google.com/some-path'
        protocol = getProtocol(url)
        assertEquals(protocol, 'https')