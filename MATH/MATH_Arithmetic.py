'''
ARITHMETIC OPERATORS

These functions are basic, but help to make the code more readable in other sections.
'''
def iDiff(iFinal, iInit):

    return iFinal - iInit


def iRatio(iNum, iDen):

    if iDen != 0:
        
        return iNum / iDen

    print("Division by 0 detected with {} / {}".format(iNum, iDen))
    
    return 0


def iFactorial(iNum):

    iResult = 1

    while iNum != 0:

        iResult *= iNum
        iNum -= 1

    return iResult


def iReciprical(iNum):

    if iNum != 0:

        return 1 / iNum

    return "ERROR! DIV/0"


def iScientificNotation(iCoeff, iPower):

    return iCoeff * (10 ** iPower)


def iPercent(iDec):

    return 100 * iDec


def sCompoundFraction(iDec):

    iWholeNum = 0

    while iDec > 1:

        iWholeNum += 1
        iDec -= 1

    sFraction = sTransformDecToFraction(iDec)
    print("{} + {}".format(int(iWholeNum), sFraction))
