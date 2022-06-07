# Areas
def iAreaRectangle(iLength, iWidth):

    return iLength * iWidth


def iAreaSquare(iSideLength):

    return iAreaRectangle(iSideLength)


def iAreaTriangle(iLength, iWidth):

    return 1 / 2 * iLength * iWidth


def iAreaTriangleHeron(iSide_A, iSide_B, iSide_C):

    iSemiPerimeter = (iSide_A + iSide_B + iSide_C) / 2

    return iSqrt(iSemiPerimeter * iDiff(iSemiPerimeter, iSideA) * iDiff(iSemiPerimeter, iSideB) * iDiff(iSemiPerimeter, iSideC))


