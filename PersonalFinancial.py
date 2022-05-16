# 01 - Income To Expense Ratio
def iIncomeToExpenseRatio (iArrRevenueData, iArrExpensesData):

    iTotalRevenue = 0
    iTotalExpenses = 0

    for iDataPoint in range(len(iArrRevenueData)):

        iTotalRevenue += iArrRevenueData[iDataPoint]

    for iDataPoint in range(len(iArrExpensesData)):

        iTotalExpenses += iArrExpensesData[iDataPoint]

    print("Total Revenue: " + str(iTotalRevenue))
    print("Total Expenses: " + str(iTotalExpenses))

    return round(iTotalRevenue / iTotalExpenses, 2)


# 02 - Profit
def iProfit(iArrRevenueData, iArrExpensesData):

    iTotalRevenue = 0
    iTotalExpenses = 0

    for iDataPoint in range(len(iArrRevenueData)):

        iTotalRevenue += iArrRevenueData[iDataPoint]

    for iDataPoint in range(len(iArrExpensesData)):

        iTotalExpenses += iArrExpensesData[iDataPoint]

    print("Total Revenue: " + str(iTotalRevenue))
    print("Total Expenses: " + str(iTotalExpenses))

    return iTotalRevenue - iTotalExpenses


#03

def iBehToRecurExpensesRatio(iArrBehExpData, iArrRecurExpData):

    # Initializations
    iTotalExpenses = 0
    iTotalBehavioralExpenses = 0
    iTotalRecurringExpenses = 0

    for iDataPoint in range(len(iArrBehExpData)):

        iTotalExpenses += iArrBehExpData[iDataPoint]
        iTotalBehavioralExpenses += iArrBehExpData[iDataPoint]

    for iDataPoint in range(len(iArrRecurExpData)):

        iTotalExpenses += iArrRecurExpData[iDataPoint]
        iTotalRecurringExpenses += iArrRecurExpData[iDataPoint]

    print("Total Behavioral Expenses: " + iTotalBehavioralExpenses)
    print("Total Recurring Expenses: " + iTotalRecurringExpenses)
    print("Total Expenses: " + iTotalExpenses)

    return round(iTotalBehavioralExpenses / iTotalRecurringExpenses, 2)