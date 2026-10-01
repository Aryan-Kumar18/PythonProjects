print("*"*50)
print("Welcome to Cabe Fare & Ride Split Calculator")
print("*"*50)

dist = float(input("Enter Distance in Kilometer: "))
base = float(input("Enter Base Fare in ₹: "))
rate = float(input("Enter rate per Kilometer in ₹: "))
surge = float(input("Enter surge multiplier (e.g. 1.2, 1.5): "))
riders = int(input("Number of passengers: "))

raw_fare = base + (dist * rate)
total_fare = raw_fare * surge
n = total_fare/riders

print("=" * 32)
print("    CAB RIDE RECEIPT")
print("=" * 32)

print(f"Total distance = {dist}")
print(f"Base fare = {base}")
print(f"Rate per Kilometer = {rate}")
print(f"surge = {surge}")
print(f"Number of passengers = {riders}")
print(f"Total fare = {total_fare}")
print(f"Each Riders pay = {n}")