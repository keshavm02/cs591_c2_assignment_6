"""
Problem 4 (Number of occurrences of the digit 1):
Given an integer n, count the total number of times the digit 1 appears in all non-negative integers that are less than or equal to n. You must use TDD to develop your solution.

Example:

Input: 17
Output: 10
Explanation: The digit 1 occurs a total of 10 times in: 1, 10, 11, 12, 13, 14, 15, 16, 17

"""
#assumption = list can not be empty
def num_occurences(list, number):
    list.sort()
    count = 0
    answer = 0
    while (count < len(list)) and (list[count] <= number): #Stop when we reach the end or when the next number is bigger than our input
        if list[count] <= 0: #skip all negative numbers and zero as well
            count += 1
            continue
        curr_num_digits = [digits for digits in str(list[count])] #split the current number we are on into a list of digits
        for digit in curr_num_digits:
            if digit == "1": 
                answer += 1
            else:
                continue
        count += 1
    return answer