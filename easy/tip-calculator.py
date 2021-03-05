def calculate_tip(bill, people, tip):
    """ calculates a tip based on a given percentage of the total bill amount.
    the functionality can be viewed on repl.it website using the following links
     https://repl.it/@abdelkha/Tip-calculator?embed=1&output=1#main.py"""
    tip_percentage = tip / 100
    total_tip_amount = bill * tip_percentage
    bill_after_tips = bill + total_tip_amount
    bill_per_person = round(bill_after_tips / people, 2)
    print(f"Each person should pay: ${bill_per_person}")


if __name__ == '__main__':
    # If the bill was $150.00, split between 5 people, with 12% tip.
    # Each person should pay (150.00 / 5) * 1.12 = 33.6
    calculate_tip(bill = 150, people = 5, tip = 12)
