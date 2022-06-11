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

    if type(iNum) != int:

        iNum = round(iNum, 0) if iNum.isnumeric() else return "Not a number!"

    if iNum < 0:

        return "Must be a positive integer!" 

    iResult = 1

    while iNum != 0:

        iResult *= iNum
        iNum -= 1

    return iResult


def iReciprical(iNum):

    if iNum != 0:

        return iRatio(1, iNum)

    return "ERROR! DIV/0"


def iScientificNotation(iCoeff, iPower):

    return iPolynomialTerm(iCoefficient, 10, iPower)


def iBinaryNotation(iPower):

    return iPolyNomialTerm(1, 2, iPower)


def iPercent(iDec):

    return iPolynomialTerm(100, iDec)


def iPolynomialTerm(iCoefficient, iBase, iPower = 1):

    return iCoefficient * (iBase ** iPower)


def iSumOverProduct(iArrNums):

    iSum  = sum(iArrNums)
    
    iProd = 1
    
    for iNum in range(len(iArrNums)):

        iProd *= iArrNums[iNum] if iArrNums[iNum] != 0 else iProd = iProd

    return iRatio(iSum, iProd)


def sAddFractions(iNum_1, iDen_1, iNum2, iDen_2, bDebug = False):

    print("Fractions: {} / {} + {} / {}".format(iNum_1, iDen_1, iNum_2, iDen_2))

    iFractMult_1 = iArrFactorsofNum(iDen_1)
    iFractMult_2 = iArrFactorsofNum(iDen_2)

    # Creates Factors and Find Correct Multiplier:
    

    # Multiply Numerator


def iMaxPerimeterForArea(iArea):

    return 2 * (iArea + 1)


def iMinPerimeterForArea(iArea):

    return 2 * math.sqrt(iArea)


def iConvertToBinary(iNum):

    if not iNum.isnumeric():

        print("Not a number!")
        return -1

    iBinaryPower = 1

    while iNum > 0:

        iArrBinaryOutput = []

        while iBinaryNotation(iBinaryPower) <= iNum:

            iBinaryPower +=1
            iArrBinaryOutput.append(0)

        # Next Step: Compare the length of the array to the power


        


        




# Print Return Statements

def sCompoundFraction(iDec):

    iWholeNum = 0

    while iDec > 1:

        iWholeNum += 1
        iDec -= 1

    sFraction = sTransformDecToFraction(iDec)
    print("{} + {}".format(int(iWholeNum), sFraction))


def sAddByCounting(iNum_1, iNum_2, bDebug = False):

    if type(iNum_1) != int or type(iNum_2) != int:

        print("Please use integers!")
        return

    iAddCount = 0

    while iAddCount <= iNum2:

        iAddCount += 1
        iIntermediateSum = iNum_1 + iAddCount

        print("{} was added to {} to create {}}".format(iAddCount, iNum_1, iIntermediateSum))


def sSubtractByCounting(iNum_1, iNum_2, bDebug = False):

    if type(iNum_1) != int or type(iNum_2) != int:   #DRY!

        print("Please use integers!")
        return

    iSubtractCount = 0

    while iSubtractCount <= iNum_2:

        iSubtractCount += 1
        iIntermediateDiff = iNum_1 - iSubtractCount

        print("{} was taken away from {} to create {}}".format(iSubtractCount, iNum_1, iIntermediateDiff))


def sMultiplyByAdding(iNum_1, iNum_2, bDebug = False):

    if type(iNum_1) != int or type(iNum_2) != int:   #DRY!

        print("Please use integers!")
        return

    iMultCount = 0

    while iMultCount <= iNum2:

        iMultCount += 1
        iIntermediateProduct = iNum_1 + iMultCount * iNum_2

        print("{} was added to {} to create {}}".format(iMultCount, iNum1, iIntermediateProduct))