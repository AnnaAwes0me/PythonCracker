#!/usr/bin/python

import random
import time

#I'm not necessarily that this works to load from both documents because I've just loaded twice.
#Should probably considered a load statement which accepts multiple files and then uses some sort of switch statement to vary the number of the sentences and then implements them in the actual cracking schema.
start_time = time.time()
with open ("eharmony.hash") as firstFile:
    dataFirst = firstFile.read().replace('\n', '')
sentence = dataFirst

#with open ("unmasked.lst" "r") as secondFile:
#    dataSecond = secondFile.read().replace('\n', '')
#secondSentence = dataSecond

def randomletter(numberofletters):

    # Takes a int and will retruns a list
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', ' ']
    listofletters = []
    index = numberofletters
    while index != 0:
        listofletters.append(letters[random.randint(0, 26)])
        index = index - 1
    return listofletters


def compare(alist, astr):

    # Takes a list and compares it to a str and retruns a percantage
    listtostr = "".join(alist)
    matches = 0
    index = 0
    for ch in listtostr:
        if ch == astr[index]:
            matches = matches + 1
        index = index + 1
    letters = float(len(astr))
    percentage = matches / letters * 100
    return (percentage, listtostr)


percentage = 0
bestpercentage = 0
trys = 0
while percentage < 100:
    percentage, string = compare(randomletter(len(sentence)), sentence)
    trys = trys + 1
    if percentage > bestpercentage:
        bestpercentage = percentage
        print(bestpercentage)
        print(string)
        print(trys)

print((time.time() - start_time) / 60, "minutes")
