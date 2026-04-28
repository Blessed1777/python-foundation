amount = int(input("Enter the amount you want to withdraw: "))
balance = 0
network = True

if not network:
    print("Service temporary unavailable")
elif balance <= 0:
    print("Invalid account balance")
elif amount <= balance:
    print("Payment successful")
elif amount > balance:
    print("Insufficient funds")

else:
    print("Payment failed")