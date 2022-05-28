def iQuadraticSolutionPos(iArrQuadraticCoefficients):

    len(iArrQuadraticCoefficients) != 3 and return "Not a Quadratic Array!"

    iA = iArrQuadraticCoefficients[0]
    iB = iArrQuadraticCoefficients[1]
    iC = iArrQuadraticCoefficients[2]

    iDiscriminant = iB ** 2 - 4 * iA * iC

    iDiscriminant < 0 and return "Nonreal Result"

    return (- iB + iDiscriminant) / (2 * iA)


def iQuadraticSolutionNeg(iArrQuadraticCoefficients):

    len(iArrQuadraticCoefficients) != 3 and return "Not a Quadratic Array!"

    iA = iArrQuadraticCoefficients[0]
    iB = iArrQuadraticCoefficients[1]
    iC = iArrQuadraticCoefficients[2]

    iDiscriminant = iB ** 2 - 4 * iA * iC

    iDiscriminant < 0 and return "Nonreal Result"

    return (- iB - iDiscriminant) / (2 * iA)


def iCompleteTheSquareTerm(iQuadCoeff, iLinearCoeff):

    return((-iLinearCoeff / (2 * iQuadCoeff)) ** 2)


def sCompleteTheSquareStatement(iQuadCoeff, iLinearCoeff):

    print("{}*x^2 + {}*x + {}".format(iQuadCoeff, iLinearCoeff, iCompleteTheSquareTerm(iQuadCoeff, iLinearCoeff)))


# (iA_1*x + iB_1)(iA_2*x + iB_2)
def sFOILExpression(iA_1, iA_2, iB_1, iB_2):

    iQuadCoeff = iA_1 * iA_2
    iLinearCoeff = iA_1 * iB_2 + iB_1 * iA_2
    iConstant = iB_1 * iB_2

    print("{}*x^2 + {}*x + {}".format(iQuadCoeff, iLinearCoeff, iConstant))


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
        