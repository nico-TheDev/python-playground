from stack import Stack

"""
The challenge then is to write an algorithm that will read a string of parentheses from left to
right and decide whether the symbols are balanced. 

To solve this problem we need to make an important observation. 

As you process symbols from left to right, the most recent opening
parenthesis must match the next closing symbol (see Figure 3.4). 

Also, the first opening symbol processed may have to wait until the very last symbol for its match. Closing symbols matchopening symbols in the reverse order of their appearance; they match from the inside out. This is a clue that stacks can be used to solve the problem. 

Once you agree that a stack is the appropriate data structure for keeping the parentheses,
the statement of the algorithm is straightforward. Starting with an empty stack, process the
parenthesis strings from left to right. 

If a symbol is an opening parenthesis, push it on the stack as a signal that a corresponding closing symbol needs to appear later. If, on the other
hand, a symbol is a closing parenthesis, pop the stack. 

As long as it is possible to pop the stack to match every closing symbol, the parentheses remain balanced. If at any time there is no opening symbol on the stack to match a closing symbol, the string is not balanced properly. 

At the end of the string, when all symbols have been processed, the stack should be empty.

"""


def parenthesis_checker(pattern):
    stack = Stack() # initialize a stack 
    balance = True  # assume that the stack will be balanced

    for par in pattern: # iterate through the stack 
        if par == "(": # check the current symbol
            stack.push("(") # push in the stack if open
        elif par == ")": 
            if stack.isEmpty(): # if the stack is empty then it is not balance
                balance = False
            else:
                stack.pop() # pop the stack if it is not empty

    return stack.isEmpty() and balance # check if the stack is empty and it remained balanced


print(parenthesis_checker('(()((())()))'))
print(parenthesis_checker('(((())))'))
print(parenthesis_checker("()))"))
print(parenthesis_checker("()))"))
print(parenthesis_checker("()))"))
print(parenthesis_checker("()"))
