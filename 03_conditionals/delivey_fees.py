order_amount=int(input("Enter the order amount: "))
delivery_fees=0 if order_amount>300 else 30
"""Here we learn about ternary operators
"""
print(f"Delivery fees: {delivery_fees}")
