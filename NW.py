import numpy as np

def match_score(alpha, beta):
    if alpha == beta:
        return 1
    else:
        return -1 # так как значения штрафов за несовпадение и гэп равны

def nw(seq1, seq2):
    
    n, m = len(seq1), len(seq2)
    
    score = np.zeros((m + 1, n + 1))
    
    score[:,0] = np.linspace(0, -m, m + 1)
    score[0,:] = np.linspace(0, -n, n + 1)
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score[i - 1][j - 1] + match_score(seq1[j-1], seq2[i-1])
            delete = score[i - 1][j] - 1
            insert = score[i][j - 1] - 1
            score[i][j] = max(match, delete, insert)
    
    i, j = m, n
    rseq1, rseq2 = [], []
    
    while i > 0 or j > 0:
        score_current = score[i][j]
        score_diagonal = score[i-1][j-1]
        score_up = score[i][j-1]
        score_left = score[i-1][j]
        
        if score_current == score_diagonal + match_score(seq1[j-1], seq2[i-1]):
            rseq1 += seq1[j-1]
            rseq2 += seq2[i-1]
            i -= 1
            j -= 1
        elif score_current == score_up - 1:
            rseq1 += seq1[j-1]
            rseq2 += '_'
            j -= 1
        elif score_current == score_left - 1:
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
print(nw(seqs[0], seqs[1]))
