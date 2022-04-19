import numpy as np

def match_score(alpha, beta, matrix):
    dict_ = {'A' : 0,
             'T' : 1,
             'G' : 2,
             'C' : 3}
    
    return matrix[dict_[alpha]][dict_[beta]]

def nw(seq1, seq2, gap, matrix):
    
    n, m = len(seq1), len(seq2)
    
    score = np.zeros((m + 1, n + 1))
    
    score[:,0] = np.linspace(0, gap * m, m + 1)
    score[0,:] = np.linspace(0, gap * n, n + 1)
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score[i - 1][j - 1] + match_score( seq2[i-1], seq1[j-1], matrix)
            delete = score[i - 1][j] + gap
            insert = score[i][j - 1] + gap
            score[i][j] = max(match, delete, insert)
    
    i, j = m, n
    rseq1, rseq2 = [], []
    
    while i > 0 or j > 0:
        score_current = score[i][j]
        score_diagonal = score[i-1][j-1]
        score_up = score[i][j-1]
        score_left = score[i-1][j]
        
        if i>0 and j >0 and score_current == score_diagonal + match_score(seq1[j - 1], seq2[i - 1], matrix):
            rseq1 += seq1[j-1]
            rseq2 += seq2[i-1]
            i -= 1
            j -= 1
        elif j > 0 and score_current == score_up + gap:
            rseq1 += seq1[j-1]
            rseq2 += '_'
            j -= 1
        elif score_current == score_left + gap:
            rseq1 += '_'
            rseq2 += seq2[i-1]
            i -= 1
    
    while j > 0:
        rseq1 += seq1[j-1]
        rseq2 += '_'
        j -= 1
    while i > 0:
        rseq1 += '_'
        rseq2 += seq2[i-1]
        i -= 1
    
    rseq1 = ''.join(rseq1)[::-1]
    rseq2 = ''.join(rseq2)[::-1]
    return ' '.join([rseq1, rseq2])

seqs = (input().strip()).split(' ')
matrix = [[0 for i in range(4)] for i in range(4)]
gap = int(seqs[2])
k = 0
for i in range(4):
    for j in range(4):
        matrix[i][j] = int(seqs[3 + k])
        k += 1
print(nw(seqs[0], seqs[1], gap, matrix))
