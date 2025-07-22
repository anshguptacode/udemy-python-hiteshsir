spice_mix =set()
print(f"Inital Spice Mix ID : {id(spice_mix)}")
print(f"Inital Spice Mix : {spice_mix}")
spice_mix.add("ginger")
spice_mix.add("Dalchini")
print(f"Afer spice Mix ID:{id(spice_mix)}")
print(f"Afer spice Mix :{spice_mix}")
'''
Inital Spice Mix ID : 4371042752
Inital Spice Mix : set()
Afer spice Mix ID:4371042752
Afer spice Mix :{'Dalchini', 'ginger'}

    # HERE AS WE CAN SEE THE ID REMAINS THE SAME FOR THE SPICE MIX
    BUT WE CAN STILL ADD THE NEW VALUES INTO THE SET WHICH MEANS SET IS OF MUTABLE TYPE
    THERE ARE MORE SUCH AS LIST DICTIONARIES ETC.
    
'''