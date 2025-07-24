chai_order=dict(type="masala chai",suagr_level=3,size="large")
print(f"chai order: {chai_order}")

chai_recipe=dict()
chai_recipe["base"]="black tea"
chai_recipe["liquid"]="milk"
print(chai_recipe)
'''
here we can observe that the case and liquid are taked as key for the dictionary and 
black tea and milk as the vales for the keys
'''
print(chai_recipe["base"])
del chai_recipe["liquid"]#to delete the element
print(chai_recipe)

#membership
print(f"is sugar avaliable in chai recipe? {"sugar" in chai_recipe}")

print(f"Keys of chai_order: {chai_order.keys()}")
print(f"Values of chai_order: {chai_order.values()}")
print(f"Items of chai_order: {chai_order.items()}")
last_item=chai_order.popitem()
print(last_item)
print(chai_order)
extra_spices=dict( cardmom= "crushed",ginger= "sliced")
chai_recipe.update(extra_spices)
print(f"updated chai recipe: {chai_recipe}")
chai_size=chai_order.get("customer note","not found")
print(chai_size)