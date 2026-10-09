print("="*50)
print("Welcome to Simple Calculator")
print("="*50)
print("")
n1=float(input("Enter 1st Number:- "))
n2=float(input("Enter 2nd Number:- "))
print("")
c=int(input("Enter 1 for Addition \nEnter 2 for Subtraction \nEnter 3 for Multiplication \nEnter 4 for Division \nEnter 5 for Exponentiation \n \n"))
print("")
if(c==1):
    s=n1+n2
    print("Addition= ",s)
elif(c==2):
    s=n1-n2
    print("subtraction= ",s)
elif (c==3):
    s=n1*n2
    print("Multiplication= ",s)
elif (c==4):
    s=n1/n2
    print("Division= ",s)
elif (c==5):
    s=n1**n2
    print("Exponentiation= ",s)
else:
    print("Invalid Choice")
print("="*50)