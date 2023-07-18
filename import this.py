import math
a = int(input('Type a:'))
b = int(input('Type b:'))
c = int(input('Type c:'))

result1 = ((-b + (b**2 - 4*a*c)**0.5)/2*a)
result2 = ((-b - (b**2 - 4*a*c)**0.5)/2*a)

print('х1 = ' + str(int(result1)))
print('х2 = ' + str(int(result2)))