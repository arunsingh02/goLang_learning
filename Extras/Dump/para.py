import os, sys

def get_para_status(exp):
    s = []
    for x in exp:
        if x in ['(', ')']:
            if x == ')':
                try:
                    s.pop()
                except:
                    print "Exp wrong"
                    return
            elif x == '(':
                s.append(x)
    if not s:print "Correct"
    else:print "wrong"

def get_complex_para_status(comp_exp):
    cb = ')]}'
    sb = '([{'
    s = []
    for x in comp_exp:
        if x in cb:
            if s and s[-1] == sb[cb.index(x)]:
                try:
                    s.pop()
                except:
                    print "Exp Wrong"
                    return
            else:
                print s
                print "Exp Wrong"
                return 
        elif x in sb:
            s.append(x)
    if not s:print "Correct"
    else:
        print s
        print "wrong"


exp = '(a+b)*(c+(d/100)*10)-()*(e-f)'

comp_exp = '(a+b)*[[]100+{c[()]}]/{2/(d/100)}*10'
#get_para_status(exp)
get_complex_para_status(comp_exp)
