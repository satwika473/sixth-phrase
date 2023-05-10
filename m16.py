net_amount = 0

while True:
    transaction = input("Enter transaction (D/W amount), or 'done' to finish: ")
    if transaction == 'done':
        break
    trans_type, amount = transaction.split()
    amount = int(amount)
    if trans_type == 'D':
        net_amount += amount
    elif trans_type == 'W':
        net_amount -= amount

print("Net amount:", net_amount)
