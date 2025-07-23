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