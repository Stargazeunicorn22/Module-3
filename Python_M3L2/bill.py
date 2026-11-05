def total_cal(t):
    bill = 50.00
    amount = bill * (t/100)
    total = bill + amount
    print(f"---Restaurant Bill ---")
    print(f"Base Bill:      ${bill:.2f}")
    print(f"-----------------------------")
    print(f"Total Paid : $ {total:.2f}")

a = total_cal(5)
print(a)