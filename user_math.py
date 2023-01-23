"""
Andy Asher 
01/22/23
This module uses custom functions to evaluate salaries and spread union propoganda.

Original provided docstring:

Always start with a docstring that describes what the module does.
Include your name and the date.

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)
def cost_liv_adj(orsal,numyrs):
#shows cost of living adjustments to original salary based on number of years in role
    try:
        adjustment = math.floor((float(orsal * (1.03 ** numyrs)) - orsal))
        return adjustment
    except Exception as ex:
        print(f"Error: {ex}")
        return None

def find_newsal(orsal, numyrs):
#find new salary based on cost of living and years in role
    try:
        new_salary = math.floor(float(orsal * (1.03 ** numyrs)))
        return new_salary
    except Exception as ex:
        print(f"Error: {ex}")
        return None

def has_wage_stagnated (orsal, newsal, numyrs):
#checks if salary has kept up with inflation
    try:
        #find what new salary should be
        expected = math.floor((float(orsal * (1.03 ** numyrs)) - orsal))
        #compare salaries
        if (newsal - orsal) < expected:
            return True
        else:
            return False
    except Exception as ex:
        print(f"Error: {ex}")
        return None      
# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":
 print("Explore some functions in the math module")
 print()
 print(f"math.comb(5,1) = {math.comb(5,1)}")
 print(f"math.perm(5,1) = {math.perm(5,1)}")
 print(f"get_area_lot(6,2) = {get_area_of_lot(6,2)}")
# call your functions here (see instructions)
print()
print()
print("your code here")
print()
print()
print("Check if your employer has offered the bare minimum cost of living adjustments to your salary!")
print()
print()
print("To see what your salary should have increased by, use find_newsal")
print()
print(f"""For example, if you started at $40,000 and have been in your role for 3 years
    you would enter cost_live_adj(40000, 3) and learn that your salary should have
    increased by ${cost_liv_adj(40000, 3)}""")
print()
print()
print(f"""If you want to see what your new salary should be after cost of living adjustments, you would use find_newsal! 
    
    For example:
    if you started at 50000 and have been in your role for 5 years,
    you would ender find_newsal(50000,5) and find that your new salary
    should be ${find_newsal(50000, 5)}""")
print()
print()
print(f"""To compare your salary to the bare minimum cost of living adjustments
    use has_wage_stagnated. For example if you started at $60,000 5 years ago, and now make $65,000
    you would enter has_wage_stagnated(60000, 65000, 5). Has that wage stagnated, true or false? {has_wage_stagnated(60000, 65000, 5)}! """)
print()
print()
print("If your wages haven't kept up with inflation, you should ask for a raise.")
print("A union can help with asking for a raise!")

