import math

# Mathematical Constants / Conversions
degreesToRadians = 180 / math.pi       # 180 degrees = pi radians

# Physics Constants
gravitationConstant = scientificNotation(6.67, -11)   # [m][m][s] / [kg][kg][kg]
radiusEarth = scientificNotation(6.3781, 6)     # [m]

# Known Astronomical Constants & Data
massMercury = scientificNotation(3.3011, 23)
massVenus = scientificNotation(4.5675, 24)
massEarth = scientificNotation(5.9722, 24)      # [kg]
massMoon = scientificNotation(7.34767309, 22)   # [kg]
massMars = scientificNotation(6.4171, 23)
massJupiter = scientificNotation(1.8982, 27)
massSaturn = scientificNotation(5.6834, 26)
massUranus = scientificNotation(8.6810, 25)
massNeptune = scientificNotation(1.02413, 26)
massPluto = scientificNotation(1.303, 22)        # Pluto is still a planet!!

# Calculated Constants
accelEarthGravity = (gravitationConstant * massEarth) / polynomialTerm(1, earthRadius, 2)


# Time Relationship Definitions
class ConversionFactor:

    def __init__(self, value, units, system):

        self.value = iValue
        self.units = Units
        self.system = sSystemType

def Units(sNum, sDen = 1):

    if sDen == 1:

        return sNum
    
    return str(sNum) + " / " + str(sDen)

# Time Based Units
secondsPerMinute = ConversionFactor(60, Units("[s]", "[min]")) 
minutesPerHour = ConversionFactor(60, Units("[min]", "[hr]"))
hoursPerDay = ConversionFactor(24, Units("[hr]", "[day]"))
daysPerWeek = ConversionFactor(7, Units("[day]", "[wk]"))
daysPerYear = ConversionFactor(365, sUnit("[day]", "[yr]"))
weeksPerYear = ConversionFactor(52, sUnit("[wk]", "[yr]"))
wonthsPerYear = ConversionFactor(12, sUnit("[mo]", "[yr]"))

# Calculated Time Constants
weeksPerMonthAvg = weeksPerYear / monthsPerYear

# Economic Constants
workHoursPerDay = 8
workDaysPerWeek = 5
hoursPerWorkweek = 40
hourlyOvertimeCoeff = 1.5

# Calculated Economic Constants
workDaysPerYear = workDaysPerWeek * workHoursPerDay * weeksPerYear

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