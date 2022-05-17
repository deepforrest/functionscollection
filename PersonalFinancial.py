# Constants (Move To Constants.py later)
iHoursPerWorkweek = 40
iSecondsPerMinute = 60
iMinutesPerHour = 60
iHoursPerDay = 24
iHoursWorkPerDay = 8
iWeeksPerYear = 52
iMonthsPerYear = 12
iOvertimeCoef = 1.5

iAvgWeeksPerMonth = iWeeksPerYear / iMonthsPerYear

# Summatives

def iWeeklyPayForHourly(iHourlyWage, iHoursPerWeek = iHoursPerWorkweek:

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

# Breakdowns

def iAnnualPayForHourly(iHourlyWage, iHoursPerWeek = iHoursPerWorkweek)

    return iMonthlyPayForHourly(iHourlyWage, iHoursPerWeek)


def iSalaryPerMonth(iSalary):

    return iSalary / iMonthsPerYear


def iSalaryBiweekly(iSalary):

    return iSalaryPerMonth(iSalary) / 2


def iSalaryPerWeek(iSalary):

    return iSalary / iWeeksPerYear


def iSalaryPerHour(iSalary, iHoursPerWeek = iHoursPerWorkweek):

    return iSalaryPayPerWeek(iSalary) / iHoursPerWeek








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
    