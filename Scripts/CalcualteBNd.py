import math as m

u = 1.661e-27

Numerator = (10.811*u + 14.0067*u)

Denominator1 = ((3*m.sqrt(3))/2) * (1.45e-10)**2

Sd = Numerator / Denominator1

d = Sd / (0.333e-9)

dAns = d / 1000

print(dAns)
