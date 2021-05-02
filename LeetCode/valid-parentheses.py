def is_valid(s):
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    :type s: str
    :rtype: bool
    """
    parentheses = '()[]{}'
    if len(s) % 2 != 0:  # simple check, if string length is odd, return false
        return False
    for index, p in enumerate(s):
        if p not in parentheses: # simple check, if all parentheses in the string are valid, otherwise raise exception
            raise TypeError("invalid parentheses")
    stack = []
    parentheses = {")": "(", "}": "{", "]": "["}  # map closing parentheses to opening parentheses
    for p in s:
        if p in parentheses.values():  # if opening parentheses is found
            stack.append(p)  # push onto stack
        elif stack and parentheses[p] == stack[-1]: # if stack is not empty and opening_p of this closing p is existing
            # on the stack
            stack.pop()# pop off stack
        else:
            return False
    return stack == []


if __name__ == '__main__':
    #     Example 1:
    # Input: s = "()"
    # Output: true
    print(is_valid("()"))

    # Example 2:
    # Input: s = "()[]{}"
    # Output: true
    print(is_valid("()[]{}"))

    # Example 3:
    # Input: s = "(]"
    # Output: false
    print(is_valid(")(]"))

    # Example 4:
    # Input: s = "([)]"
    # Output: false
    print(is_valid("([)]"))

    # Example 5:
    # Input: s = "{[]}"
    # Output: true
    print(is_valid("{[]}"))
