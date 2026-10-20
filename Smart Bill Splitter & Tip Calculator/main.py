print ("Welcome to Smart Bill Splitter & Tip calculator")
n1 = int(input("Enter Bill Amount: "))
n2 = int(input("Enter Tip Percentage: "))
n3 = int(input("Enter number of people: "))
tip = n1*(n2/100)
total = n1 + tip
s = total/n3
print(f"Tip amount = ₹{tip}")
print(f"Total Amount= ₹{total}")
print(f"share per person = ₹{s}")