print("="*65)
print("      Welcome to the Factors, Multiples, and Digit Counter Program!")
print("="*65)
n=int(input("Enter a positive number: "))
print("")
if n<=0:
    print("Enter a number greater than 0")
else:
    print(f"The factors of {n} are: ", )
    for i in range (1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()
    print("")

    print(f"The multiples of {n} up to 1000 are: ",)
    for i in range(1 , 1001):
        if i % n == 0:
            print(i, end=" ")
    print()
    print("")
    print(f"Total number of digits in {n} is: ", len(str(n)))