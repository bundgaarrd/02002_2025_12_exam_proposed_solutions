# Opgave 1 (Gauge Diameter)
import math

def gauge_diameter(n):
    V = 40 # cm^3
    d = ((6*V)/(n*math.pi)) ** (1/3)
    return d