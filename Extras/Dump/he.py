from decimal import Decimal
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    nn, p, z = 0, 0, 0
    for d in arr:
        if d > 0:
            p += 1
        elif d < 0:
            nn += 1
        else:
            z += 1
            
    x = '{:.6f}'.format(Decimal(p)/Decimal(n))
    y = '{:.6f}'.format(Decimal(nn)/Decimal(n))
    z = '{:.6f}'.format(Decimal(z)/Decimal(n))

    print '%s\n%s\n%s'%(x, y, z)

#print plusMinus([-4, 3, -9, 0, 4, 1])
#print plusMinus([1, 2, 3, -1, -2, -3, 0, 0])
#sys.exit()

def star(n):
    for i in range(1, n+1):
        space = n-i
        if space:
            print ''.join([' ' for k in range(space)]),
        print ''.join(['*' for j in range(i)])
       

#star(6) 

def min_max(arr):
    all_sum = reduce(lambda x, y:x+y, arr)
    ar = []
    for i in range(len(arr)):
        ar.append(all_sum - arr[i])
    ar.sort()
    print ar[0],ar[-1]

#min_max([1,2,3,4,5])

def candle(arr):
    if len(arr) == 1:
        print (1)
        sys.exit()
    arr.sort(reverse = True)
    nar = []
    nar.append(arr[0])
    for i, d in enumerate(arr, 1):
        if d == arr[i]:
            nar.append(d)
        else:
            break
    print (len(nar))

#candle([3,1,2,3, 1, 2, 3, 3, 2, 1, 1, 2])
        
def even_odd(N):
    if (N % 2) != 0:
        print 'Weird'
    elif (N % 2) == 0 and (2 <= N <= 5):
        print 'Not Weird'
    elif (N % 2) == 0 and (6 <= N <= 20):
        print 'Weird'
    elif (N % 2) == 0 and (N > 20):
        print 'Not Weird'

#N = input()
#even_odd(N)

import numpy as np

def arr_mul(a, b):
    #a = np.array(a)
    #b = np.array(b)
    #print (a * b)
    print(np.multiply(a, b))

#arr_mul([[1,2],[3, 4]], [[1,2],[3, 4]])


import numpy as np

def arr_product(x, y):
    print (np.dot(x, y))

def collect_arr(f):
    x = []
    for i in range(f):
        d = input()
        xr = [int(k.strip()) for k in d.split(' ')]
        x.append(xr)
    return x
    
#f = int(input())
#ar1 = collect_arr(f)
#print ar1
#ar2 = collect_arr(f)
#print ar2
#arr_product(ar1, ar2)

##LIST COMP
N = 2
m =  [(x, y, z) for x in range(3) for y in range(3) for z in range(3) if x+y+z != N]

##
def runner_up(arr):
    #arr = list(set(arr))
    x, y = arr[0], arr[1]
    if x < y:
        x, y = arr[1], arr[0]
    for d in arr[2:]:
        if d > x:
            y = x
            x = d
        elif d != x and d > y:
            y = d
        elif x == y and d < y:
            y = d
    print y

#runner_up([57, 57, -57, 57])
#runner_up([1,2,6,4,6,5])

##
def last_runner_up(arr):
    #arr = list(set(arr))
    x, y = arr[0], arr[1]
    if x > y:
        x, y = arr[1], arr[0]
    for d in arr[2:]:
        if d < x:
            y = x
            x = d
        elif d != x and d < y:
            y = d
        elif x == y and d > y:
            y = d
    print y

#last_runner_up([57, 57, -57, 57])
#last_runner_up([1,2,6,4,6,5, 3,4,1.21])

arr = [ 73, 67, 38, 33 ]
new_arr = []
for n in arr:
    m = 5 - (n%5)
    if (n>=38 and m<3):
        n += m
    new_arr.append(n)
print(new_arr)
