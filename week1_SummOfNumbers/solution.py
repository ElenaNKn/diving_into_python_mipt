import sys

# script converts a string to a list and calculates a sum of list's elements
a=[int(i) for i in list(sys.argv[1])]

print(sum(a))