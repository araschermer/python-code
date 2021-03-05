def calculate_body_mass_index(weight, height):
    """calculates the Body Mass Index through the formula: BMI =(weight(in kg)/height(in meters)^2).
    the functionality can be viewed on repl.it website using the following links
    https://repl.it/@abdelkha/BMI-calculator?embed=1&output=1#main.py """
    bmi = int(weight) // float(height) ** 2  # calculates exponentiation (height^2) prior to the division
    # saves the whole number in the variable bmi
    # alternative: use the following to return a round the number to two digits
    #  mbi=round(weight/height**2,2)
    print(bmi)
    return bmi

if __name__ == '__main__':
    calculate_body_mass_index(weight = 80, height = 1.75)
