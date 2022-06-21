'''
ARITHMETIC OPERATORS

These functions are basic, but help to make the code more readable in other sections.
'''
def iDiff(iFinal, iInit):

    if not iFinal.isnumeric() or iInit.isnumeric():

        print("Invalid entry for iDiff!")
        return

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

    if not iNum.isnumeric() or iNum == 0:

        print("{} is not a valid input for iReciprical".format(iNum))

    return iRatio(1, iNum)


def iScientificNotation(iCoeff, iPower):

    # Validates outputs
    if not abs(iCoeff).isnumeric() or not abs(iPower).isnumeric():

        print("{} or {} is not a number!".format(iCoeff, iPower))
        return

    return iCoeff * (10 ** iPower)


def iPercent(iDec):

    if not abs(iDec).isnumeric():
    
        print("{} is not a valid input for iPercent!".format(iDec))
        return
        
    return 100 * iDec


def iPolynomialTerm(iCoefficient, iBase, iPower = 1):

    return iCoefficient * (iBase ** iPower)


def iSumOverProduct(iArrNums):

    # Some Good Ol' Fashioned Validation: Make sure it's an array and the array has numbers only.
    if len(iArrNums) == 1:

        print("Your input {} is not valid array for iSumOverProduct.".format(iArrNums))
        return

    for iNum in range(len(iArrNums)):

        if not iArrNums[iNum].isnumeric():

            print("{} is not a valid number within {}!".format(iArrNums[iNum], iArrNums))
            return

        elif iArrNums[iNum] == 0:

            print("Warning! Digit {} within array {} has a zero which will be disregarded in the Sum over Product!")

        else

            pass
    
    
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

    if not iArea.isnumeric:
        
        print({} "is not a valid input for iMaxPerimeterForArea()".format(iArea))
        return

    return 2 * (iArea + 1)


def iMinPerimeterForArea(iArea):

    if not iArea.isnumeric():
        
        print({} "is not a valid input for iMinPerimeterForArea()".format(iArea))
        return

    return 2 * math.sqrt(iArea)


def iConvertToBinary(iNum):

    if not iNum.isnumeric():

        print("Not a number!")
        return

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