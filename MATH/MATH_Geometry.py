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

    return iPolynomialTerm(iReciprical(2), iLength * iWidth)


def iAreaTriangleHeron(iSide_A, iSide_B, iSide_C):

    iSemiPerimeter = iRatio(iSide_A + iSide_B + iSide_C, 2)
    iProductofDiffs = iDiff(iSemiPerimeter, iSideA) * iDiff(iSemiPerimeter, iSideB) * iDiff(iSemiPerimeter, iSideC)

    return iSqrt(iSemiPerimeter * iProductofDiffs)


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


# --------------------------- 2D -- GEOMETRY -- ADVANCED --------------------------- #

def iAreaFlatRing_Radius(iOuterRadius, iInnerRadius):

    return iAreaCircle_Radius(iOuterRadius) - iAreaCircle_Radius(iInnerRadius)


def iAreaFlatRing_Diameter(iOuterDiameter, iInnerDiameter):

    return iAreaCircle_Diameter(iOuterDiameter) - iAreaCircle_Diameter(iInnerDiameter)

# --------------------------- 3D -- GEOMETRY -- SURFACE - AREA --------------------------- #

def iSurfaceAreaEllipsoid_Radius(iRadius_X, iRadius_Y, iRadius_Z):

    iKTF_Exp = 1.6075  # With Knud Thompson's Formula
    iKTF_Coeff = 4 * iPi

    iKTF_TermXY = iPolynomialTerm(1, iRadius_X * iRadius_Y, iKTF_Exp)
    iKTF_TermYZ = iPolynomialTerm(1, iRadius_Y * iRadius_Z, iKTF_Exp)
    iKTF_TermXZ = iPolynomialTerm(1, iRadius_X * iRadius_Z, iKTF_Exp)

    iArrKTFTerms = [iKTF_TermXY, iKTF_TermYZ, KTF_TermXZ]

    iKTF_AvgOfTerms = sum(iArrKTFTerms) / len(iArrKTFTerms)

    return iPolynomialTerm(iKTF_Coeff, iKTF_AvgOfTerms, iReciprical(iKTF_Exp))


def iSurfaceAreaEllipsoid_Diameter(iDiameter_X, iDiameter_Y, iDiameter_Z):

    iRadius_X = iRatio(iDiameter_X, 2)
    iRadius_Y = iRatio(iDiameter_Y, 2)
    iRadius_Z = iRatio(iDiameter_Z, 2)

    return iSurfaceAreaEllipsoid_Radius(iRadius_X, iRadius_Y, iRadius_Z)

# --------------------------- 3D -- GEOMETRY -- VOLUME --------------------------- #

def iVolumeCylinder_Radius(iRadius, iHeight):

    return iAreaCircle_Radius(iRadius) * iHeight


def iVolumeCylinder_Diameter(iDiameter, iHeight):

    return iAreaCircle(iDiameter) * iHeight


def iVolumeParallelepiped(iSide_A, iSide_B, iSide_C):

    return iSide_A * iSide_B * iSide_C


def iVolumeCube(iSide):

    return iVolumeParallelepiped(iSide, iSide, iSide)


def iVolumeCuboid(iSide_Square, iSide_Depth):

    return iAreaSquare(iSide_Square) * iSide_Depth


def iVolumePyramidSquare(iSide_Square, iSide_Height):

    return iRatio(iSideSquare(iSide_Square) * iSide_Height, 3)


def iVolumeEllipsoid_Radius(iRadius_X, iRadius_Y, iRadius_Z):

    return iRatio(4 * iPi * iRadius_X * iRadius_Y * iRadius_Z, 3)


def iVolumeEllipsoid_Diameter(iDiameter_X, iDiameter_Y, iDiameter_Z):

    return iRatio(iPi * iDiameter_X * iDiameter_Y * iDiameter_Z, 6)


def iVolumeSphere_Radius(iRadius):

    return iVolumeEllipsoid_Radius(iRadius, iRadius, iRadius)


def iVolumeSphere_Diameter(iDiameter):

    return iVolumeEllipsoid_Diameter(iDiameter, iDiameter, iDiameter)