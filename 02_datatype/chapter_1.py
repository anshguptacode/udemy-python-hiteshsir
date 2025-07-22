sugar_ammount=2
print(f"Inital sugar :{sugar_ammount}")
sugar_ammount=12
print(f"Second Amount :{sugar_ammount}")
print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")
"""
sugar_ammount = 2:
An integer object with the value 2 is created in memory. Let's assume its unique memory address (identity) is ID_A.
The variable sugar_ammount is then assigned to reference this integer object at ID_A.
print(id(sugar_ammount)) will output ID_A.
sugar_ammount = 12:
This is an assignment operation. Since integers are immutable data types in Python, 
the existing integer object 2 at ID_A cannot be modified in-place to become 12.
Instead, a new integer object with the value 12 is created in a different memory location. Let's assume its unique memory address is ID_B.
The variable sugar_ammount is then reassigned (rebound) to now reference this new integer object at ID_B.
print(id(sugar_ammount)) will now output ID_B.
print(f"ID of integer object 2: {id(2)}"):
This explicitly requests the identity of the integer object 2. Python might have a cached instance of 2 (for small integers,
Python often pre-allocates them for efficiency), and it will return ID_A.
print(f"ID of integer object 12: {id(12)}"):
This explicitly requests the identity of the integer object 12. It will return ID_B.

#The crucial point:
The id of sugar_ammount changed between the two assignment statements because sugar_ammount stopped pointing to the object with value 2 and 
started pointing to a different object with value 12. This behavior is characteristic of operations involving immutable types: any "modification" 
effectively creates a new object.

## In This what i am changing is the reference not the values (means i cannot change the value of 2 or 12)
what the python in the backend is doing is changeing the reference of sugar_ammount from 2 then to 12.

"""