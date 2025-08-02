# # value=13
# # remainder=value%5
# # if remainder:
# #     print(f"Not divisible by 5, Remainder is : {remainder}")

# value =13
# if(remainder := value%5):
#     print(f"Not divisible by 5, Remainder is : {remainder}")


# available_sizes =["small","large", "medium"]
# if (requested_size := input("Enter your size : ")) in available_sizes:
#     print(f"The requested size is: {requested_size}")
# else:
#     print(f"This size is not avaliable: {requested_size}")

flavours = ["masala", "Lemon" ,"mint"]
print("Available flavors are",flavours)
while (flavour := input("Choose your falvor: ")) in flavours:
    print(f"sorry, {flavour} is not avaliable")
print(f"Choose your flavor {flavour}")