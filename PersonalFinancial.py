# Constants (Move To Constants.py later)


# Summatives

def iWeeklyPayForHourly(iHourlyWage, iHoursPerWeek = iHoursPerWorkweek):

    return iHourlyWage * iHoursPerWeek


def iWeeklyPayOT(iHourlyWage, iHoursPerWeek = iHoursPerWorkweek, bOvertimeTrigger = True):

    # Takes into consideration
    if (iHoursPerWeek > iHoursPerWorkweek and bOvertimeTrigger = True):

        iOvertimeHours = iDiff(iHoursPerWeek, iHoursPerWorkweek)

        return iHourlyWage * (iHoursPerWorkweek + iOvertimeCoef * iOvertimeHours)

    return iHourlyWage * iHoursPerWeek


def iBiweeklyPayForHourly(iHourlyWage, iHoursBiweekly = 2 iHoursPerWorkweek)

    return iWeeklyPayForHourly(iHourlyWage, iHoursBiweekly)


def iMonthlyPayForHourly(iHourlyWage, iHoursPerWeek = iHoursPerWorkweek):

    return iHourlyWage * iHoursPerWorkweek * iAvgWeeksPerMonth


def iAnnualPayForHourly(iHourlyWage, iHoursPerWeek = iHoursPerWorkweek)

    return iMonthlyPayForHourly(iHourlyWage, iHoursPerWeek)


# Breakdowns

def iSalaryPerMonth(iSalary):

    return iSalary / iMonthsPerYear


def iSalaryBiweekly(iSalary):

    return iSalaryPerMonth(iSalary) / 2


def iSalaryPerWeek(iSalary):

    return iSalary / iWeeksPerYear


def iSalaryPerHour(iSalary, iHoursPerWeek = iHoursPerWorkweek):

    return iSalaryPayPerWeek(iSalary) / iHoursPerWeek


def iSalaryPerMinute(iSalary, iHoursPerWeek = iHoursPerWorkweek):

    if iSalaryPerHour(iSalary, iHoursPerWorkweek) / iMinutesPerHour < 10 ** -2:
        
        print("Too small to calculate")
        return 0

    return  iSalaryPerHour(iSalary, iHoursPerWorkweek) / iMinutesPerHour

'''
Other Functions to Consider

    - 

'''



# 01 - Income To Expense Ratio
def iIncomeToExpenseRatio (iArrRevenueData, iArrExpensesData):

    iCalcRevAndCostTotals(iArrRevenueData, iArrExpensesData)

    return round(iTotalRevenue / iTotalExpenses, 2)


# 02 - Profit
def iProfit(iArrRevenueData, iArrExpensesData):

    iCalcRevAndCostTotals(iArrRevenueData, iArrExpensesData)

    return iTotalRevenue - iTotalExpenses


# 03 - 
def iBehToRecurExpensesRatio(iArrBehExpData, iArrRecurExpData):

    # Initializations
    iTotalBehavioralExpenses = sum(iArrBehExpData)
    iTotalRecurringExpenses = sum(iArrRecurExpData)
    iTotalExpenses = iTotalBehavioralExpenses + iTotalRecurringExpenses

    print("Total Behavioral Expenses: " + iTotalBehavioralExpenses)
    print("Total Recurring Expenses: " + iTotalRecurringExpenses)
    print("Total Expenses: " + iTotalExpenses)

    return round(iTotalBehavioralExpenses / iTotalRecurringExpenses, 2)


def iCalcRevAndCostTotals(iArrRevenueData, iArrCostsData):

    iTotalRevenue = sum(iArrRevenueData)
    iTotalExpenses = sum(iArrCostsData)

    print("Total Revenue: " + str(iTotalRevenue))
    print("Total Expenses: " + str(iTotalExpenses))

# Function that takes current wages and earnings and calculates how many hours a person working
# At minimum wage would need to work to achieve that income level.  
def iMinWageHours(iArrEarnings, iArrHours):

    iTotalEarnings = sum(iArrEarnings)
    iTotalHours = sum(iArrHours)

    if len(iArrEarnings) != len(iArrHours):
        print("Number of Total Earnings: " + str(len(iArrEarnings)))
        print("Number of Total Hour Entries: " + str(len(iArrHours)))
        print("Double check entries and try again")
        return -1

    print("Total Entries = " + str(len(iArrEarnings)))
    print("Totals: $" + str(round(iTotalEarnings, 2)) + " / " + str(iTotalHours) + " Hours")
    iArrEarningsPerHour = []

    iEntryIndex = 0

    while iEntryIndex < len(iArrEarnings):

        iArrEarningsPerHour.append(round(iArrEarnings[iEntryIndex] / iArrHours[iEntryIndex], 2))
        iEntryIndex += 1

    print("Earnings Per Hour Array: " + str(iArrEarningsPerHour))
    iMinWage = 14  #CA, 2022

    iAvgHourlyWage = round(iTotalEarnings / iTotalHours, 2)

    iWageRatio = round(iAvgHourlyWage / iMinWage, 2)

    iMinHoursReq = round(iWageRatio * iTotalHours, 1)

    print("Average Wage / Hour: $" + str(iAvgHourlyWage))
    print("Wage/Min Ratio: " + str(iWageRatio))
    print("Min Wage Hours = " + str(iMinHoursReq))

    if iMinHoursReq > 7 * 24:
        print("UNSUSTAINABLE!")

    return round(iWageRatio * iTotalHours, 1)

# Min Weekly Earnings per Day, Given Expenses
def iMinWeeklyEarningsPerDay(iArrMonthlyExpenses):

    iDaysPerWeek = 7
    iTotalWeeklyExpenses = sum(iArrMonthlyExpenses) * iDaysPerWeek / 30

    for iDay in range(1, iDaysPerWeek + 1):

        iEarningsPerDay = round(iTotalWeeklyExpenses / iDay, 2)

        print("In a " + str(iDay) + "-Day Workweek, you need to make $" + str(iEarningsPerDay) + "/Day")


def iProjectedFederalTaxes(iArrIncome):

    # Checks to see if an array was passed, otherwise a scalar
    if isinstance(iArrIncome, list):

        iTotalIncome = sum(iArrIncome)

    else:

        iTotalIncome = iArrIncome

    iTotalTaxes = 0

    while iTotalIncome > 0:

        # Create the tax table here:

    return iTotalTaxes