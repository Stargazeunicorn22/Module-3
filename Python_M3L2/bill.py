def total_cal(bill, tip_percentage):
    tip_amount = bill * (tip_percentage / 100)
    total_amount = bill + tip_amount
    
    print(f"--- Restaurant Bill ---")
    print(f"Base Bill:   ${bill:.2f}")
    print(f"Tip ({tip_percentage}%): ${tip_amount:.2f}")
    print(f"-----------------------")
    print(f"Total Paid:  ${total_amount:.2f}")

total_cal(65.50, 18)
