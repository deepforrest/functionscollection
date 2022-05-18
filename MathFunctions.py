def iFactorial(iNum):

    iResult = 1

    while iNum != 0:

        iResult *= iNum
        iNum -= 1

    return iResult


def iCombinations(iSelection, iSetTotal):

    return iFactorial(iSetTotal) / (iFactorial(iSelection) * iFactorial(iSetTotal - iSelection))


def iPermutations(iSelection, iSetTotal):

    return iFactorial(iSetTotal) / iFactorial(iSetTotal - iSelection)


def iIntegratePolyTerm(iCoeff, iVar, iPower):

    iNewPower = iPower + 1

    return (iCoeff * (iVar ** iNewPower)) / iNewPower


def iDifferentiatePolyTerm(iCoeff, iVar, iPower):

    iNewPower = iPower - 1

    return (iCoeff * iPower * (iVar ** iNewPower))

# Tested.  Returns an array of prime numbers that when multiplied together, create the original number.  Optimized for speed
def iArrFactorsOfNum(iNum):

    iArrFactors = []
    iDivisor = 2

    while iDivisor <= iNum:

        #print ("Number = " + str(iNum))
        #print ("Divisor = " + str(iDivisor))

        while iNum % iDivisor == 0:

            iArrFactors.append(iDivisor)
            #print(str(iNum) + " is divisible by " + str(iDivisor))

            iNum /= iDivisor
            #print("New Number: " + str(iNum))

        if iDivisor != 2:

            iDivisor += 2

        else:

            iDivisor += 1

    if len(iArrFactors) == 1:

        return "1 and itself"

    return iArrFactors

def bIsPrimeNumber(iNum):

    iMidPoint = iNum // 2
    iDivisor = 2

    while iNum <= iMidPoint:

        if iNum % iDivisor == 0: return False

        if iDivisor != 2:

            iDivisor += 2

        else:

            iDivisor += 1

    return True