print("Welcome to Loan Simple Interest & EMI Estimator")
principal = float(input("Enter Loan Principal (₹): "))
annual_rate = float(input("Enter Annual Interest Rate %: "))
years = int(input("Enter Tenure (in years): "))

# Simple Interest Formula: (P * R * T) / 100
total_interest = (principal * annual_rate * years) / 100
total_repayment = principal + total_interest
total_months = years * 12
monthly_installment = total_repayment / total_months

print("\n" + "#" * 32)
print("     LOAN SUMMARY REPORT")
print("#" * 32)
print(f"Borrowed Amount:    ₹{principal:,.2f}")
print(f"Total Interest:     ₹{total_interest:,.2f}")
print(f"Gross Repayable:    ₹{total_repayment:,.2f}")
print(f"Monthly Cost:       ₹{monthly_installment:,.2f} ({total_months} months)")
print("-" * 32)
print(f"Interest > 20% of Loan? {total_interest > (principal * 0.20)}")
print("#" * 32)