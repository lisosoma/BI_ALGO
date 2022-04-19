import numpy as np
from math import exp, log 

array = (input().strip()).split(' ')

a, b = [0, 0, 0, 0], [0, 0, 0, 0]
p = [np.float64(array[0]), np.float64(array[1])]
o = array[-1]

for i in range(4):
    a[i] = np.float64(array[i + 2])
    b[i] = np.float64(array[i + 6])
    
S = ['+', '-']
s = {'+': p[0], '-': p[1]}
tr = {
    '+': {'+': a[0], '-': a[1]},
    '-': {'+': a[2], '-': a[3]},
}
em = {
    '+': {'0': b[0], '1': b[1]},
    '-': {'0': b[2], '1': b[3]},
}

def viterbi(o, S, s, tr, em):
    V, seq = [{}], []
    n, mp, bst = len(o), 0, -1
    
    for st in S:
        V[0][st] = {'p': exp(log(s[st]) + log(em[st][o[0]])), 'pr': -1}
        
    for t in range(1, n):
        V.append({})
        
        for st in S:
            max_V = exp(log(V[t-1][S[0]]['p']) + log(tr[S[0]][st]))
            pr_s = S[0]
            
            for pr in S:
                tr_prob = exp(log(V[t-1][pr]['p']) + log(tr[pr][st]))
                if tr_prob > max_V:
                    max_V = tr_prob
                    pr_s = pr
 
            max_prob = exp(log(max_V) + log(em[st][o[t]]))
            V[t][st] = {'p': max_prob, 'pr': pr_s}
 
    for st, d in V[-1].items():
        if d['p'] > mp:
            mp = d['p']
            bst = st
            
    seq.append(bst)
    prev = bst
    k = len(V) - 2
 
    for t in range(k, -1, -1):
        seq.insert(0, V[t + 1][prev]['pr'])
        prev = V[t + 1][prev]['pr']
 
    return (''.join(seq))
    
print(viterbi(o, S, s, tr, em))
