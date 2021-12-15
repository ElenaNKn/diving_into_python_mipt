import sys

# we take each element from the string, convert it to integer and sum with 
# the result variable

result=0
for i in sys.argv[1]:
    result+=int(i)

print(result)