import math

# Mathematical Constants / Conversions
iConvDegToRad = 180 / math.pi       # 180 degrees = pi radians

# Physics Constants
iGravityConstant = iScientificNotation(6.67, -11)   # [m][m][s] / [kg][kg][kg]
iRadius_Earth = iScientificNotation(6.3781, 6)     # [m]

# Known Astronomical Constants & Data
iMass_Mercury = iScientificNotation(3.3011, 23)
iMass_Venus = iScientificNotation(4.5675, 24)
iMass_Earth = iScientificNotation(5.9722, 24)      # [kg]
iMass_Moon = iScientificNotation(7.34767309, 22)   # [kg]
iMass_Mars = iScientificNotation(6.4171, 23)
iMass_Jupiter = iScientificNotation(1.8982, 27)
iMass_Saturn = iScientificNotation(5.6834, 26)
iMass_Uranus = iScientificNotation(8.6810, 25)
iMass_Neptune = iScientificNotation(1.02413, 26)
iMass_Pluto = iScientificNotation(1.303, 22)        # Pluto is still a planet!!

# Calculated Constants
iAccelGravEarth = (iGravityConstant * iMass_Earth) / (iRadiusOfEarth ** 2)


# Time Relationship Definitions
class ConversionFactor:

    def __init__(self, value, units, system):

        self.value = iValue
        self.units = sUnits
        self.system = sSystemType

def sUnits(sNum, sDen = 1):

    if sDen == 1:

        return sNum
    
    return str(sNum) + " / " + str(sDen)

# Time Based Units
cSecondsPerMinute = ConversionFactor(60, sUnits("[s]", "[min]")) 
cMinutesPerHour = ConversionFactor(60, sUnits("[min]", "[hr]"))
cHoursPerDay = ConversionFactor(24, sUnits("[hr]", "[day]"))
cDaysPerWeek = ConversionFactor(7, sUnits("[day]", "[wk]"))
cDaysPerYear = ConversionFactor(365, sUnit("[day]", "[yr]"))
cWeeksPerYear = ConversionFactor(52, sUnit("[wk]", "[yr]"))
cMonthsPerYear = ConversionFactor(12, sUnit("[mo]", "[yr]"))

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