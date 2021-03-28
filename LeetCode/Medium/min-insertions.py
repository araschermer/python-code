def min_insertions(s: str) -> int:
    opening_count = 0
    closing_count = 0
    s = s.replace("))", "}")
    # print(s)
    for parenthesis in s:

        if parenthesis == "(":
            opening_count += 1
        elif parenthesis == ")":
            if opening_count > 0:
                closing_count += 1
                opening_count -= 1
            else:  # here we need another closing parenthesis and an opening parenthesis to balance ->2
                closing_count += 2
        else:  # to handle the cases of "}"
            if opening_count > 0:  # if the string already contains an opening parenthesis
                opening_count -= 1
            else:  #
                closing_count += 1
    # print(f"closing_count={closing_count} opening_count={opening_count}")

    # print(closing_count + (opening_count * 2))
    return closing_count + opening_count * 2


if __name__ == "__main__":
    test_cases = ["(()))", "())", "))())(", "((((((", ")))))))"]
    for test in test_cases:
        print(min_insertions(test))
