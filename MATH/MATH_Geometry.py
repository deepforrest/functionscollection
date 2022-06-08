iPi = math.pi()

# Sides
def iLengthSide_Square(iArea):

    return iSqrt(iArea)


def iLengthSide_Rectangle(iArea, iLength):

    return iRatio(iArea, iLength)


def iLengthDimension_Triangle(iArea, iLength):

    return 2 * iRatio(iArea, iLength)

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


def iAreaTrapezoid(iSide_A, iSide_B, iDistances_Sides_AB):

    return iRatio(iSide_A + iSide_B, 2) * iDistances_Side_AB


def iAreaEllipse_Radii(iRadius_Long, iRadius_Short):

    return iPi * iRadius_Long * iRadius_Short


def iAreaEllipse_Diameters(iDiameter_Long, iDiameter_Short):

    return iPi * iRatio(iDiameter_Long, 2) * iRatio(iDiameter_Short, 2)


def iAreaCircle_Radius(iRadius):

    return iAreaEllipse_Radii(iRadius, iRadius)


def iAreaCircle_Diameter(iDiameter):

    return iAreaEllipse_Diameter(iDiameter, iDiameter)

# --------------------------- 3D -- GEOMETRY --------------------------- #