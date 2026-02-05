# Opgave 3 (Parallel Resistors)

# deliberately not using numpy in this one

def parallel_resistors(resistances: list): # expects list as an argument
    R = 0
    for Rn in resistances:
        R += 1/(Rn)
    return R**(-1)