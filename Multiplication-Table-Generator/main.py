print("="*64)
print("Welcome to the Multiplication Table Generator!")
print("="*64)
print()
n=int(input("Enter a number to generate its multiplication table: "))
table = []
for i in range(1,11):
    table.append(n*i)
print()
print(f"The multiplication table of {n} is:")
print(table)
print()
print("="*64)