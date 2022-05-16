iArrFebRevenue = [850, 990, 850, 990, 42, 42, 42, 42, 150, 150, 150, 100, 120, 120]
iArrFebCosts = [1300, 100, 150, 40, 40, 40, 40]

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

iFebIncomeToExpenseRatio = iIncomeToExpenseRatio(iArrFebRevenue, iArrFebCosts)

print(iFebIncomeToExpenseRatio)