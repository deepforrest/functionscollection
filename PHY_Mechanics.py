import math

iRightAngle = math.pi() / 2

'''


def iAccelerationCentripetal(iVel, iRadius)

    return (iVel ** 2) / iRadius


def iCircularMotionPeriod(iRadius, iVelocity)

    return (2 * math.pi() * iRadius) / iVelocity



def iVelocityTerminal(iMass, iAreaSurface):

    return math.sqrt((4 * iMass * iAccelGravEarth) / iAreaSurface)


def iVelocityOrbit(iRadius, iAccel = iAccelGravEarth):

    return math.sqrt(iRadius * iAccel)


# Conservation Laws
def iMomentum(iMass, iVelocity):

    return iMass * iVelocity


def iImpulse(iForce, iDeltaTime):

    return iForce * iDeltaTime


def iEnergyPotentialGrav(iMass, iDistance, iAccel = iAccelGravEarth):

    return iMass * iAccel * iDistance


def iEnergyKineticDef (iMass, iVel):

    return (iMass * (iVel ** 2)) / 2


def iEnergyKineticAlt(iMomentum, iMass):

    return (iMomentum ** 2) / (2 * iMass)



def iForceHookesLaw(iSpringConst, iDeltaPosition, iNormAngle = iRightAngle):

    return - iSpringConst * iDeltaPosition * sin(iNormAngle)


def iEnergyHookesLaw(iSpringConst, iDeltaPosition, iNormAngle = iRightAngle):

    return 1/2 * iSpringConst * (iDeltaPosition ** 2) * math.sin(iNormAngle)


'''

# Math

def iDiff(iFinal, iInit):

    return iFinal - iInit

# Kinematics, 1D

def iVelocityFinalAlt(iVelInit, iAccel, iPosFinal, iPosInit):

    return math.sqrt((iVelInit ** 2) + 2 * iAccel * iDiff(iPosFinal, iPosInit))


def iPositionFinal(iPosInit, iVel, iAccel, iTime):

    return iPosInit + iVel * iTime + 1 / 2 * iAccel * (iTime ** 2)


def iPositionInit(iPosFinal, iVel, iTime):

    return iPosFinal - (iVel * iTime + iAccel * (iTime ** 2) / 2)


def iVelocityAvg(iPosFinal, iPosInit, iTimeFinal, iTimeInit = 0):

    return iDiff(iPosFinal, iPosInit) / iDiff(iTimeFinal, iTimeInit)


def iVelocityFinal(iVelInit, iAccel, iTimeFinal, iTimeInit = 0):

    return iVelInit + iAccel * iDiff(iTimeFinal, iTimeInit)


def iAccelerationAvg(iVelFinal, iVelInit, iTimeFinal, iTimeInit = 0):

    return iDiff(iVelFinal, iVelInit) / iDiff(iTimeFinal, iTimeInit)


# Vector Components

def iAdjComponent(iHyp, iAngle):

    return iHyp * math.cos(iAngle)


def iOppComponent(iHyp, iAngle):

    return iHyp * math.sin(iAngle)


def iComponentResultant(iArrComponents)

    return sum(iArrComponents)


def iAngleBetweenResultants(iArrResY, iArrResX):

    return math.arctan(iArrResY / iArrResX)


def iHeightFromRise(iVelInit, iAccel = iAccelGravEarth):

    return (iVelInit ** 2) / (2 * iAccel)


def iDistanceResultant(iVelInit, iAngle, iAccel = iAccelGravEarth):

    return ((iVelInit ** 2) * math.sin(2 * iAngle)) / iAccel


# Dynamics - Forces, Newtons Laws of Motion

def iForce(iMass, iAcceleration):

    return iMass * iAcceleration


def iForceReactive(iForce):

    return -iForce


def iForceAttract(iMass_1, iMass_2, iDistance):

    return iGravityConstant * (iMass_1 * iMass_2) / (iDistance ** 2)


def iWeight(iMass, iAccel = iAccelGravEarth):

    return iMass * iAccel


# Friction, Drag, Elasticity

def iStress(iForce, iArea):

    return iForce / iArea


 # Energy, Work

def iWork(iForce, iDeltaPosition, iAngle = iRightAngle):

    return iForce * iDeltaPosition * math.sin(iAngle)