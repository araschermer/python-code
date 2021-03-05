def sum_digits():
    """ sums, prints, and returns the digits of the number that the user inserts.
    the functionality can be viewed on repl.it website using the following links
     https://repl.it/@abdelkha/sum-digits?embed=1&output=1#main.py"""
    sum_ = 0
    while True:
        try:
            digits = input('please enter integers only\n')  # saves user input in variable
            for digit in digits:
                sum_ += int(digit)
            print(sum_)
            break
        except ValueError:
            print("Please enter integers only\n ")
            continue
    return sum_


if __name__ == '__main__':
    sum_digits()
