def bValidateInputs(iArrInputs, sFunctionName)

    iArrInputs = [iFinal, iInit]

    # Checks to Make Sure All Inputs Are Numerical
    for iInput in range(len(iArrInputs)):

        iNumInQuestion = iArrInputs[iInput]

        if not isinstance(iNumInQuestion, (int, float)):

            print("Invalid entry for function {}: {}".format(sFunctionName, iNumInQuestion))
            return False

    return True