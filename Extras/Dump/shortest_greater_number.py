
def gno(num):
    kstr = str(num)
    print 'old : ', kstr
    nstr  = [i for i in kstr]
    gstr = nstr[:]
    all_d = []
    flg = 0
    for i in range(len(nstr)-1, -1, -1):
        for j in range(len(nstr)):
            nstr[i], nstr[i-j] = nstr[i-j], nstr[i]
            print nstr
            if int(num) < int(''.join(nstr)):
                print ''.join(nstr)
                all_d.append(int(''.join(nstr)))
                #flg = 1
                #break
            nstr = gstr[:]
        #if flg:break
    print all_d
    last = min(all_d)
    return last


from itertools import permutations
def gno_new(num):
    kstr = str(num)
    all_poss = []
    for i in permutations(kstr, len(kstr)):
        cur_n = int(''.join(list(i)))
        if num < cur_n:
            all_poss.append(cur_n)
    
    x = sorted(all_poss)
    f, s = x[0], x[1]
    if f < s:
        f, s = x[1], x[0]
    for n in x[2:]:
        if n > f:
            s = f
            f = n
        elif n > s:
            s = n
    print min(x)
    print x
    print f, s
    return 'done'
        

print gno_new(5617)
#print gno_new(1234)
            
        
