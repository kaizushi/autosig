import os
import time

class errorRuleFormat(Exception):
    """The rules file format is incorrectly formatted"""
    pass


# a newline seperated list of replacement rules
def getRules(repF):
    rulefile = open(repF, 'r')
    rulelist = []
    for reprule in rulefile:
        rulelist.append(reprule)
    return rulelist

def getTruth(question):
    print(question + " Y/N?")
    while (True): #if you cant see the exit cond you must hang
       answer = input()
       if (answer = "Y"):
            return True
       elif (answer = "N"):
            return False
       print("You need to respond with a capital Y or N, try again...")


def getUserAnswers(rulelist):
    hardlist = []

    for rule in rulelist:
        rules = rule.split('|') #yes i do know i can have a list of lists

        if (len(rules) != 2):
            raise errorRuleFormat

        namerule = rules[0]
        donerule = ""

        if (rules[1] == "!ASKUSER!"):
            while (True):
                ans = input("What do you wish " + namerule + " to be?")
                truth = getTruth("Are you actually sure you want it to be " + ans)

                if (truth == True): #silence, i just like breaking things up
                    donerule = ans
                    continue

                print("I will ask once again...")
        else:
            donerule = rules[1]
        hardlist.append(namerule + "|" + donerule)
    return hardlist

# a template with 
def getTemplate(templateF):
    tplfile = open(templateF, 'r')
    tpldata = []
    for line in tplfile:
        tpldata.append(line)

def transByArray(dataIn, arrayIn):
    trans = []
    for rule in arrayIn:
        for line in DataIn:
            trans.append(string.replace(rule, dataIn))
    return trans
