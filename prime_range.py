"""
Write a Python program that takes two numbers, start and end, and prints all prime numbers in that range.

Example:
  For start = 10, end = 30:
  11, 13, 17, 19, 23, 29
"""
start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))
for i in range(start, end + 1):
    flag = 0 
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            flag = 1 
            break
    if flag == 0:  
        print(i, end=" ") 
