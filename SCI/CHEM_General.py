def bCheckIfIdealGas(iPres, iVol, iTemp, iSub = 1):

    iIdealGasConst = iGetIdealGasConst("[J]", "[mol]", "[K]")

    return iPres * iVol = iSub * iIdealGasConst * iTemp


def iIdealGasLawPressure(iVol, iTemp, iSub = 1):

    iIdealGasConst = iGetIdealGasConst("[J]", "[mol]", "[K]")

    return iSub * iIdealGasConst * iTemp / iVol


def iIdealGasLawVolume(iPres, iTemp, iSub = 1):

    iIdealGasConst = iGetIdealGasConst("[J]", "[mol]", "[K]")

    return iSub * iIdealGasConst * iTemp / iPres


def iIdealGasLawTemp(iPres, iVol, iSub = 1):

    iIdealGasConst = iGetIdealGasConst("[J]", "[mol]", "[K]")

    return (iPres * iVol) / (iSub * iIdealGasConst)


def iDensityFromMassVol(iMass, iVol):

    return iMass / iVol