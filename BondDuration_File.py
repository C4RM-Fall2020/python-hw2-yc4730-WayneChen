import numpy as np
from BondPrice_File import getBondPrice
def getBondDuration(y, face, couponRate, m, ppy = 1):
    adj_y = y/ppy
    adj_couponRate = couponRate/ppy
    adj_m = m * ppy

    couponpayment = adj_couponRate * face
    t = np.arange(1, adj_m+1)
    wt = np.sum(couponpayment*(1+adj_y)**(-t)*t)+(adj_m*face*(1+adj_y)**(-adj_m))
    
    price = getBondPrice(y, face, couponRate, m, ppy = 1)
    Duration = wt/price
    return(Duration)
