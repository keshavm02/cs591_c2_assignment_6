"""
Problem 4 (Number of occurrences of the digit 1):
Given an integer n, count the total number of times the digit 1 appears in all non-negative integers that are less than or equal to n. You must use TDD to develop your solution.

Example:

Input: 17
Output: 10
Explanation: The digit 1 occurs a total of 10 times in: 1, 10, 11, 12, 13, 14, 15, 16, 17

"""
def num_occurences(number):
    answer = 0
    if number <= 0: #skip if number is negative to 0
        return answer
    else:
        all_digits = ""
        for x in range(number+1): #for all numbers starting from 0 up to the inputed number, concatenate it and make it a huge string
            all_digits += str(x)
        num_digits = [digits for digits in all_digits] #now seperate that stringed number into a list of digits
        for digit in num_digits: #go through list and count the 1's
            if digit == "1": 
                answer += 1
            else:
                continue
        return answer
