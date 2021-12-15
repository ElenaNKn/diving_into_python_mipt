import sys

n = int(sys.argv[1])

# use that, for example, 3*'#' is '###' and 'a'+'b' is 'ab'

for i in range(1,n+1):
    print(' '*(n-i)+'#'*i)