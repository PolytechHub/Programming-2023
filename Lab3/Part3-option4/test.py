from math import sqrt

R = float(input('R: ').replace(',', '.'))
X = float(input('X: ').replace(',', '.'))
Y = float(input('Y: ').replace(',', '.'))

result = True

if Y == 0:
    if abs(X) > R:
        result = False
elif Y > 0:
    if abs(X) > R:
        result = False
    elif Y > sqrt(R**2 - X**2):
        result = False
elif Y < 0:
    if X > 0:
        result = False
    elif Y < -R:
        result = False
    elif X < Y:
        result = False

if result:
    print("Inside the chart")
else:
    print("Otside the chart")