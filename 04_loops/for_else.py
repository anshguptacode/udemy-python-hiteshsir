staff=[("Ansh", 21),("DPS",20),("Vanshika",21)]

for name ,age in staff:
    if age>=20:
        print(f"{name} is elegiable")
        break
else:
    print("No one is elegiable")

'''
he code iterates through the staff list in order.
It first checks Ansh, whose age is 21.
The condition age >= 20 is true.
It prints "Ansh is elegiable".
The break statement is executed, and the loop stops completely. It will not proceed to check DPS or Vanshika.
'''