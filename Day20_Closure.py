def outer_function(x):
    # This is the enclosing function that defines a variable 'x'
    
    def inner_function(y):
        # This is the inner function that takes an argument 'y'
        # and has access to the variable 'x' from the enclosing scope
        return x + y
    
    # Return the inner function without calling it
    return inner_function

# Call the outer function to create a closure
closure = outer_function(10)

# Call the closure with an argument
result = closure(5)

print(result)  # Output will be 15

def ad(x):
    def add(y):
        return x+y
    return add
closure=ad(49)
print(closure(30))
print(closure(44))

"""closure_instance=ad(66)
resu=closure_instance(34)
print(resu)"""

