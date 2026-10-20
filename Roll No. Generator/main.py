print("Welcome to Roll No. Generator")
n=str(input("Enter Student Name: "))
r=str(input("Enter Mobile Number without (country code): "))
d=str(input("Enter Date of Birth in DDMMYYYY Format: "))
y=str(input("Enter Admission Year: "))
a=y[2:]
b=r[8:10]
c=d[6:8]
e=n[0:2]
print(f"The Generated Roll Number is: {a}{b}{c}{e}")