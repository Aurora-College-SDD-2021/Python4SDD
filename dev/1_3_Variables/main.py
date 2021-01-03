""" Demonstrate variables.

Add the line of code where indicated to change the value of the variable.
The script will print out the value before and after you change it.
Use the run arrow or debugger to run the program.
Run pytest in the repl.it shell to check your work.
"""

def the_answer() -> int:
    """Provides an answer to the question of Life, The Universe, Everything.

    Also some travel information about Earth.
    """
    meaning_of_life: int = 42
    planet_earth: str = "harmless"
    print(f"the Meaning of Life is {meaning_of_life}")
    print(f"Earth is {planet_earth}")
    # add lines of code immediately below that change the values of the variables
    
    
    print(f"the Meaning of Life is {meaning_of_life}")
    print(f"Earth is {planet_earth}")
    return [meaning_of_life, planet_earth]

# main script
the_answer()