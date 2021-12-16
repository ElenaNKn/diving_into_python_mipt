import sys

# read coefficients of a quadratic equation

a , b , c = int(sys.argv[1]) , int(sys.argv[2]) , int(sys.argv[3])

# output roots of quadratic equation

print(int((-b-(b**2-4*a*c) ** 0.5)/(2*a)))
print(int((-b+(b**2-4*a*c) ** 0.5)/(2*a)))