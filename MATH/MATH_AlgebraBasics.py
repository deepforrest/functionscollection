# Functions

def bIsAFunction(iArrInputs, iArrOutputs):

    if len(iArrInputs) != len(iArrOutputs):

        print("Input and output arrays have different lengths!")
        print("Input: {} has length of {}".format(iArrInputs, len(iArrInputs)))
        print("Output: {} has length of {}".format(iArrOutputs, len(iArrOutputs)))
        return

    iArrs = [iArrInputs, iArrOutputs]

    for iArr in iArrs:

        for iAgent in iArr:

            if not isinstance(iArr[iAgent], (int, float)):

                print("{} is not a valid input for analysis!".format(iArr[iAgent]))

    
    # Next, need to write code that analyzes the inputs for duplicates.


    for iIndNum in iArrInputs:

        iIndNum_2 = iIndNum + 1

        while iIndNum_2 < len(iArrInputs):

            


# Linear Equations

def iTangentOfPoints(iX_2, iX_1, iY_2, iY_1):

    iDelta_X = iDiff(iX_2, iX_1)
    iDelta_Y = iDiff(iY_2, iY_1)

    if iDelta_X != 0:
        
        return iRatio(iDelta_Y, iDelta_X)


# Quadratic Solution Definitions

def iQuadraticDiscriminant(iA, iB, iC):

    return iB ** 2 - 4 * iA * iC

def sNoOfRealQuadraticSolutions(iArrQuadraticCoefficients):

    iA = iArrQuadraticCoefficients[0]
    iB = iArrQuadraticCoefficients[1]
    iC = iArrQuadraticCoefficients[2]

    iDiscriminant = iQuadraticDiscriminant(iA, iB, iC)

    return "Two Solutions" if iDiscriminant > 0 else "No Real Solution" if iDiscriminant < 0 else "One Solution"


def iQuadraticSolutionPos(iArrQuadraticCoefficients):

    if len(iArrQuadraticCoefficients) != 3: 
        
        return "Not a Quadratic Array!"


    for iCoeff in iArrQuadraticCoefficients:

        if not iCoeff.isnumeric():

            return "Nonnumber detected in array."


    iA = iArrQuadraticCoefficients[0]
    iB = iArrQuadraticCoefficients[1]
    iC = iArrQuadraticCoefficients[2]

    iDiscriminant = iQuadraticDiscriminant(iA, iB, iC)

    return iRatio(- iB + iDiscriminant, 2 * iA)


def iQuadraticSolutionNeg(iArrQuadraticCoefficients):

    if len(iArrQuadraticCoefficients) != 3: 
        
        return "Not a Quadratic Array!"

    
    for iCoeff in iArrQuadraticCoefficients:

        if not iCoeff.isnumeric():

            return "Nonnumber detected in array."


    iA = iArrQuadraticCoefficients[0]
    iB = iArrQuadraticCoefficients[1]
    iC = iArrQuadraticCoefficients[2]

    iDiscriminant = iQuadraticDiscriminant(iA, iB, iC)

    return iRatio(- iB - iDiscriminant, 2 * iA)


def iQuadraticSolutionArray(iArrQuadraticCoefficients):

    return [iQuadraticSolutionPos(iArrQuadraticCoefficients), iQuadraticSolutionNeg(iArrQuadraticCoefficients)]


# Completing The Square

def iTerm_CompleteTheSquare(iQuadCoeff, iLinearCoeff):

    return((iLinearCoeff / (2 * iQuadCoeff)) ** 2)


def sCompleteTheSquareStatement(iQuadCoeff, iLinearCoeff):

    print("{}*x^2 + {}*x + {}".format(iQuadCoeff, iLinearCoeff, iTerm_CompleteTheSquare(iQuadCoeff, iLinearCoeff)))


# (iA_1*x + iB_1)(iA_2*x + iB_2)
def sFOILExpression(iA_1, iA_2, iB_1, iB_2):

    iQuadCoeff = iA_1 * iA_2
    iLinearCoeff = iA_1 * iB_2 + iB_1 * iA_2
    iConstant = iB_1 * iB_2

    print("{}*x^2 + {}*x + {}".format(iQuadCoeff, iLinearCoeff, iConstant))


# Unfinished
def sFactorTrinomial(iArrTrinomialCoeff, bDebug = False):

    if len(iArrTrinomialCoeff) != 3: 

        return "Not a trinomial set of coefficients!"

    for iCoeff in iArrTrinomialCoeff:

        if type(iArrTrinomialCoeff[iCoeff]) != int:

            return "Noninteger detected!"

    bDebug and print("{} x^2 + {} x + {}".format(iArrTrinomialCoeff[0], iArrTrinomialCoeff[1], iArrTrinomialCoeff[2]))

    iQuadTerm = iArrTrinomialCoeff[0]
    iLinearTerm = iArrTrinomialCoeff[1]
    iConstTerm = iArrTrinomialCoeff[2]

    # Midpoints
    iA_MP = round(iSqrt(iQuadTerm), 0)
    iB_MP = round(iSqrt(iConstTerm), 0)
    
    # Baseline Points to Start The Factoring Process.
    iA_1 = iA_MP
    iA_2 = iA_MP

    iB_1 = iB_MP
    iB_2 = iB_MP

    iMP_Smallest = min(iA_MP, iB_MP)

    # WORKSHOP!
    while iMP_Smallest > 0:

        # Initialization Conditions

        while iB_2 <= iConstTerm:

            iTestQuadTerm = iA_1 * iA_2
            iTestLinearTerm = iA_1 * iB_2 + iA_2 * iB_1
            iTestConstTerm = iB_1 * iB_2

            iArrTestCoeff = [iTestQuadTerm, iTestLinearTerm, iTestConstTerm]

            if iArrTestCoeff = iArrTrinomialCoeff:

                sLHS = "{} x^2 + {} x + {}".format(iTestQuadTerm, iTestLinearTerm, iTestConstTerm)
                sRHS = "({}x + {})({}x + {}".format(iA_1, iA_2, iB_1, iB_2)

                print(sLHS + " = " sRHS)
                return

            iB_2 += 1

        iMP_Smallest -= 1
        