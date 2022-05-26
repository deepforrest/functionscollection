# Even though is a math.function, this is an exercise
# for myself in the event I take this into a different
# language that doesn't have such libraries.

def iFactorial(iNum):

    iResult = 1

    while iNum != 0:

        iResult *= iNum
        iNum -= 1

    return iResult

# Recipricals

def iReciprical(iNum):

    if iNum != 0:

        return 1 / iNum

    return "ERROR! DIV/0"

def iSciNot(iPower):

    return 10 ** iPower


# Numerical solution to a polynomial term according to the power rule
def iIntegratePolyTerm(iCoeff, iVar, iPower):

    iNewPower = iPower + 1

    return (iCoeff * (iVar ** iNewPower)) / iNewPower

# Numerical solution to a polynomial term according to the power rule
def iDifferentiatePolyTerm(iCoeff, iVar, iPower):

    iNewPower = iPower - 1

    return (iCoeff * iPower * (iVar ** iNewPower))

# Tested.  Returns an array of prime numbers that when multiplied together, create the original number.  Optimized for speed
def iArrFactorsOfNum(iNum):

    iOrigNum = int(iNum)
    iArrFactors = []
    iDivisor = 2

    while iDivisor <= iNum:

        #print ("Number = " + str(iNum))
        #print ("Divisor = " + str(iDivisor))

        while iNum % iDivisor == 0:

            iArrFactors.append(iDivisor)
            #print(str(iNum) + " is divisible by " + str(iDivisor))

            iNum /= iDivisor
            #print("\nNew Number: " + str(iNum))

        if iDivisor != 2:

            iDivisor += 2

        else:

            iDivisor += 1

    if len(iArrFactors) == 1:

        return [1, iOrigNum]

    return iArrFactors


def bIsPrimeNumber(iNum):

    iMidPoint = iNum // 2
    iDivisor = 2

    while iNum <= iMidPoint:

        if iNum % iDivisor == 0: return False

        if iDivisor != 2:

            iDivisor += 2

        else:

            iDivisor += 1

    return True


def bHasPrimeFactor(iNum, iFactor):

    iArrOfFactors = iArrFactorsOfNum(iNum)

    for iPrimeNo in range(len(iArrOfFactors)):

        if iArrOfFactors[iPrimeNo] == iFactor:

            return True
        
    return False


def iArrBreakDigits(iNum):

    return int(iDigits) for iDigits in str(iNum)


def bDiffRequiresBorrowing(iLargerNum, iSmallerNum):

    if iLargerNum =< iSmallerNum return False

    # Turn numbers into arrays and analyze them from right to left
    iArrSNum = iArrBreakDigits(iSmallerNum)
    iArrLNum = iArrBreakDigits(iLargerNum)

    # print(iArrSSum + " vs. " + iArrLSum)

    iArrSNLen = len(iArrSNum) - 1
    iArrLNLen = len(iArrLNum) - 1

    # Needs to iterate R to L.

    while iArrSNLen >= 0:

        if iArrSNum[iArrSNLen] > iArrLNum[iArrLNLen]:

            return True

        iArrSNLen -= 1
        iArrLNLen -= 1

    return False


def bAddRequiresCarryingDigits(iLargerNum, iSmallerNum):

    # Switches inputs in the event they were entered out of order
    if iLargerNum < iSmallerNum:

        iLargerNum, iSmallerNum = iSmallerNum, iLargerNum

    iArrSNum = iArrBreakDigits(iSmallerNum)
    iArrLNum = iArrBreakDigits(iLargerNum)

    # Provides indices of right most index
    iArrSNLen = len(iArrSNum) - 1
    iArrLNLen = len(iArrLNum) - 1

    # Needs to iterate R to L, and only on the smallest number.
    while iArrSNLen >= 0:

        if iArrSNum[iArrSNLen] + iArrLNum[iArrLNLen] > 10:

            return True

        iArrSNLen -= 1
        iArrLNLen -= 1

    return False

# Converts an angle in the DMS (Degree, Minute, Second) system as a float.
def iDegDec(iDeg, iMin, iSec = 0):

    return iDeg + iMin / 60 + iSec / (60 ** 2)


def iDegToMin(iDeg):

    return 60 * round(iDeg - math.floor(iDeg), 4)


