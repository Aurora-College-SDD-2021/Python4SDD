""" Introduction to operators.

More detailed instructions. Use the run arrow or debugger to run the program.
Run pytest in the repl.it shell to check your work.
"""

def calc_sum(num1, num2):
    """Returns the sum of num1 and num2.
    
    This one has been done for you. Use it as a gide for
    the funstions below.
    """
    result = num1 + num2
    return result

def calc_difference(num1, num2):
    """Returns the difference between num1 between num2."""
    result = None
    return result

def calc_product(num1, num2):
    """Returns the product of num1 and num2."""
    result = None
    return result

def calc_quotient(num1, num2):
    """Returns num1 divided by num2."""
    result = None
    return result

def calc_remainder(num1, num2):
    """Returns the remainter of num1 divided by num2."""
    result = None
    return result

def calc_exponentiation(num1, num2):
    """Returns num1 to the power of num2."""
    result = None
    return result

def largest(num1, num2):
    """Returns the largest of the two numbers.
    
    This one has been done for you. Use it as a gide for
    the funstions below.
    """
    if num1 > num2:
        return num1
    else:
        return num2

def smallest(num1, num2):
    """Returns the smallest of the two numbers."""
    return None
    

# Ignore everything below this line...we will talk about it later
if __name__ == "__main__":
    num1 = 6
    num2 = 7
    print(f"The sum of the two numbers is {calc_sum(num1, num2)}")
    print(f"The difference between the two numbers is {calc_difference(num1, num2)}")
    print(f"The product of the two numbers is {calc_product(num1, num2)}")
    print(f"The quotient of the two numbers is {calc_quotient(num1, num2)}")
    print(f"The remainder of the two numbers is {calc_remainder(num1, num2)}")
    print(f"The first number raised to the second is {calc_exponentiation(num1, num2)}")
    
    pass