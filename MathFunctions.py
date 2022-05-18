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


