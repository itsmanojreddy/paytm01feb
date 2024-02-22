global_variable = 42

global x
x=10
print(x)
print(type(x))


def my_function():
    # global global_variable
    x = 2
    print(locals()['x'])
    print(globals()['x'])
    global_variable = 1
    print("Inside my_function:", global_variable)


my_function()

print("Outside my_function:", global_variable)
