is_boiling=True
no_of_cups=5
total_no_of_cups=is_boiling+no_of_cups
print(f"total of cups: {total_no_of_cups}") 
'''
This is what we called upcasting here what we can see is
the bool type for is_boiling is true which is consider as 1 
so when we add the int type with bool it will give us result as 6
also, for false it is consider as 0
'''

is_milk_ava=0
print(f"Is milk Avaliable= {bool(is_milk_ava)}") #as we can observe the int 0 is consider as bool when we use keyword "Bool"

water_added=True
Tea_added=True
can_serve=water_added and Tea_added
print(f"Can tea be served: {can_serve}")