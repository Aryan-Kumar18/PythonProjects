print("="*64)
print("          Welcome to Credit Card Formatter & Masker")
print("="*64)
print("")
n=input("Enter Credit Card Number: ")
cn=n.strip()
cn=cn.replace("-","")
cn=cn.replace(" ","")
if cn.isdigit() == False:
    print("Invalid Credit Card Number. Please enter a valid number.")
elif (len(cn)!=16):
    print("Invalid Credit Card Number. Please enter a 16-digit number.")
else:
    if cn.startswith("4"):
        network="Visa"
    elif cn[:2]=="51" or cn[:2]=="52" or cn[:2]=="53" or cn[:2]=="54" or cn[:2]=="55":
        network="MasterCard"
    elif cn.startswith("37"):
        network="American Express"
    else:
        network="Unknown"
lf=cn[-4:]
mcn="****-****-****-"+lf
print("-"*64)
print(f"Card Network: {network}")
print(f"Masked Number: {mcn}")
print("-"*64)
print("")
print("="*64)