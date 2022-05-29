import math

# Mathematical Constants / Conversions
iConvDegToRad = 180 / math.pi

# Physics Constants
iGravityConstant = 6.67 * (10 ** -11)   # [m][m][s] / [kg][kg][kg]
iRadiusOfEarth = 6.3781 * (10 ** 6)     # [m]

# Known Astronomical Constants & Data
iMassOfMercury = 
iMassOfVenus =
iMassOfEarth = 5.9722 * (10 ** 24)      # [kg]
iMassOfMoon = 7.34767309 * (10 ** 22)   # [kg]
iMassOfMars = 
iMassOfSaturn =

# Calculated Constants
iAccelGravEarth = (iGravityConstant * iMassOfEarth) / (iRadiusOfEarth ** 2)


# Time Relationship Definitions
iSecondsPerMinute = 60
iMinutesPerHour = 60
iHoursPerDay = 24
iDaysPerWeek = 7
iDaysPerYear = 365
iWeeksPerYear = 52
iMonthsPerYear = 12

# Calculated Time Constants
iAvgWeeksPerMonth = iWeeksPerYear / iMonthsPerYear

# Economic Constants
iHoursWorkPerDay = 8
iWorkDaysPerWeek = 5
iHoursPerWorkweek = 40
iOvertimeCoef = 1.5

# Calculated Economic Constants
iWorkDaysPerYear = iWorkDaysPerWeek * iHoursWorkPerDay * iWeeksPerYear

# Rewrite Constants as a Function of their Units:

def iGetIdealGasConst(sEnergyUnit, sSubstanceUnit, sTempUnit):

    sUnitArray = [sEnergyUnit, sSubstanceUnit, sTempUnit]

    if sUnitArray = ["[J]", "[mol]", "[K]"]: return 8.31446261815324
    if sUnitArray = ["[Btu]", "[mol]", "[ºR]"]: return 1.985875279009
    
class IdealGasConstant:

    def __init__(self, units):

        self.units = sArrUnits
        # self.value = f(units)


# Proposed Classes
class AtomicElement:

class Planet:
    
    def __init__(self, name, radius, mass):

        self.name = sName
        self.radius = iRadius
        self.mass = iMass

        iVolume = iSphericalVolume(iRadius)
        iSurfaceArea = iSphereSurfArea(iRadius)


class Moon(Planet):
    
    # Add super function
    def __init__(self, planetOrbit):

        self.planetOrbit = sPlanetName
    

class Star:
    
    def __init__(self, *args):
    # Has some physical properties of planets, including:
        # Mass
        # Volume = f(r)
        # Surface Area
        # Radius


class Molecule:

    def __init__(self, *args):
    
    # Somehow, the molecule has to be made as a function of the
    # elements attached to it.  It has to draw from the atomic
    # element classes that are associated with it and accept multiple
    # arguments for its arrangement.  This will probably require different
    # functions to analyze molecules and match with a database.

class Particle:

    def __init__(self, ...):