def iDegToSec(iDeg):

    iDegDec = iDegToMin(iDeg)
    return int(round(iDegDec - math.floor(iDegDec), 4) * 60)


# Returns a side of a triangle, given another side, its corresponding angle, and the other side's angle.
def iSideLawofSins(iSideB, iAngleA, iAngleB):

    iAngleA *= iConvDegToRad
    iAngleB *= iConvDegToRad

    return math.sin(iAngleA) * iSideB / math.sin(iAngleB)


def iAngleLawofSins(iSideA, iSideB, iAngleB):

    iAngleB *= iConvDegToRad

    return math.asin(iSideA * math.sin(iAngleB) / iSideB) * iConvDegToRad


def iSideLawOfCosines(iSideA, iSideB, iAngleCDeg, sType = "Deg"):

    if sType == "Deg":
        
        iAngleC = iConvDegToRad * iAngleCDeg

    return math.sqrt(iSideA ** 2 + iSideB ** 2 - 2 * iSideA * iSideB * math.cos(iAngleC))


def iAngleLawofCosines(iSideA, iSideB, iSideC, sType = "Deg"):

    iAngle = math.acos((iSideC ** 2 - (iSideA ** 2 + iSideB ** 2)) / (-2 * iSideA * iSideB))
    
    if sType != "Rad":

        iAngle /= iConvDegToRad 

    return iAngle


def iCalcResultVect(iVectorMag01, iVectorMag02, iAngleBetween, sAngleType = "Deg", bDebug = False):

    iNewAngle = iCalcSupplementaryAngle(iAngleBetween)

    if bDebug:
        
        print("New angle = " + str(iNewAngle))

    if sAngleType != "Deg":

        return iSideLawOfCosines(iVectorMag01, iVectorMag02, iNewAngle, "Rad")        

    return iSideLawOfCosines(iVectorMag01, iVectorMag02, iNewAngle, "Deg")


def iCalcComplementaryAngle(iAngle):

    return 90 - iAngle


def iCalcSupplementaryAngle(iAngle):

    return 180 - iAngle


def iCalcThirdAngle(iAngle01, iAngle02)

    iKnownAngles = [iAngle01, iAngle02]
    
    return 180 - sum(iKnownAngles)


