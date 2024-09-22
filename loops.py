# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]  #Find  how many are positive number
# positive_number_count = 0
# negative_number_count = 0
# for num in numbers :
#     if num>=0:
#         positive_number_count += 1
#     elif num<=0:
#         negative_number_count += 1

# print("Final count of positive number is :", positive_number_count, negative_number_count)
#----------------------------------------------------Reverse string -------------------------------------------

input_str = "Python"
reversed_str = ""
for char in input_str:
    reversed_str =  char + reversed_str 
print(reversed_str)

input_str = "teeteracdacd"
#---------------------------------------------Find first non-reapeated character------------------------------
for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is : ", char)
        #break

#-------------------------------------------Factorial Calculator using while loop -----------------------------
number = 5
factorial = 1
while number > 0:
    # factorial = factorial * number
    factorial *= number
    # number = number - 1
    number -= 1 
    print("Factorial is :--", factorial)

#---------------------------------------Validate Input, Keep asking untill they enter number B/w 1 and 15-------------------------------------

while True:
    number = int(input("Enter value b/w 1 and 15 :-  "))
    if 1 <= number >= 10:
        print("Thanks")
        break
    else:
        print("Invalid number , try again")

#------------------------------------Prime number Check-------------------------------------------------------------

number = 29

is_prime = True
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)

