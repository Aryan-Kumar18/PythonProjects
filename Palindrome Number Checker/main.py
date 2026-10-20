print(100*"=")
print("                 Weclome to Palindrome Number Checker")
print(100*"=")
n=int(input("Enter any number: "))
t=str(n)
r=t[::-1]
if(t==r):
    print("It is a Palindrome Number")
else:
    print("It is not a Palindrome Number")
