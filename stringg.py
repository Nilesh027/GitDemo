chai = "      Masala Chai Chai    "

slice_chai = chai[0:6]

print(slice_chai)

num_list = "0123456789"

print(num_list[:])

print(num_list[3:])

print(num_list[:5])

print(num_list[0:7:2])

print(chai.upper())
print(chai.lower())

print(chai.strip()) # Remove Extra spaces 

print(chai.replace("Masala", "Ginger"))
print(chai)
print(chai.find("Chai"))
print(chai.count("Chai"))
print("Masala" in chai)

# chai_type = "Masala"
# quantity = 2
# order = "f(I ordered {quantity} cups of {chai_type} chai)" # {}--In python Used as a Place holder.
# print(order)
# print(order.format(quantity, chai_type))

tea_varities = ["Black", "Green", "Oolang", "White"]
print("".join(tea_varities))
print(" ".join(tea_varities))
print("-".join(tea_varities))
print(", ".join(tea_varities))

print(len(chai))

# for i in chai:
#     print(i)

Chai = "He said, \"Masala chai is awesome\" "
print(Chai)

#--------------------tuple-----------------------------------------------------------------------------------------------------

tea_type = ("Black", "Green", "Oolang")
more_tea = ("Herbal", "Earl Grey")
all_tea = tea_type + more_tea
print(all_tea)

if i in tea_type: # Wrong syntex this is a conditional statement 
    print(i)

if "Black" in tea_type:
    print("Yes present")
