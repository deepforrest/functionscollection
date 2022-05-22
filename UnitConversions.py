# Temperature - Basics

iDegKtoR = 5 / 9
iDiffCtoK = 273.15
iDiffFtoR = 459.67
iDiffCtoF = 32

def iDegreesCtoK(iTemp):

    return iTemp + iDiffCtoK


def iDegreesKtoC(iTemp):

    return iTemp - iDiffCtoK


def iDegreesFtoR(iTemp):

    return iTemp + iDiffFtoR


def iDegreesRtoF(iTemp):

    return iTemp - iDiffFtoR

# Temperature - More Sophisticated

def iDegreesCtoF(iTemp):

    return iDegKtoR * (iTemp - iDiffCtoF)


def iDegreesFtoC(iTemp):

    return iTemp / iDegKtoR + iDiffCtoF


def iDegreesKtoR(iTemp):

    return iDegKtoR * iTemp


def iDegreesRtoK(iTemp):

    return iTemp / iDegKtoR


def iDegreesRtoC(iTemp):

    return iDegreesCtoK(iDegreesRtoK(iTemp))


def iDegreesKtoF(iTemp):

    return iDegreesFtoR(iDegreesKtoR(iTemp))