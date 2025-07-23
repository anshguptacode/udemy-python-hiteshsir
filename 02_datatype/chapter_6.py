chai_type="ginger"
customer="Ansh"
print(f"Order for {customer} : {chai_type} Please! ")
chai_discription='Aromatic Chai'
print(f"First word : {chai_discription[0:9]}")
print(f"last word : {chai_discription[8:]}")
print(f"Revrese : {chai_discription[::-1]}")


'''
Here what we learn is slicing in this we can slice down the letter form sting accound to out need
the concept of indexing is used in it so what we are doing here is we want to get the first word form the 
chai discription what we does is we start from 0 index means the word 'A' then to the last word 'c' but 
due to some wierd rule the the slice will print only the n-1 element where n=number of index steps 

NOTE the syntac for indexing is [start:end-1:steps]
Trick for reversing [::-1]
'''

'''
Now we will learn the encoding and decoding

'''
lable_type="柴"
endcoded_labe=lable_type.encode("utf-8")
print(f"non endcoded word: {lable_type}")
print(f"endcoded word: {endcoded_labe}")
decoded_lable=endcoded_labe.decode("utf-8")
print(f"decoded word: {decoded_lable}")