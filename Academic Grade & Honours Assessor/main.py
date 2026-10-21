print("="*64)
print("            Welcome to Academic Grade & Honours Assessor")
print("="*64)
m1=float(input("Enter Subject 1 Marks: "))
m2=float(input("Enter Subject 2 Marks: "))
m3=float(input("Enter Subject 3 Marks: "))
avg=(m1+m2+m3)/3
if (m1<0 or m1>100 or m2<0 or m2>100 or m3<0 or m3>100):
    print("Invalid Marks entered. Please enter marks between 0 and 100.")
elif (m1<40 or m2<40 or m3<40):
    print("Grade: U - Failed (Backlog detected in one or more subjects)")
elif (avg>=90):
    if(m1>=75 and m2>=75 and m3>=75):
        print("Grade: A+ - Passed with Academic Distinction")
    else: print("Grade: A+ - Passed")
elif (avg>=80 and avg<90):
    print("Passed with Grade: A")
elif (avg>=70 and avg<80):
    print("Passed with Grade: B")
elif (avg>=60 and avg<70):
    print("Passed with Grade: C")
elif (avg>=50 and avg<60):
    print("Passed with Grade: D")
elif (avg>=40 and avg<50):
    print("Passed with Grade: E")
else:
    print("Grade: U - Failed")
print("="*64)
