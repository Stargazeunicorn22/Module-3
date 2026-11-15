def calculate_change(bill_amount, amount_paid):
    change = amount_paid - bill_amount
    return change


total_bill = 2.50
paid = 4.00

money_returned = calculate_change(total_bill, paid)

print(f"The shopkeeper should return: ${money_returned:.2f}")