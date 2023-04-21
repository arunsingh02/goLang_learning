a = [[1,2,3,4], [5,6,7,8], [9,0,11,12], [13, 14, 15, 10]]
for i in range(2):
    for j in range(2):
        print(a[i][j])

i = 0
j = 2

while i < 3:
    for x in range(i, j):
	    for y in range(i, j):
		    print(x, y, a[x][y])
    i += 1
    j += 1

 # for i in range(4):
    #     l = i
    #     for k in [i-1] * 4:
    #         hourglass = []
    #         for j in range(l, l+3):
    #             val1 = arr[i][j]
    #             if j != 0 and j != 2:
    #                 val2 = arr[i+1][j]
    #                 hourglass.append((i+1, j, val2))
    #             hourglass.append((i, j, val1))
    #             val3 = arr[i+2][j]
    #             hourglass.append((i+2, j, val3))
    #         l += 1
    #         if l > 3:break


    def minimumBribes(q):
    total_bribe = 0
    for val_ind in range(len(q) - 1):
        bribe = 0
        for v in range(val_ind+1, len(q)):
            if q[v] < q[val_ind]:
                bribe += 1
            if bribe > 2:
                print("Too chaotic")
                return
        total_bribe += bribe
    print(total_bribe)


def minimumSwaps(arr):
    counter = 0
    for i in range(len(arr)-1):
        small, ind = 9999999, -1
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                if min(small, arr[j]) < small:
                    small, ind = arr[j], j
        if ind > 0:
            arr[i], arr[ind] = arr[ind], arr[i]
            counter +=1
    return counter
