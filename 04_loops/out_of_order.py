flavours=["Ginger", "out of stock", "lemon","discontinued","tulsi"]

for flavour in flavours:
    if flavour=="out of stock":
        continue
    if flavour=="discontinued":
        break
    print("discontunued found")
print("outside the loop")