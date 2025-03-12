"""
Problem Explanation:

You are given an array that contains n-1 distinct numbers. These numbers are chosen from the range 1 to n, where 
n is the total number of elements you expect. Since there is one missing number, the array contains every number 
from the range except one.

For example, if n = 6, the complete set of numbers would be: [1, 2, 3, 4, 5, 6]
If the array contains the numbers: [1, 2, 3, 5, 6]
Then the missing number is 4.

"""
array = [1, 2, 3, 4, 5]
n = 6 
for i in range(1, n + 1):  
    count = 0
    for j in array: 
        if i == j:
            count += 1 
    if count == 0:
        print("Missing element is:", i)
        break 
