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

        list = [1,10,11,12,13,14,15,16,17]
        input = 17
        expected = 10
        actual = prob4.num_occurences(list,input)
        self.assertEqual(expected,actual)


        list = [1,10,11,17]
        input = 17
        expected = 5
        actual = prob4.num_occurences(list,input)
        self.assertEqual(expected,actual)

        list = [1,10,11,12,13,14,15,16,17]
        input = 11
        expected = 4
        actual = prob4.num_occurences(list,input)
        self.assertEqual(expected,actual)

        
        list = [10,11,15,1,17,16,18,12,13,14]
        input = 17
        expected = 10
        actual = prob4.num_occurences(list,input)
        self.assertEqual(expected,actual)

        list = [17,17,17,17,17]
        input = 17
        expected = 5
        actual = prob4.num_occurences(list,input)
        self.assertEqual(expected,actual)

        list = [-1,-2,-3]
        input = 17
        expected = 0
        actual = prob4.num_occurences(list,input)
        self.assertEqual(expected,actual)

        list = [-1,-2,-3, 1]
        input = -2
        expected = 0
        actual = prob4.num_occurences(list,input)
        self.assertEqual(expected,actual)

        list = [-1,-2,-3, 11]
        input = 11
        expected = 2
        actual = prob4.num_occurences(list,input)
        self.assertEqual(expected,actual)

        list = [101,111,131,-111]
        input = 112
        expected = 5
        actual = prob4.num_occurences(list,input)
        self.assertEqual(expected,actual)

        list = [1001]
        input = 112
        expected = 0
        actual = prob4.num_occurences(list,input)
        self.assertEqual(expected,actual)

        list = [111111]
        input = 1000000
        expected = 6
        actual = prob4.num_occurences(list,input)
        self.assertEqual(expected,actual)
        


if __name__ == "__main__":
    unittest.main()