# username = "Chaiaur code "

# def fun():
#     username = "Coffee"
#     print(username)

# print(username)
# fun()


# def fun02(y):
#     z = x + y
#     return z

# result = fun02(1)
# print(result)
#-------------------------------------------------------------------------------------
# def fun03():
#     X = 88

# print(X)
#--------------------------------------
# def fun03():
#     global X
#     X = 88

# fun03(0)
# print(X)
#-------------------------------------------------------------------------------------

# def f1():
#     #X = 88                  Climbing
#     def f2():
#         print(X)
#     f2()
# f1()

#-----------------
# def f1():
#     X = 88
#     def f2():
#         print(X)
#     return f2            # Kya hoga jab main yaha return keyword laga du f2() PARENTHESIS KA HOTA EXECUTE KARNA APNE KO F2 KO RETURN KARNA HAI ! 
# myResult = f1()
# myResult()

#-------------------------FACTORY FUNCTION 
def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))