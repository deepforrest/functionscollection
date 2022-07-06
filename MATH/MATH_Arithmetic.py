'''

I - ARITHMETIC OPERATORS

    These functions are basic, but help to make the code more readable in other sections.

A - Coding Philosophy
    A wise programmer once said:
    "Your code should explain your comments to the computer..."

    and so you shall see in the code below.

B - codeCase Used

    The codeCase I use is called sTypeCase, which identifies the expected data type for the variable within the first letter:

        - b: Boolean
        - i: Numeric
        - s: String
        - v: Variants (Usually with Arrays)

    If there is an Array/List involved, it is denoted after the data type with Arr, such as vArr, sArr, iArr, etc.

'''

from PROG_GenFunctions import bValidateInputs

# Part 1 - Elementary Functions

def iDiff(iFinal, iInit):

    ''' 
    While this function may seem silly at first glance, I've created it for several reasons:

        1 - To reduce my operators shown down to only '+'s,
        2 - To ensure that order of operations are always fully followed
        3 - To help with reference calculations in engineering, and
        4 - To make code more readable from left to right and not worrying about match parentheses
    '''

    # 1 - Validation of Inputs
    iArrInputs = [iFinal, iInit]

    # 2 - Calculate Result
    return if bValidateInputs(iArrInputs, "iDiff") else return (iFinal - iInit)


def iRatio(iNum, iDen):

    ''' 
        While this function may also seem silly at first glance, I've created it for several reasons:

        1 - To reduce my operators down to only '+'s,
        2 - To ensure that order of operations are always fully followed
        3 - To make code more readable from left to right and not worrying about match parentheses

    '''

    # 1 - Validation of Inputs
    iArrInputs = [iNum, iDen]

    # Checks for Nonnumeric inputs
    if !bValidateInputs(iArrInputs, "iRatio"):

        return # Kill Statement

    # Divide by Zero Issues
    if iDen == 0:

        print("Denominator cannot be {} for iRatio!".format(iDen))
        return # Kill Statement

    return (iNum / iDen)


def iFactorial(iNum, bConvertNegative = True):

    # 1 Validation of Inputs

    # First checks to make sure it is an integer
    if not isinstance(iNum, int):

        # Checks to make sure the number is at least a float, and if not, aborts the function.
        if not isinstance(iNum, float): 
            
            print("{} is not a number!".format(iNum))
            return # Kill Statement 

        # Attempts to Redeem Float By Converting It Into an Integer Required for Factorial Calculations
        iNum = int(iNum)

    # Next, check to make sure the number is positive, and if not, convert it unless overridden in function inputs
    if iNum < 0 and bConvertNegative:

        print("{} converted to a positive number!".format(iNum))
        iNum = -iNum

    # Usually only happens if the user explicitly says do not convert.
    else

        print("{} cannot be a negative number in iFactorial!".format(iNum))
        return # Kill Statement

    # Baseline Starting Point because 1 * n = n
    iResult = 1

    # A Factorial Calculation is given as n * (n - 1) * (n - 2) ... (n - (n - 2) * (n - (n - 1)))
    # Function stops at 1 instead of 0 because multiplying by 1 is meaningless.
    while iNum != 1:

        iResult *= iNum
        iNum -= 1

    # Once iNum reaches 1, the result is ready for return
    return iResult


def iReciprical(iNum):

    # Validation of Inputs
    if not isinstance(iNum, (int, float)):

        print("{} is not a valid input for iReciprical".format(iNum))
        return

    # Shows 
    if iNum == 0:

        print("{} has an indeterminant reciprocal!".format(iNum))
        return

    # Calculates from iRatio as 1 / iNum
    return iRatio(1, iNum)


def iPolynomialTerm(iCoeff, iBase, iPower = 1):

    # Setup for Validation of Inputs
    iArrInputs = [iCoeff, iBase, iPower]

    return iCoeff * (iBase ** iPower) if bValidateInputs(iArrInputs, "iPolynomialTerm") else return


def iScientificNotation(iCoeff, iPower):

    # Validation taken care of in next step
    return iPolynomialTerm(iCoeff, 10, iPower)


def iPercent(iDec):

    if not isinstance(iDec, (int, float)):
    
        print("{} is not a valid input for iPercent!".format(iDec))
        return
        
    return 100 * iDec


