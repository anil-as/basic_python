# Beginner Python Logic Building Questions

## 1. **Sum of Even Numbers**
Write a Python program that calculates the sum of all even numbers between 1 and 100.

### Example Input:
No input required.

### Example Output:
`2550`

```python
sum=0
for i in range(2,101,2):
    sum+=i
print("Sum of even numbers between 1 and 100 is ",sum)
```
---

## 2. **Reverse a String**
Write a Python function that takes a string as input and returns the string reversed.

### Example Input:
`"hello"`

### Example Output:
`"olleh"`

```python
word = input("Enter a string: ")
length = len(word)
new_word = "" 

for i in range(length - 1, -1, -1): 
    new_word += word[i] 

print("Reversed string:", new_word)
```
---

## 3. **Factorial of a Number**
Write a Python program that calculates the factorial of a number (n!). For example, the factorial of 5 is `5 * 4 * 3 * 2 * 1 = 120`.

### Example Input:
`5`

### Example Output:
`120`

```python
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter a number: "))
print(f"Factorial of number {n} is {fact(n)}")
```

---

## 4. **Check if a Number is Prime**
Write a Python function that checks if a given number is prime.

### Example Input:
`7`

### Example Output:
`True`

```python
import math

def prime(n):
    if n < 2: 
        return False

    for i in range(2, int(math.sqrt(n)) + 1):  
        if n % i == 0:
            return False
    
    return True

n = int(input("Enter a number: "))
print(prime(n))
```

---

## 5. **Count Vowels in a String**
Write a Python program that counts the number of vowels (a, e, i, o, u) in a given string.

### Example Input:
`"programming"`

### Example Output:
`3`

```python
string = input("Enter a string: ")  
temp = string.lower() 
count = 0  

while temp:    
    if temp[-1] in ['a', 'e', 'i', 'o', 'u']:  
        count += 1  
    temp = temp[:-1] 

print(count)  
```

---

## 6. **Fibonacci Series**
Write a Python program that prints the Fibonacci series up to the nth number, where n is provided by the user.

### Example Input:
`5`

### Example Output:
`0 1 1 2 3`

```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter number: "))
for i in range(n):  
    print(fib(i), end=' ')
```

---

## 7. **Find the Largest Number in a List**
Write a Python program that finds and prints the largest number from a given list of integers.

### Example Input:
`[10, 30, 25, 60, 12]`

### Example Output:
`60`

```python
n=[10, 30, 25, 60, 12]
max=n[0]
for i in n:
    if i>max:
        max=i
print(max)
```

---

## 8. **Check Palindrome**
Write a Python function that checks whether a given string is a palindrome (reads the same backward as forward).

### Example Input:
`"madam"`

### Example Output:
`True`

```python
word = input("Enter a string: ")  
length = len(word)
new_word = ""  

for i in range(length - 1, -1, -1):  
    new_word += word[i]  
if word == new_word:
    print(True) 
else:
    print(False)
```
---

## 9. **Multiplication Table**
Write a Python program that generates the multiplication table of a number up to 10.

### Example Input:
`4`

### Example Output:
```
    4 * 1 = 4 
    4 * 2 = 8 
    4 * 3 = 12 
    4 * 4 = 16 
    4 * 5 = 20 
    4 * 6 = 24 
    4 * 7 = 28 
    4 * 8 = 32 
    4 * 9 = 36 
    4 * 10 = 40
  ```

```python
n=int(input("Enter a number : "))
for i in range(1,10):
    print(f"{n} * {i} = ",(n*i))
```

---

## 10. **Count Digits in a Number**
Write a Python function that counts the number of digits in a given number.

### Example Input:
`12345`

### Example Output:
`5`
```python
n = int(input("Enter a number: "))  
print("Number of digits:", len(str(n)))  
```

---

## 11. **Sum of Digits**
Write a Python program that calculates the sum of the digits in a number.

### Example Input:
`1234`

### Example Output:
`10`

```python
n = int(input("Enter a number: "))  
print("Sum of digits:", sum(map(int, str(n))))
```

---

## 12. **Find the Second Largest Number**
Write a Python function that finds the second-largest number in a list of numbers.

### Example Input:
`[10, 20, 4, 45, 99]`

### Example Output:
`45`

---

## 13. **Convert Celsius to Fahrenheit**
Write a Python program that converts a temperature in Celsius to Fahrenheit.

### Example Input:
`25`

### Example Output:
`77.0`

---

## 14. **Check if a Number is Armstrong**
Write a Python function to check whether a number is an Armstrong number. An Armstrong number is one where the sum of the cubes of its digits equals the number itself (for a 3-digit number).

### Example Input:
`153`

### Example Output:
`True`

---

## 15. **Find the Common Elements in Two Lists**
Write a Python program that finds the common elements between two lists.

### Example Input:
`[1, 2, 3, 4]`  
`[3, 4, 5, 6]`

### Example Output:
`[3, 4]`

---

## 16. **Remove Duplicates from a List**
Write a Python program that removes all duplicate elements from a list and returns the list with unique elements only.

### Example Input:
`[1, 2, 2, 3, 4, 4, 5]`

### Example Output:
`[1, 2, 3, 4, 5]`

---

## 17. **Sum of Odd Numbers**
Write a Python program that calculates the sum of all odd numbers between 1 and 100.

### Example Input:
No input required.

### Example Output:
`2500`

---

## 18. **Check for Leap Year**
Write a Python function that checks if a given year is a leap year.

### Example Input:
`2024`

### Example Output:
`True`

---

## 19. **Count Words in a Sentence**
Write a Python program that counts the number of words in a given sentence.

### Example Input:
`"Python is fun"`

### Example Output:
`4`

---

## 20. **Create a Dictionary of Squares**
Write a Python program that creates a dictionary where the keys are numbers from 1 to 10 and the values are the squares of those numbers.

### Example Output:
```python
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25,
    6: 36,
    7: 49,
    8: 64,
    9: 81,
    10: 100
}
