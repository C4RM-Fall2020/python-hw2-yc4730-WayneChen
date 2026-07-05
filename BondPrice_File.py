import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    adj_y = y/ppy
    adj_couponRate = couponRate/ppy
    adj_m = m * ppy

    couponpayment = adj_couponRate * face
    t = np.arange(1, adj_m+1)

    return np.sum(couponpayment*(1+adj_y)**(-t))+(face*(1+adj_y)**(-adj_m))
