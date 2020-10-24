def anagramSolution1(wordOne, wordTwo):
    isOK = True  # initialize isOK as TRUE

    # if words are different lengths automatic not an anagram
    if len(wordOne) != len(wordTwo):
        isOK = False

    wordTwoList = list(wordTwo)
    positionOne = 0

    # wiil only run if same length
    while positionOne < len(wordOne) and isOK:
        positionTwo = 0
        found = False
        while positionTwo < len(wordTwoList) and not found:
            if wordOne[positionOne] == wordTwoList[positionTwo]:
                found = True
            else:
                positionTwo = positionTwo + 1

        if found:
            wordTwoList[positionTwo] = None
        else:
            isOK = False

        positionOne = positionOne + 1

    return isOK


print(anagramSolution1('abcd', 'dcba'))


def anagramSolution2(wordOne, wordTwo):
    # converst the String into List
    listOne = list(wordOne)
    listTwo = list(wordTwo)
    # access the sort method from the list so each letter will be sorted out
    listOne.sort()
    listTwo.sort()

    # initialize a position and infer that it's an anagram
    pos = 0
    matches = True
    # iterates until pos is less than length of wordOne
    while pos < len(wordOne) and matches:
        if listOne[pos] == listTwo[pos]:  # if both letters are the same
            pos = pos + 1  # go to the next letter
        else:
            # not the same letter so not an anagram
            # matches will now be False so the next iteration wont happen
            matches = False
    return matches


print(anagramSolution2('abcde', 'edcba'))


def anagramSolution4(wordOne, wordTwo):
    countOne = [0]*26
    countTwo = [0]*26

    # iterates every letter of the word
    for i in range(len(wordOne)):
        # position as order of the letter minus the first letter order a
        pos = ord(wordOne[i]) - ord('a')
        # adds one to the position
        countOne[pos] = countOne[pos] + 1

    # repeat process for word two
    for i in range(len(wordTwo)):
        pos = ord(wordTwo[i])-ord('a')
        countTwo[pos] = countTwo[pos] + 1

    current = 0
    stillOK = True
    while current < 26 and stillOK:
        if countOne[j] == countTwo[j]:
            current += 1
        else:
            stillOK = False

    return stillOK


print(anagramSolution4('apple', 'pleap'))
