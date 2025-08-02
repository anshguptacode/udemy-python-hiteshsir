balance=100000
withdrawals=[99999]
result = []
index = 0
while index < len(withdrawals):
    amount = withdrawals[index]
    if amount <= balance:
        balance -= amount
        result.append(f"Withdrawn: {amount}")
    else:
        result.append(f"Insufficient funds for requested amount: {amount}")
        index += 1
    result.append(f"Remaining Balance: {balance}")
print(f"{result}")