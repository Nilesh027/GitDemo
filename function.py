# def square(number):
#     return number ** 2

# result = square(4)
# print(result)
# print(square(4))

#------------------------------------Fubctions with * args -----------------------------------------------

# def sum_all(*args):
#     return sum(args)

# print(sum_all(1,2))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7,8))

# def sum_all(*args):
#     print(*args)
#     return sum(args)

# print(sum_all(1,2))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7,8))

# def sum_all(*args):
#     print(args)
#     return sum(args)

# print(sum_all(1,2))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7,8))

# def sum_all(*args):
#     print(args)
#     for i in args:
#         print(i * 2)
#     return sum(args)

print(sum_all(1,2,3))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7,8))

#----------------Function with **kwargs --------------------------
# Create a function that accepts any number of keyword arguments and prints them in the the format key:value

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Shaktiman", Power = "lazer")    

# Generator Function with yield--write a generator function that yields even numbers up to a specified limit.
