data = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
data = [[1,2,3,4,5,6], [5,6,7,8,9,10], [9,10,11,12,13,14], [1,2,3,4,5,6], [5,6,7,8,9,10], [9,10,11,12,13,14]]

p = 3
arr = []
ind = 0
for m in range(len(data)):
    tmp = []
    for i in range(len(data)):
        for j in range(i, i+p):
            for k in range(ind, p+ind):
                #print '>>', ind, m, '===', (j, k)
                tmp.append((j,k))
    arr.append(tmp)
    ind += 1



if 0:
    p = 3
    final = []
    for i, x in enumerate(data):
        arr = []
        for m in range(i, len(data)):
            tmp = []
            for j in range(p):
                if m+p > len(data):break
                for k in range(m, m+p):
                    print '%s%s'%(m, k), ' ',
                    tmp.append(data[j][k])
            if tmp:
                arr.append(sum(tmp))
        final.append(arr)
        
for x in arr:
    print '>>>>>>', x
