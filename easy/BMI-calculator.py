def calculate_body_mass_index(weight, height):
    """calculates the Body Mass Index through the formula: BMI =(weight(in kg)/height(in meters)^2).
    the functionality can be viewed on repl.it website using the following links
    https://repl.it/@abdelkha/BMI-calculator?embed=1&output=1#main.py """
    bmi = int(weight) // float(height) ** 2  # calculates exponentiation (height^2) prior to the division
    # saves the whole number in the variable bmi
    # alternative: use the following to return a round the number to two digits
    #  mbi=round(weight/height**2,2)
    weight_status = ""
    if bmi < 18.5:
        weight_status = "underweight"
    elif 18.5 <= bmi <= 25:
        weight_status = "normal"
    elif 25 < bmi <= 30:
        weight_status = "overweight"
    elif 30 < bmi <= 35:
        weight_status = "obese"
    elif bmi > 35:
        weight_status = "clinically obese"

    if weight_status == "normal":
        print(f" your BMI is: {bmi}, your have a {weight_status} weight!")
    else:
        print(f" your BMI is: {bmi}, you are {weight_status}")

    return bmi


if __name__ == '__main__':
    calculate_body_mass_index(weight = 66, height = 1.75)
