import numpy as np

global seq
seq = input()

def score(A, B):
    pairs = [('A', 'U'), ('U', 'A'),
             ('C', 'G'), ('G', 'C')]
    if (A, B) in pairs:
        return 1
    else:
        return 0

def nussinov():
    n = len(seq)
    mll = 3
    
    mat = [[0 for i in range(n)] for i in range(n)]
    
    for k in range(1, n):
        for i in range(n - k):
            j = i + k
            if j - i >= mll + 1:
                down = mat[i + 1][j] 
                left = mat[i][j - 1] 
                diag = mat[i + 1][j - 1] + score(seq[i], seq[j])
                rc = max([mat[i][t] + mat[t + 1][j] for t in range(i, j)])
                mat[i][j] = max(down, left, diag, rc)
            else:
                mat[i][j] = 0
    return mat

def trace(mat, i, j):                
    if i <= j:
        if mat[i][j] == mat[i + 1][j]:
            trace(mat, i + 1, j)
        elif mat[i][j] == mat[i][j - 1]:
            trace(mat, i, j - 1)
        elif mat[i][j] == mat[i + 1][j - 1] + 1 and score(seq[i], seq[j]):
            print(i + 1, j + 1, end=' ')
            trace(mat, i + 1, j - 1)
        else:
            for k in range(i + 1, j):
                if mat[i][j] == mat[i][k] + mat[k + 1][j]:
                    trace(mat, i, k)
                    trace(mat, k + 1, j)
                    break

m = nussinov()
trace(m, 0, len(seq) - 1)
