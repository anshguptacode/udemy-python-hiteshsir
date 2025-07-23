ingredients= ["water","sugar","milk"]
print(f"Ingridients are: {ingredients}")
ingredients.append("Tea Leaves")
print(f"Ingridients are: {ingredients}")
'''
This means that list are mustable and we can add , remove or 
do other oprations on it accordning to our needs
'''
spices=["cardmom","ginger","dalchini"]
ingredients.extend(spices)
print(f"Things needed:{ingredients} ")
'''
We can also perform slicing opration on list where first element is consider as index 0 and 
similar to previous chapter we can can print the needed elements of the list

'''
print(f"Sliced ingridents are: {ingredients[1:5]}" )

'''
Using Slicing operation we can add elemets to the indexes we want to add them
'''
ingredients.insert(4,"black pepper") #when we append it add the element to the last postion of list but using insert we can add to the desired posiotion
print(ingredients)

ingredients.pop()#using pop we can remove the last element of the list
print(ingredients)

'''
we can also use max and min function for finding the man and min element in the list
'''
sugar_level=[1,2,3,4,5,6]
print(f"maximum sugar level is:{max(sugar_level)}")
print(f"minimum sugar level is:{min(sugar_level)}")
ingredients.sort()