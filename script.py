num = int(input("Enter your number:-"))
if num%2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")


sum = 0
for i in range(1,51):
    sum = sum + i
print(f"The sum of number from 1 to 50 :{sum}")
