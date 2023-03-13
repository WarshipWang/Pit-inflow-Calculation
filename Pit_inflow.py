# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 14:20:29 2022
Equation to get pit inflows
Ref: Marinelli, F. & Niccoli, W (2000): Simple Analytical Equations for Estimating Groundwater Inflow to a Mine Pit. Groundwater Journal, Volume 38, No.2, March-April 2000 (p311-314)
@author: Junjian Wang
"""

from scipy.optimize import fsolve
import math

rp   = 33.5             # Effective pit radius, m
h0   = 9.1              # Initial (premining) saturated thickness above the base of Zone 1, m
hp   = 6.4              # Saturated thickness above the base of Zone 1 at rp, m 
W    = 2.4e-9           # The distributed recharge flux, m/s 
Kh1  = 5.3e-7           # Horizontal hydraulic conductivity of materials within Zone 1, m/s
Kh2  = 5.3e-7           # Horizontal hydraulic conductivity of materials within Zone 2, m/s
m2   = 1                # Anisotropy parameter of hydraulic conducvitity of Zone 2
Kv2  = Kh2/(m2 ** 2)    # Vertical hydraulic conductivity of materials within Zone 2, m/s 
roguess = 200           # a guess number of ro to use fsolve.
d    = 6.4              # Depth of the pit lake, m


def F(ro, rp, h0, hp, W, Kh1):
    return h0 ** 2 - hp ** 2 - W/Kh1*(ro ** 2 * math.log(ro/rp)-(ro ** 2 - rp ** 2)/2)

ro = float(fsolve(F, roguess, args=(rp, h0, hp, W, Kh1)))   # Calculated radius of influence (maxiumum extent of the cone of depression), m

print(ro)

Q1 = W * math.pi * (ro ** 2 - rp ** 2)                      # Calculated inflow from Zone 1, m3/s
Q2 = 4*rp*(Kh2/m2)*(h0-d)                                   # Calculated inflow from Zone 2, m3/s
 
