import numpy as np

def match_score(a, b, m, mm):
    if a == b:
        return m
    else:
        return mm

def mg(seq1, seq2, mat, mm, p, gap):
    n, m = len(seq1), len(seq2)
    
    s = [[-1000000 for i in range(m+1)] for j in range(n+1)]
    t = [[-1000000 for i in range(m+1)] for j in range(n+1)]
    u = [[-1000000 for i in range(m+1)] for j in range(n+1)]
    
    s[0][0], t[0][0], u[0][0] = 0, 0, 0
    
    for i in range(1, m + 1):
        u[0][i] = gap * i + p
    for i in range(1, n + 1):
        t[i][0] = gap * i + p
    
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            match = s[i - 1][j] + (gap + p)
            delete = t[i - 1][j] + gap 
            insert = u[i - 1][j] + gap + p
            t[i][j] = max(match, delete, insert)
                
            match = s[i][j - 1] + (gap + p)
            delete = t[i][j - 1] + gap + p
            insert = u[i][j - 1] + gap
            u[i][j] = max(match, insert, delete)
            
            match = s[i - 1][j - 1] + match_score(seq1[i-1], seq2[j-1], mat, mm)
            delete = u[i - 1][j - 1] + match_score(seq1[i-1], seq2[j-1], mat, mm)
            insert = t[i - 1][j - 1] + match_score(seq1[i-1], seq2[j-1], mat, mm)
            s[i][j] = max(match, delete, insert)
            
    max_score = str(max(s[n][m], u[n][m], t[n][m]))
    
    return ' '.join([max_score, seq1, seq2])
    
    
seqs = (input().strip()).split(' ')
print(mg(seqs[0], seqs[1], int(seqs[2]), int(seqs[3]), int(seqs[4]), int(seqs[5])))
