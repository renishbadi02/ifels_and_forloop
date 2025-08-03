# ifels_and_forloop
 Python Program: Even/Odd Checker & Sum of Numbers from 1 to 50
This Python program does the following:

Takes a number from the user and checks if it's even or odd.

Calculates the sum of numbers from 1 to 50.

python
Copy
Edit
# Check if the number is even or odd
num = int(input("Enter your number: "))
if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

# Calculate the sum of numbers from 1 to 50
sum = 0
for i in range(1, 51):
    sum = sum + i
print(f"The sum of number from 1 to 50 : {sum}")
🧠 Sample Output
python
Copy
Edit
Enter your number: 7
7 is odd number
The sum of number from 1 to 50 : 1275
✅ Tip: Avoid using sum as a variable name, since it's a built-in function in Python 
