#Runtime: 24 ms, faster than 94.29% of Python3 online submissions for Student Attendance Record I.
# Memory Usage: 14.2 MB, less than 73.33% of Python3 online submissions for Student Attendance Record I.
# https://leetcode.com/submissions/detail/473427699/
def checkRecord(s: str) -> bool:
    """ given a string s representing an attendance record for a student where each character
    signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
    'A': Absent.
    'L': Late.
    'P': Present.
    The student is eligible for an attendance award if they meet both of the following criteria:
    The student was absent ('A') for strictly fewer than 2 days total.
    The student was never late ('L') for 3 or more consecutive days.
    Return true if the student is eligible for an attendance award, or false otherwise."""
    absent = s.count("A")
    if absent >= 2:
        return False
    else:
        maximum = 3
        for char in s:
            if char == "L":
                maximum -= 1
            else:
                maximum = 3
            if maximum == 0:
                return False
        return True


if __name__ == "__main__":
    test_cases = ["PPALLP", "PPALLL"]
    for test in test_cases:
        print(checkRecord(test))
