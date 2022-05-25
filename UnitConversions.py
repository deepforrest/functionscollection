# Temperature - Basics

iDeg_K_to_R = 5 / 9
iDiff_C_to_K = 273.15
iDiff_F_to_R = 459.67
iDiff_C_to_F = 32

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

def iLength_in_to_cm(iLen_in):

    return 2.54 * iLen_in

def iLength_m_to_cm(iLen_m):

    return 100 * iLen_m

def iLength_cm_to_mm(iLen_cm):

    return 10 * iLen_cm

def iLength_ft_to_in(iLen_ft):

    return 12 * iLen_ft

def iLength_yd_to_ft(iLen_yd):

    return 3 * iLen_yd

def iLength_mi_to_ft(iLen_mi):

    return 5_280 * iLen_mi


# Compound Length Conversions

def iLength_ft_to_cm(iLen_ft):

    return iLength_in_to_cm(iLength_ft_to_in(iLen_ft))

def iLength_ft_to_mm(iLen_ft):

    return iLength_cm_to_mm(iLength_ft_to_cm(iLen_ft))