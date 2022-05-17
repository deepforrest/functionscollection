# Physics Constants

iGravityConstant = 6.67 * (10 ** -11) # [m][m][s] / [kg][kg][kg]

iRadiusOfEarth = 6.3781 * (10 ** 6)     # [m]
iMassOfEarth = 5.9722 * (10 ** 24)      # [kg]
iMassOfMoon = 7.34767309 * (10 ** 22)  # [kg]
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
