#water bottle
def canMeasureWater(x, y, z):
    import math
    if x+y < z: return False
    return z % math.gcd(x,y)==0
print(canMeasureWater(3,6,2))
