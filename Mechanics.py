def iPositionFinal(iPosInit, iVel, iAccel, iTime):

    return iPosInit + iVel * iTime + 1 / 2 * iAccel * (iTime ** 2)


def iPositionInit(iPosFinal, iVel, iTime):

    return iPosFinal - (iVel * iTime + 1 / 2 * iAccel * (iTime ** 2))


def iVelocityAvg(iPosFinal, iPosInit, iTimeFinal, iTimeInit):

    return (iPosFinal - iPosInit) / (iTimeFinal - iTimeInit)


def iVelocityFinal(iVelInit, iAccel, iDeltaTime):

    return iVelInit + iAccel * iDeltaTime


def iAccelerationAvg(iVelFinal, iVelInit, iTimeFinal, iTimeInit):

    return (iVelFinal - iVelInit) / (iTimeFinal - iTimeInit)


def iAccelerationCentripetal(iVel, iRadius)

    return (iVel ** 2) / iRadius

def iCircularMotionPeriod(iRadius, iVelocity)

    return (2 * math.pi() * iRadius) / iVelocity


def iForce(iMass, iAcceleration):

    return iMass * iAcceleration


# Newton's Third Law
def iReactiveForce(iForce):

    return -iForce

def iForceNewtonLawofGravity(iMass_1, iMass_2, iDistance)

    return iGravityConstant * (iMass_1 * iMass_2) / (iDistance ** 2)

def iVelocityTerminal(iMass, iAreaSurface):

    return sqrt((4 * iMass * iAccelGravEarth) / iAreaSurface)


def iVelocityOrbit(iRadius, iAccel = iAccelGravEarth):

    return sqrt(iRadius * iAccel)


# Conservation Laws
def iMomentum(iMass, iVelocity):

    return iMass * iVelocity

def iImpulse(iForce, iDeltaTime):

    return iForce * iDeltaTime

def iEnergyPotentialGrav(iMass, iDistance, iAccel = iAccelGravEarth):

    return iMass * iAccel * iDistance

def iEnergyKineticDef (iMass, iVel):

    return 1 / 2 * iMass * (iVel ** 2)

def iEnergyKineticAlt(iMomentum, iMass):

    return (iMomentum ** 2) / (2 * iMass)

def iForceHookesLaw(iSpringConst, iDeltaPosition):

    return - iSpringConst * iDeltaPosition

def iEnergyPotentialElastic(iSpringConst, iDeltaPosition):

    return 1/2 * iSpringConst * (iDeltaPosition ** 2)

def iWork(iForce, iDeltaPosition, iAngle = 90):

    return iForce * iDeltaPosition