def sReduceFractionByFactoring(iNum, iDen, bDebug = False):

    iOrigNum = iNum
    iOrigDen = iDen

    # Calculate Factors of Numerator and Denominator from Factor Array Function:
    iArrNumFactors = iArrFactorsOfNum(iNum)
    iArrDenFactors = iArrFactorsOfNum(iDen)

    bDebug and print("\nStep 1 - Find Factors of Numerator and Denominator")
    bDebug and print("Factors of {}: {}".format(iNum, iArrNumFactors))
    bDebug and print("Factors of {}: {}".format(iDen, iArrDenFactors))

    # Create A Whole New Array of Relevant Prime Numbers to Iterate Through:
    iArrAllFactors = []

    bDebug and print("\nStep 2a - Add The Numbers The All Factor Array from Num:")
    # Function Needs To Optimally Iterate Through All Factors and Add Nonduplicates
    for iFactor in iArrNumFactors:

        iArrAllFactors.append(iFactor)
        bDebug and print("Updated All Factors Array: {} ".format(iArrAllFactors))

    bDebug and print("\nStep 2b - Add The Numbers The All Factor Array from Num:")

    for iFactors in iArrDenFactors:

        iArrAllFactors.append(iFactors)
        bDebug and print("Updated All Factors Array: {} ".format(iArrAllFactors))


    bDebug and print("\nStep 3 - Sort All Numbers:")
    iArrAllFactors.sort()

    bDebug and print("Sorted Array: {}".format(iArrAllFactors))
    iArrIndex = 1
    iArrIter = 0

    # Removes Duplicates
    bDebug and print("\nStep 4 - Remove Duplicates Within Array:")
    while iArrIndex <= len(iArrAllFactors) - 1:

        iArrIter += 1
        bDebug and print("\nMaster Array Iteration: {}".format(iArrIter))
        bDebug and print("Current Length of Array: {} ".format(len(iArrAllFactors)))

        while iArrAllFactors[iArrIndex] == iArrAllFactors[iArrIndex - 1] and len(iArrAllFactors) > 1:

            bDebug and print("\nFactor {} at Index {} = Factor {} at Index {}".format(iArrAllFactors[iArrIndex], iArrIndex, iArrAllFactors[iArrIndex - 1], iArrIndex - 1))
            
            iArrIndex -= 1
            iArrAllFactors.pop(iArrIndex)

            if iArrIndex < 0: iArrIndex = 0
            
            bDebug and print("\nDuplicate Factor {} removed at Index {}".format(iArrAllFactors[iArrIndex], iArrIndex))
            bDebug and print("Updated List: {}".format(iArrAllFactors))

        iArrIndex += 1

    # Analysis of which has the most of each factor:

    bDebug and print("\nReduced Array: {}".format(iArrAllFactors))

    iArrNumReducedFactors = [1]
    iArrDenReducedFactors = [1]
    iMasterFactor = 0

    bDebug and print("\nStep 5 - Compare Number of Factors in Num/Den While Iterating Through Master Array")

    while iMasterFactor <= len(iArrAllFactors) - 1:
        
        bDebug and print("\nFactor: {}".format(iArrAllFactors[iMasterFactor]))
        bDebug and print("\nFactors Array Length: {} with Index {}".format(len(iArrAllFactors), iMasterFactor))


        # Initialization of Counters for Each Factor
        iNumCount = 0
        iDenCount = 0

        # Iterate Through Numerator
        for iFactNum in range(len(iArrNumFactors)):

            bDebug and print("\nMaster Factor Index: {}  \nNum Factor Index {}".format(iMasterFactor, iFactNum))
            bDebug and print("\nMaster Array Length: {}  \nNum Array Length {}".format(len(iArrAllFactors), len(iArrNumFactors)))
            # bDebug and print("\nRangeLen = {}".format(range(len(iArrNumFactors))))            
            if iArrAllFactors[iMasterFactor] == iArrNumFactors[iFactNum]:

                iNumCount += 1
                bDebug and print("Numerator has factor of {}".format(iArrAllFactors[iMasterFactor]))

            bDebug and print("\nNumber of {} Factors in Numerator = {}".format(iArrAllFactors[iMasterFactor], iNumCount))

        # Iterate Through Denominator
        for iFactDen in range(len(iArrDenFactors)):

            if iArrAllFactors[iMasterFactor] == iArrDenFactors[iFactDen]:

                iDenCount += 1
                bDebug and print("Denominator has factor of {}".format(iArrAllFactors[iMasterFactor]))
                
            bDebug and print("\nNumber of {} factors in denominator = {}".format(iArrAllFactors[iMasterFactor], iDenCount))

        iCountDiff = abs(iNumCount - iDenCount)
    
        bDebug and print("\nStep 6 - Compare Numerator and Denominator Counts of The Factor {}".format(iArrAllFactors[iMasterFactor]))
        bDebug and print("Num Count: {} \nDen Count: {}".format(iNumCount, iDenCount))
        bDebug and print("Absolute Difference = {}".format(iCountDiff))


        if iNumCount > iDenCount:

            bDebug and print("\nNumerator has highest count of Factor: {}".format(iArrAllFactors[iMasterFactor]))
            bDebug and print("and will be added {} times".format(iCountDiff))

            while iCountDiff != 0:

                iArrNumReducedFactors.append(iArrAllFactors[iMasterFactor])
                iCountDiff -= 1

        elif iNumCount < iDenCount:
            
            bDebug and print("\nDenominator has highest count of Factor: {}".format(iArrAllFactors[iMasterFactor]))
            bDebug and print("and will be added {} times".format(iCountDiff))

            while iCountDiff != 0:

                iArrDenReducedFactors.append(iArrAllFactors[iMasterFactor])
                iCountDiff -= 1

        else:

            bDebug and print("Num and Den have the same amount of {}s.  Factor discarded.".format(iArrAllFactors[iMasterFactor]))
            pass

        iMasterFactor += 1

        bDebug and print("\nUpdated Arrays:")
        bDebug and print("Num Factor Array: {}".format(iArrNumReducedFactors))
        bDebug and print("Den Factor Array: {}".format(iArrDenReducedFactors))

    # Finally, take the product of the new factors on num and den and return string
    
    bDebug and print("\nFinal Reduced Arrays:")
    bDebug and print("Num Factor Array: {}".format(iArrNumReducedFactors))
    bDebug and print("Den Factor Array: {}".format(iArrDenReducedFactors))
    
    # Initialized Variables for Product of All Arrays:
    iNumReduced = 1
    iDenReduced = 1

    # Iterate Arrays for Product of Num / Den
    for iNumRedInd in range(len(iArrNumReducedFactors)):
        
        iNumReduced *= iArrNumReducedFactors[iNumRedInd] 
    
    for iDenRedInd in range(len(iArrDenReducedFactors)):
        
        iDenReduced *= iArrDenReducedFactors[iDenRedInd] 
    
    print("\n\nFinal Result for Fraction {:,} / {:,}:".format(iOrigNum, iOrigDen))
    print("\nReduces to {:,}".format(iNumReduced)) if iDenReduced == 1 else print("Fraction reduces to {:,} / {:,}".format(iNumReduced, iDenReduced))

