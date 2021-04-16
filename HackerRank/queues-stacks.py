import sys


# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and
# forwards. Can you determine if a given string, , is a palindrome?
# To solve this challenge, we must first take each character in , enqueue it in a queue, and also push that same
# character onto a stack. Once that's done, we must dequeue the first character from the queue and pop the top
# character off the stack, then compare the two characters to see if they are the same; as long as the characters
# match, we continue dequeueing, popping, and comparing each character until our containers are empty (a non-match
# means  isn't a palindrome).
# Input Format
# You do not need to read anything from stdin. The locked stub code in your editor reads a single line containing
# string s. It then calls the methods specified above to pass each character to your instance variables.

class Solution:
    # Write your code here
    def __init__(self):
        super().__init__()
        self.stack = []
        self.queue = []

    def pushCharacter(self, s):
        """pushes a character onto a stack"""
        self.stack.append(s)

    def enqueueCharacter(self, s):
        """enqueues a character in the queue  instance variable"""
        self.queue.append(s)

    def popCharacter(self):
        """pops and returns the character at the top of the stack instance variable"""
        return self.stack.pop()

    def dequeueCharacter(self):
        """dequeues and returns the first character in the queue instance variable"""
        first_element = self.queue[0]
        self.queue.remove(first_element)
        return first_element


# read the string s
s = input("Write a string to test\n")
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
