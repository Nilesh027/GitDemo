"""Questions on conditionals

1. Age Group Categorization
2. Movie Ticket Pricing
3. Grade Calculator
4.Fruit Ripeness Checker
5. Weather Acitvity Suggestion
6. Transportation Mode Selection
7. Coffe Customization
8. Password Strength Checker
9. Leap Year Checker
10. Pet Food Recommendation

 """
age = int(input("Your age please"))
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2
print(price)