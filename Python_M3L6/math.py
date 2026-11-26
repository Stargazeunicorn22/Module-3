import math

d = float(input("Enter angle in degrees: "))
r = math.radians(d)

x = math.sin(r)
y = math.cos(r)
z = math.tan(r)

print(round(x, 4))
print(round(y, 4))
print(round(z, 4))
