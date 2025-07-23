essential_spices={"cardmom", "cloves", "ginger",}
optional_spices={"black pepper","ginger","dalchini"}

all_spices=essential_spices|optional_spices
print(all_spices)
'''
here as we can obsever that the duplicate item for the set is not printed this
happen due to the operator called union "|" which we can say merge the duplicate item and print it
only once
'''
print(f"common spice: {essential_spices&optional_spices}")
'''
here we use intersection operator "&"which help us to print out the common item in the set

'''
print(f"removing common spice: {essential_spices-optional_spices}")
#membership
print(f"is ginger present in optional? {"ginger" in optional_spices}")
#frozen set
essential_items = frozenset(["milk", "bread", "ketchup"])
print(essential_items)