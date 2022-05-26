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

    print("{}x^2 + {}x + {}".format(iQuadCoeff, iLinearCoeff, iCompleteTheSquareTerm(iQuadCoeff, iLinearCoeff)))