def iPositionFinal(iPositionInit, iVelocity, iTime):

    return iPositionInit + iVelocity * iTime


def iPositionInit(iPositionFinal, iVelocity, iTime):

    return iPositionFinal - iVelocity * iTime


def iVelocityAvg(iPosFinal, iPosInit, iTimeFinal, iTimeInit):

    return (iPosFinal - iPosInit) / (iTimeFinal - iTimeInit)


def iVelocityFinal(iVelInit, iAccel, iTime):

    return iVelInit + iAccel * iTime


def iAccelerationAvg(iVelFinal, iVelInit, iTimeFinal, iTimeInit):

    return (iVelFinal - iVelInit) / (iTimeFinal - iTimeInit)


def iForce(iMass, iAcceleration):

    return iMass * iAcceleration


def iMomentum(iMass, iVelocity):

    return iMass * iVelocity

