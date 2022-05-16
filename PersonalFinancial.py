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
    