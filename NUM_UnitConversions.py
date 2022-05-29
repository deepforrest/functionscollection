# Temperature - Basics

iDeg_K_to_R = 5 / 9
iDiff_C_to_K = 273.15
iDiff_F_to_R = 459.67
iDiff_C_to_F = 32

iLen_yd_per_mi = 1760
iLen_ft_per_yd = 3
iLen_in_per_ft = 12

iLen_cm_per_in = 2.54

# VOLUME - IMPERIAL
iVol_gal_to_qt = 4
iVol_qt_to_pt = 2
iVol_pt_to_cup = 2
iVol_cup_to_gill = 2
iVol_gill_to_floz = 5

# SI Prefix Conversions
iSIPrefBaseConv = {

    "Y": iScientificNotation(1, -24),
    "Z": iScientificNotation(1, -21),
    "E": iScientificNotation(1, -18),
    "P": iScientificNotation(1, -15),
    "T": iScientificNotation(1, -12),
    "G": iScientificNotation(1, -9),
    "M": iScientificNotation(1, -6),
    "k": iScientificNotation(1, -3),
    "h": iScientificNotation(1, -2),
    "da": iScientificNotation(1, -1),
    "d": iScientificNotation(1, 1),
    "c": iScientificNotation(1, 2),
    "m": iScientificNotation(1, 3),
    "µ": iScientificNotation(1, 6),
    "n": iScientificNotation(1, 9),
    "p": iScientificNotation(1, 12),
    "f": iScientificNotation(1, 15),
    "a": iScientificNotation(1, 18),
    "z": iScientificNotation(1, 21),
    "y": iScientificNotation(1, 24)

}

# https://www.ece.utoronto.ca/canadian-metric-association/si-derived-units/
sDerivedUnits_SI {

    "[C]": "[A][s]",
    "[F]": "[A][A][s][s][s][s]/[kg][m][m]",
    "[H]": "[m][m][kg]/[A][A][s][s]",
    "[Hz]": "[1]/[s]"
    "[J]": "[kg][m][m]/[s][s]",
    "[lm]": "[cd][sr]",
    "[N]": "[kg][m]/[s][s]",
    "[Ω]": "[m][m][kg]/[A][A][s][s][s]",
    "[Pa]": "[kg]/[m][s][s]",
    "[S]": "[A][A][s][s][s]/[m][m][kg]",
    "[Sv]": "[m][m]/[s][s]",
    "[T]": "[kg]/[A][s][s]",
    "[V]": "[kg][m][m]/[A][s][s][s]"
    "[W]": "[kg][m][m]/[s][s][s]",
    "[Wb]": "[m][m][kg]/[A][s][s]",

    "[lx]": "[]",
    "[bq]": "[]",
    "[Gy]": "[]",
    "[rad]": "[]",
    "[sr]": "[]",

}

sConsolidatedUnits_SI {

    "acceleration": "[m]/[s][s]",
    "force": "[kg][m]/[s][s]"
    "jerk": "[m]/[s][s][s]",
    "velocity": "[m]/[s]",


}


# Fundamental Units
sFundamentalUnits_SI {

    "mass": "[kg]",
    "length": "[m]",
    "time": "[s]",
    "substance": "[mol]",
    "electric current": "[A]",
    "temperature": "[K]",
    "luminous intensity": "[cd]"

}

def sStandardizeUnit(sUnit):

    if sUnit[0] != "[" or sUnit[len(sUnit) - 1] != "]":

        return "Improperly formatted unit!"

    sLastLetter = sUnit[len(sUnit) - 2]

    # Iterates through the 7 Fundamental Units
    return sFundamentalUnits_SI["mass"] if sLastLetter = "g" else
        sFundamentalUnits_SI["length"] if sLastLetter = "m" else
        sFundamentalUnits_SI["temperature"] if sLastLetter = "K" else
        sFundamentalUnits_SI["time"] if sLastLetter = "s" else
        sFundamentalUnits_SI["substance"] if sLastLetter = "l" else
        sFundamentalUnits_SI["electric current"] if sLastLetter = "A" else sFundamentalUnits_SI("luminous intensity")


# Temperature Unit Conversions
def iDegrees_C_to_K(iTemp_C):

    return iTemp_C + iDiff_C_to_K


def iDegrees_K_to_C(iTemp_K):

    return iTemp_K - iDiff_C_to_K


def iDegrees_F_to_R(iTemp_F):

    return iTemp_F + iDiff_F_to_R


def iDegrees_R_to_F(iTemp_R):

    return iTemp_R - iDiff_F_to_R

# Temperature - More Sophisticated

def iDegrees_C_to_F(iTemp_C):

    return iDeg_K_to_R * (iTemp_C - iDiff_C_to_F)


def iDegrees_F_to_C(iTemp_F):

    return iTemp_F / iDeg_K_to_R + iDiff_C_to_F


def iDegrees_K_to_R(iTemp_K):

    return iDeg_K_to_R * iTemp_K


def iDegrees_R_to_K(iTemp_R):

    return iTemp_R / iDeg_K_to_R


def iDegrees_R_to_C(iTemp_R):

    return iDegrees_C_to_K(iDegrees_R_to_K(iTemp_R))


def iDegrees_K_to_F(iTemp_K):

    return iDegrees_F_to_R(iDegrees_K_to_R(iTemp_K))

#------------------Length--Conversions---------------

def iLength_m_to_cm(iLen_m):

    return (10 ** 2) * iLen_m


def iLength_m_to_mm(iLen_cm):

    return (10 ** 3) * iLen_cm


# Step Conversions - Imperial

def iLength_ft_to_in(iLen_ft):

    return iLen_in_per_ft * iLen_ft


def iLength_yd_to_ft(iLen_yd):

    return iLen_ft_per_yd * iLen_yd


def iLength_mi_to_yd(iLen_mi):

    return iLen_yd_per_mi * iLen_mi

# Fundamental Imperial to Metric Conversion
def iLength_in_to_cm(iLen_in):

    return iLen_cm_per_in * iLen_in

def iLength_cm_to_in(iLen_cm):

    return iReciprical(iLength_in_to_cm(iLen_cm))  # Double check?


#-----------------------Cascading-Length-Conversions-----------------------

# IMPERIAL - FORWARD
def iLength_mi_to_ft(iLen_mi):

    return iLength_yd_to_ft(iLength_mi_to_yd(iLen_mi))


def iLength_mi_to_in(iLen_mi):

    return iLength_ft_to_in(iLength_mi_to_ft(iLen_mi))


def iLength_yd_to_in(iLen_yd):

    return iLength_ft_to_in(iLength_yd_to_ft(iLen_yd))

# IMPERIAL - BACKWARD
def iLength_in_to_yd(ilLen_in):

    return iReciprical(iLength_yd_to_in(iLen_in))  # Modify - conversion route incorrect!


def iLength_in_to_mi(iLen_in):

    return iReciprical(iLength_mi_to_in(iLen_in))  # Modify - conversion route incorrect!


def iLength_ft_to_mi(iLen_mi):

    return iReciprical(iLength_mi_to_ft(iLen_mi))  # Modify - conversion route incorrect!

# METRIC

# Imperial to Metric Conversions
def iLength_ft_to_cm(iLen_ft):

    return iLength_in_to_cm(iLength_ft_to_in(iLen_ft))


def iLength_ft_to_mm(iLen_ft):

    return iLength_cm_to_mm(iLength_ft_to_cm(iLen_ft))