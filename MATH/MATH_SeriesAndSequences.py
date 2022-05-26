def sLinearSequence_FindNextNTerms(iInitialTerm, iDifference, iNum):

    if n < 1: return "Not a valid number of terms!"

    sSeriesStatement = str(iInitialTerm)
    iTerm = 2

    while iTerm <= iNum:

        sSeriesStatement += ", " + str(iInitialTerm + (iTerm - 1)*iDifference)
        iTerm += 1

    return sSeriesStatement

def iGeometricSeries_ExpandToNTerms(iInitialTerm, iRatio, iNum):

    if iNum < 1: return "Not a valid number of terms!"

    sSeriesStatement = str(iInitialTerm)
    iTerm = 2

    while iTerm <= iNum:

        sSeriesStatement += ", " + str(iInitialTerm * iRatio ** (iTerm - 1))
        iTerm += 1

    return sSeriesStatement

print(iGeometricSeries_FindNextNTerms(2, 1.5, 20))