"""An exercise in recognising different data types.
"""

def data_type():
    """Demonstrates different data types.

    Modify the code below replacing None by different data types as indicated
    """
    # replace None with an integer
    an_int = None

    # replace None with a floating point number
    a_float = None

    # replace None with a string - don't forget the quotation marks!
    a_str = None

    # replace None with a boolean - dont forget in Python the first letter must be a capital!
    a_bool = None

    #this line groups all the data and sents it back to the command that called it
    return [an_int, a_float, a_str, a_bool]


if __name__ == "__main__":
    # print out the data type and its value
    for variable in data_type(): 
        print(f'Data type is {type(variable)}: Value is {variable}')