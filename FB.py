import numpy as np
from math import exp, log 

array = (input().strip()).split(' ')

a, b = [0, 0, 0, 0], [0, 0, 0, 0]
p = [np.float64(array[0]), np.float64(array[1])]
o = array[-1]

for i in range(4):
    a[i] = np.float64(array[i + 2])
    b[i] = np.float64(array[i + 6])

s = {'+': p[0], '-': p[1]}
tr = {
    '+': {'+': a[0], '-': a[1]},
    '-': {'+': a[2], '-': a[3]},
}
em = {
    '+': {'0': b[0], '1': b[1]},
    '-': {'0': b[2], '1': b[3]},
}

def for_back(o, s, tr, em):
    #forward
    
    k = len(o)
    alpha = [[exp(log(s['+']) + log(em['+'][o[0]]))], [exp(log(s['-']) + log(em['-'][o[0]]))]]
    for i in range(1, k):
        alp1 = (exp(log(alpha[0][-1]) + log(em['+'][o[i]]) + log(tr['+']['+'])) + 
               exp(log(alpha[1][-1]) + log(em['+'][o[i]]) + log(tr['-']['+'])))
        alp2 = (exp(log(alpha[0][-1]) + log(em['-'][o[i]]) + log(tr['+']['-'])) + 
               exp(log(alpha[1][-1]) + log(em['-'][o[i]]) + log(tr['-']['-'])))
        alpha[0].append(alp1)
        alpha[1].append(alp2)
        
    #backward
    beta = [[1], [1]]
    for i in range(1, k):
        bet1 = (exp(log(beta[0][-1]) + log(tr['+']['+']) + log(em['+'][o[k - i]])) + 
               exp(log(beta[1][-1]) + log(tr['+']['-']) + log(em['-'][o[k - i]])))
        bet2 = (exp(log(beta[0][-1]) + log(tr['-']['+']) + log(em['+'][o[k - i]])) + 
               exp(log(beta[1][-1]) + log(tr['-']['-']) + log(em['-'][o[k - i]])))
        beta[0].append(bet1)
        beta[1].append(bet2)
    
    #probability
    alpha_sum = alpha[0][-1] + alpha[1][-1]
    prob = [[], []]

    
    for i in range(k):
        prob[0].append(alpha[0][i] * beta[0][k - i - 1] / alpha_sum)
        prob[1].append(alpha[1][i] * beta[1][k - i - 1] / alpha_sum)

    return prob

a = for_back(o, s, tr, em)
for x in a[0]:
    print(round(x, 2), end=' ')
print()
for x in a[1]:
    print(round(x, 2), end=' ')
