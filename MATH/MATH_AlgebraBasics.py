# Functions

def bIsAFunction(iArrInputs, iArrOutputs, bDebug = False):

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

            if iArrInputs[iIndNum] == iArrInputs[iIndNum_2]:

                bDebug and print("{} is duplicated at indices {} & {}!".format(iArrInputs[iIndNum], iIndNum, iIndNum_2))
                return False

            iIndNum_2 += 1

    return True


# Linear Equations
def iTangentOfPoints(iX_2, iX_1, iY_2, iY_1):

    iArrInputs = [iX_2, iX_1, iY_2, iY_1]

    for iInput in iArrInputs:

        if not isinstance(iArrInputs[iInput], (int, float)):

            print("{} is a nonnumber and cannot be used for this function".format(iArrInputs[iInput]))
            return

    iDelta_X = iDiff(iX_2, iX_1)
    iDelta_Y = iDiff(iY_2, iY_1)

    if iDelta_X != 0:
        
        return iRatio(iDelta_Y, iDelta_X)


# Quadratic Solution Definitions

def iQuadraticDiscriminant(iA, iB, iC):

    iArrInputs = [iA, iB, iC]

    for iCoeff in iArrInputs:

        if not isinstance(iArrInputs[iCoeff], (int, float)):

            print("{} is not an appropriate coefficient!".format(iArrInputs[iCoeff]))

    return iDiff(iPolynomialTerm(1, iB, 2), iPolyTerm(4, iA * iC))


def sNoOfRealQuadraticSolutions(iA, iB, iC):

    iArrQuadraticCoefficients = [IA, iB, iC]

    iDiscriminant = iQuadraticDiscriminant(iA, iB, iC)  # Validation is contained within function

    return "Two Solutions" if iDiscriminant > 0 else "No Real Solution" if iDiscriminant < 0 else "One Solution"


def iQuadraticSolutionPos(iA, iB, iC):

    iArrQuadraticCoefficients = [iA, iB, iC]

    for iCoeff in iArrQuadraticCoefficients:

        if not isinstance(iArrQuadraticCoefficients[iCoeff], (int, float)):

            print("{} is not a number and cannot be used!".format(iArrQuadraticCoefficients[iCoeff]))
            return

    iDiscriminant = iQuadraticDiscriminant(iA, iB, iC)

    return iRatio(iDiff(iDiscriminant, iB), iPolynomialTerm(2, iA))


def iQuadraticSolutionNeg(iA, iB, iC):

    iArrQuadraticCoefficients = [iA, iB, iC]

    for iCoeff in iArrQuadraticCoefficients:

        if not isinstance(iArrQuadraticCoefficients[iCoeff], (int, float)):

            print("{} is not a number and cannot be used!".format(iArrQuadraticCoefficients[iCoeff]))
            return

    iDiscriminant = iQuadraticDiscriminant(iA, iB, iC)

    return iRatio(iDiff(-iDiscriminant, iB), iPolynomialTerm(2, iA))


def iArrQuadraticSolution(iA, iB, iC):

    iArrInputs = [iA, iB, iC]

    for iCoeff in iArrInputs:

        if not isinstance(iArrInputs[iCoeff], (int, float)):

            print("{} is not a usable input!".format(iArrInputs[iCoeff]))
            return

    iPosSol = iQuadraticSolutionPos(iA, iB, iC)
    iNegSol = iQuadraticSolutionNeg(iA, iB, iC)

    return [iPosSol, iNegSol]


# Completing The Square

def iTerm_CompleteTheSquare(iQuadCoeff, iLinearCoeff):

    iArrInputs = [iQuadCoeff, iLinearCoeff]

    for iCoeff in iArrInputs:

        if not isinstance(iArrInputs[iCoeff], (int, float)):

            print("{} is not a usable input!".format(iArrInputs[iCoeff]))
            return

    return iPolynomialTerm(iLinearCoefficient, iReciprical(iPolynomialTerm(2, iQuadCoeff)), 2)


def sCompleteTheSquareStatement(iQuadCoeff, iLinearCoeff):

    print("{}*x^2 + {}*x + {}".format(iQuadCoeff, iLinearCoeff, iTerm_CompleteTheSquare(iQuadCoeff, iLinearCoeff)))


# (iA_1*x + iB_1)(iA_2*x + iB_2)
def sFOILExpression(iA_1, iA_2, iB_1, iB_2):

    iArrInputs = [iA_1, iA_2, iB_1, iB_2]

    for iCoeff in iArrInputs:

        if not isinstance(iArrInputs[iCoeff], (int, float)):

            print("{} is not a valid input!".format(iArrInputs[iCoeff]))
            return

    iQuadCoeff = iPolynomialTerm(iA_1, iA_2)
    iLinearCoeff = iPolynomialTerm(iA_1, iB_2) + iPolynomialTerm(iB_1, iA_2)
    iConstant = iPolynomialTerm(iB_1, iB_2)

    print("{}*x^2 + {}*x + {}".format(iQuadCoeff, iLinearCoeff, iConstant))
    return [iQuadCoeff, iLinearCoeff, iConstant]


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
        