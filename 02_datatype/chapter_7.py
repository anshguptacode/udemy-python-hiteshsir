masala_spices=("cardmom", "ginger" ,"dalchini", "balck salt")
(spice1,spice2,spice3,spice4)=masala_spices
print(f"Ingridiants are :{spice1} ,{spice2} ,{spice3}")
ginger_ratio,cardmom_ratio=1,2
'''
here in python we can use both the format for tuples such as name= ("a","b") then assing them other variable name to 
point them or we can directly use the method we used in ratios 
both of them will act as a tuples and are mutable 
'''
print(f"Ratio of ginger:{ginger_ratio} and ratio of cardmom: {cardmom_ratio}")
ginger_ratio,cardmom_ratio=cardmom_ratio,ginger_ratio
print(f"Ratio of ginger:{ginger_ratio} and ratio of cardmom: {cardmom_ratio}")
"""
here what we have done is we have swaped the values simply but in other languages we have to use
differrent methods such as temp which is easy to use but still its more simple accoring to PEP8,
"why to be complicated if it can be simple"
"""

#membership
print(f"Is cardomom in masala spices :{"cardmom" in masala_spices}")
print(f"Is cardomom in masala spices :{"sugar" in masala_spices}")