def iSumOverProduct(iArrNums):

    # Some Good Ol' Fashioned Validation: Make sure it's an array and the array has numbers only.
    if len(iArrNums) == 1:

        print("Your input {} is not valid array for iSumOverProduct.".format(iArrNums))
        return

    for iNum in range(len(iArrNums)):

        if not isinstance(iArrNums[iNum], (int, float)):

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

    # 1 - Validation to ensure inputs are numeric
    iArrInputs = [iNum_1, iDen_1, iNum_2, iDen_2]

    if !bValidateInputs(iArrInputs, "sAddFractions"):

        return
    
    # 2 - Transformative Process From Float to Integers, which is the definition of a rational num
    iArrFract_1 = [iNum_1, iDen_1]
    iArrFract_2 = [iNum_2, iDen_2]
    iArrFracts = [iArrFract_1, iArrFract_2]

    for iFract in range(len(iArrFracts)):

        # Put Validation Function here, if possible
        for iNum in range(len(iFract)):

            if not isinstance(iNum, int):

                # Do something here to transform them into decimaless integers

    print("Validation Complete:\nFractions: {} / {} + {} / {}".format(iNum_1, iDen_1, iNum_2, iDen_2))

    iFractMult_1 = iArrFactorsofNum(iDen_1)
    iFractMult_2 = iArrFactorsofNum(iDen_2)

    # Creates Factors and Find Correct Multiplier:
    

    # Multiply Numerator


def iMaxPerimeterForArea(iArea):

    if not isinstance(iArea, (int, float)):
        
        print({} "is not a valid input for iMaxPerimeterForArea()".format(iArea))
        return

    return 2 * (iArea + 1)


def iMinPerimeterForArea(iArea):

    if not isinstance(iArea, (int, float)):
        
        print({} "is not a valid input for iMinPerimeterForArea()".format(iArea))
        return

    return 4 * math.sqrt(iArea)


def iConvertDecToBinary(iNum):

    if not isinstance(iNum, (int, float)):

        print("{} is not a valid number for binary!".format(iNum))
        return

    iExp = 0

    iComparator = iPolynomialTerm(1, 2, iExp)
    iArrBinary = []

    while iComparator < iNum:

        iExp += 1
        iComparator = iPolynomialTerm(1, 2, iExp)


    if type(iNum) == int or iNum == int(iNum):

        while iComparator > 0:

            if iComparator > iNum:

                iArrBinary.append(0)

            else: 
                
                iArrBinary.append(1)
                iNum -= iComparator

            iExp -= 1
            iComparator = iPolynomialTerm(1, 2, iExp)

        return iArrBinary

    if type(iNum) == float:

        # Set up code to have two bounds to look for
        iComparatorMax = iComparator
        iComparatorMid = 0
        # iComparatorMin = -infinity
            
    
# Print Return Statements

def sCompoundFraction(iDec):

    if not isinstance(iDec, (int, float)):

        print("{} is not a valid input for sCompoundFraction!")
        return

    if type(iDec) == int:

        print("Input is already an integer:\n{} / 1".format(iDec))
        return 


    # Post Validation
    # Is the code below legit?
    iWholeNum = 0

    while iDec > 1:

        iWholeNum += 1
        iDec -= 1

    sFraction = sTransformDecToFraction(iDec)
    print("{} + {}".format(int(iWholeNum), sFraction))


def iAddForwardSubtractBackward(iNumAdd, iNumSub, iNum_Start, iNum_Stop, bPrint = False):

    iArrInputs = [iNumAdd, iNumSub, iNum_Start, iNum_Stop]

    bValidateInputs(iArrInputs, "iAddForwardSubtractBackward")

    # More Validation Steps are Needed For This Function To Ensure No Inf Loops

    bInfLoop = True

    if iNumAdd > iNumSub:

        if iNumStop > iNumStart:

            bInfLoop = False

    if iNumAdd < iNumSub:

        if iNumStop < iNumStart:

            bInfLoop = False

    # Start of Function
    iNum = iNum_Start
    iCounter = 0

    while iNum < iNum_Stop and !bInfLoop:

        iNum += iNumAdd
        iNum -= iNumSub
        iCounter += 1

    bPrint and print("It took {} iterations to get from {} to {} by adding {} and subtracting {}".format(iCounter, iNum_Start, iNum_Stop, iNumAdd, iNumSub))





# CONTINUE HERE





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