tea_varities = ["Black", "Green", "Oolang", "White"]
print(tea_varities)
print(tea_varities[1])
tea_varities[3] = "Herbal"
print(tea_varities)
tea_varities[1:2] = "Lemon"
print(tea_varities)
tea_varities = ["Black", "Green", "Oolang", "White"]
tea_varities[1:2] = ["Lemon"]

for tea in tea_varities:
    print(tea, end="-")
