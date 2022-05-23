# Even though is a math.function, this is an exercise
# for myself in the event I take this into a different
# language that doesn't have such libraries.

def iFactorial(iNum):

    iResult = 1

    while iNum != 0:

        iResult *= iNum
        iNum -= 1

    return iResult

# Combinations in probability and statestics
def iCombinations(iSelection, iSetTotal):

    return iFactorial(iSetTotal) / (iFactorial(iSelection) * iFactorial(iSetTotal - iSelection))


# Permutations are similar to combinations
def iPermutations(iSelection, iSetTotal):

    return iFactorial(iSetTotal) / iFactorial(iSetTotal - iSelection)

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

    iArrFactors = []
    iDivisor = 2

    while iDivisor <= iNum:

        #print ("Number = " + str(iNum))
        #print ("Divisor = " + str(iDivisor))

        while iNum % iDivisor == 0:

            iArrFactors.append(iDivisor)
            #print(str(iNum) + " is divisible by " + str(iDivisor))

            iNum /= iDivisor
            #print("New Number: " + str(iNum))

        if iDivisor != 2:

            iDivisor += 2

        else:

            iDivisor += 1

    if len(iArrFactors) == 1:

        return "1 and itself"

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