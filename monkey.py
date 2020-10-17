
"""
Here’s a self check that really covers everything so far. You may have heard of the infinite monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. 

Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”

You’re not going to want to run this one in the browser, so fire up your favorite Python IDE. The way we’ll simulate this is to write a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.

A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.

"""

from random import randint

alphabet = "abcdefghijklmnopqrstuvwxyz "
goal = "methinks it is like a weasel"


print(len(alphabet))
print(len(goal))


def generate_string():
    new_string = ''
    for _ in range(len(goal)):
        new_string += alphabet[randint(0, len(alphabet) - 1)]
    return new_string


def score_string(gen_string):
    score = 0
    count = 0
    for letter in goal:
        if(gen_string[count] == letter):
            score+=1
        count+=1

def repeat():
    pass


for _ in range(10000):
    print(generate_string())
