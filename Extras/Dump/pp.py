n = 5
for i in range(1, n):
    k = i*2-1
    s = (n-i-1)
    for x in range(s):
        print ' ',
    for j in range(k):
        print '*',
    print


###
a = [10,2,6,5,4,7,1,3]

print a
l, h = 0, len(a)
i = l-1

for j in range(l, h):
    p = a[h-1]
    if a[j] <= p:
        i += 1
        a[j], a[i] = a[i], a[j]
a[i+1], a[h-1] = a[h-1], a[i+1]
print a

###
n = 10
a = 0
b = 1
arr = [str(a)]
for i in range(n):
    arr.append(str(b))
    a, b = b, a+b

print ' '.join(arr)