def sReduceFractionFast(iNum, iDen):

    print("Fraction: {:,} / {:,}".format(iNum, iDen))

    # Start the factor at the middle of the lowest number to save time
    iFactor = iNum // 2 if (iNum <= iDen) else iDen // 2
    
    #Starts the function at an odd number so that the only even number analyzed is 2
    if iFactor % 2 == 0: iFactor += 1
    iFactorArray = []


    # Go down the list of odd numbers
    while iFactor > 1:

        # Checks to see if both numerator and denominator can be divided by the same number into an integer 
        if iNum % iFactor == 0 and iDen % iFactor == 0:

            # Necessary because sometimes you may be able to factor out a number multiple times.
            while iNum % iFactor == 0 and iDen % iFactor == 0:

                iNum /= iFactor
                iDen /= iFactor
                iFactorArray.append(iFactor)

        # Testing Req'd to Verify this procedure works
        # Makes the last number 2 if it is at 3
        iFactor -= 2 if iFactor != 3 else iFactor -= 1
    
    print("Reduced Fraction: {:,} / {:,}".format(int(iNum), int(iDen)))
    print("Factor Array: {}".format(iFactorArray))


def iQuotientPower(iNumPoly, iNumPower, iDenPoly, iDenPower):

    if iNumPoly != iDenPoly:

        return "Not Computable"
    
    return iNumPower - iDenPower


def iProductPower(iNumPoly, iNumPower, iDenPoly, iDenPower):

    if iNumPoly != iDenPoly:

        return "Not Computable"
    
    return iNumPower + iDenPower


def iNumericPolyTerm(iCoeff, iVar, iPower):

    return iCoeff * (iVar ** iPower)


def iExponentiatePolyTerm(iCoeff, iPoly, iPower, iExponent)

    return iNumericPolyTerm(iCoeff ** iExponent, iPoly, iPower * iExponent)


def iNumericPolynomial(iArrCoeff, iVar, bDebug = False):

    iLeadingPower = len(iArrCoeff) - 1
    
    if bDebug:

        sPolyStatement = "Numeric Polynomial = "
        iPower = iLeadingPower

        for iCoefficients in iArrCoeff:

            sPolyStatement += str(iArrCoeff[iCoefficients]) + "x^" + str(iPower)
            iPower >= 1 and sPolyStatement += " + " 
            
            iPower -= 1

        print(sPolyStatement)

    iPower = iLeadingPower
    iNumericSolution = 0

    for iCoefficients in iArrCoeff:

        iNumericSolution += iNumericPolyTerm(iArrCoeff[iCoefficients], iVar, iPower)
        iPower -= 1

    return iNumericSolution


def sDefineEndToEndBehavior(iArrCoeff):
    
    iIndex = 0

    # Validation to ensure no 0 coefficients appear in the lead terms.
    while iArrCoeff[iIndex] == 0:

        iIndex += 1
    
    iHighestPower = len(iArrCoeff) - iIndex - 1
    iLeadCoeff = iArrCoeff[iIndex]
    
    if iHighestPower % 2 == 0:

        return "Quadrant II to Quadrant I" if iLeadCoeff > 0, else "Quadrant III to Quadrant IV"

    return "Quadrant III to Quadrant I" if iLeadCoeff > 0, else "Quadrant II to Quadrant IV"