import numpy as np

def match_score(a, b, m, mm):
    if a == b:
        return m
    else:
        return mm

def sw(seq1, seq2, match, mm, gap):
    n, m = len(seq1), len(seq2)
    
    max_score = -1
    max_cell = (-1, -1)
    
    score = np.zeros((m + 1, n + 1))
    trace = np.zeros((m + 1, n + 1))
     
    if gap > 0:
        score[:,0] = np.linspace(0, gap * m, m + 1)
        score[0,:] = np.linspace(0, gap * n, n + 1)
        trace[:,0] = np.linspace(2, 2, m + 1)
        trace[0,:] = np.linspace(1, 1, n + 1)
        
    trace[0][0] = 0
       
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match_ = score[i - 1][j - 1] + match_score(seq1[j-1], seq2[i-1], match, mm)
            delete = score[i - 1][j] + gap
            insert = score[i][j - 1] + gap
            score[i][j] = max(0, match_, delete, insert)
            
            if score[i][j] >= max_score:
                max_cell = (i, j)
                max_score = score[i, j]
                
            if score[i][j] == 0: 
                trace[i][j] = 0
            elif score[i][j] == insert: 
                trace[i][j] = 1
            elif score[i][j] == delete: 
                trace[i][j] = 2   
            elif score[i][j] == match_: 
                trace[i][j] = 3
                
    rseq1, rseq2 = [], []
    (max_i, max_j) = max_cell
    
    
    while trace[max_i][max_j] != 0:
        if trace[max_i][max_j] == 3:
            rseq1 += seq1[max_j - 1]
            rseq2 += seq2[max_i - 1]
            max_i -= 1
            max_j -= 1
        elif trace[max_i][max_j] == 1:
            rseq1 += seq1[max_j - 1]
            rseq2 += '_'
            max_j -= 1
        elif trace[max_i][max_j] == 2:
            rseq1 += '_'
            rseq2 += seq2[max_i - 1]
            max_i -= 1
     
    for i in range(max_cell[1], n):
        rseq1 = [seq1[i].lower()] + rseq1
    for i in range(max_cell[0], m):
        rseq2 = [seq2[i].lower()] + rseq2
    

    for i in range(max_j - 1, -1, -1):
        rseq1 = rseq1 + [seq1[i].lower()]
    for i in range(max_i - 1, -1, -1):
        rseq2 =  rseq2 + [seq2[i].lower()]
    
        
    rseq1 = ''.join(rseq1)[::-1]
    rseq2 = ''.join(rseq2)[::-1]
    max_s = str(max_score)
    return ' '.join([max_s, rseq1, rseq2])
    

seqs = (input().strip()).split(' ')
print(sw(seqs[0], seqs[1], int(seqs[2]), int(seqs[3]), int(seqs[4])))
