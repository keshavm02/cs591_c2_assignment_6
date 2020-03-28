import unittest
import prob4


"""
Problem 4 (Number of occurrences of the digit 1):
Given an integer n, count the total number of times the digit 1 appears in all non-negative integers that are less than or equal to n. You must use TDD to develop your solution.

Example:

Input: 17
Output: 10
Explanation: The digit 1 occurs a total of 10 times in: 1, 10, 11, 12, 13, 14, 15, 16, 17

"""

class test_problem4(unittest.TestCase):
    
    def test_num_occurences(self):
        input = 17
        expected = 10
        actual = prob4.num_occurences(input)
        self.assertEqual(expected,actual)

        input = 18
        expected = 11
        actual = prob4.num_occurences(input)
        self.assertEqual(expected,actual)

        input = 11
        expected = 4
        actual = prob4.num_occurences(input)
        self.assertEqual(expected,actual)

        input = 0
        expected = 0
        actual = prob4.num_occurences(input)
        self.assertEqual(expected,actual)

        input= -10
        expected = 0
        actual = prob4.num_occurences(input)
        self.assertEqual(expected,actual)

        
        input = 2
        expected = 1
        actual = prob4.num_occurences(input)
        self.assertEqual(expected,actual)

        input = 100
        expected = 21
        actual = prob4.num_occurences(input)
        self.assertEqual(expected,actual)


        input = 1000
        expected = 301
        actual = prob4.num_occurences(input)
        self.assertEqual(expected,actual)


if __name__ == "__main__":
    unittest.main()