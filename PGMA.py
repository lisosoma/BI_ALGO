def create_matrix(n, array):
    matrix = []
    
    for i in range(n):
        line = []
        for j in range(n - i - 1):
            line.append(array[0])
            del array[0]
        line.reverse()
        matrix.append(line)
    matrix_ =[]
    for i in range(n):
        line = []
        for j in range(i):
            line.append(matrix[j][n - i - 1])
        matrix_.append(line)
            
    return matrix_

global let
let = []
array = (input().strip()).split(' ')
n = int(array[0])
matrix = []
for i in range(int(n * (n - 1) / 2)):
    matrix.append(int(array[i + 2]))
letters = [chr(ord('A') + i) for i in range(n)]
m = create_matrix(n, matrix)
global b
b = list(letters)




def minimum(matrix):
    m, k = -1, -1
    min_ = 99999999

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_:
                min_ = matrix[i][j]
                m, k = i, j
    return m, k


def insert_letters(m, k, letters, score1 = 1, score2 = 1):
    if m > k: m, k = k, m
        
    global let
    
    first_letter = letters[m]
    second_letter = letters[k]
    
    letters[m] = '(' + first_letter + ':' + f'{score1}' + ',' + second_letter + ':' + f'{score2}' + ')'
    a = letters[m]
    let.append(a)
    
    del letters[k]
    
    return(letters)


def insert_matrix(m, k, mat):
    if m > k: m, k = k, m
    line = []
    for i in range(0, m):
        line.append(round(((mat[m][i] + mat[k][i]) / 2), 2))
        
    mat[m] = line
    for i in range(m + 1, k):
        mat[i][m] = round(((mat[i][m] + mat[k][i]) / 2), 2)
        
    for i in range(k + 1, len(mat)):
        mat[i][m] = round(((mat[i][m] + mat[i][k]) / 2), 2)
        del mat[i][k]

    del mat[k]
    
    
def insert_matrix_u(m, k, mat):
    if m > k: m, k = k, m
    line = []
    count1 = 0
    count2 = 0
    for x in letters[k]:
        if x in b:
            count1 += 1
    for x in letters[m]:
        if x in b:
            count2 +=1
    for i in range(0, m):
        line.append(round((( count2 * mat[m][i] + count1 * mat[k][i]) / (count1 + count2)), 2))
        
    mat[m] = line
    for i in range(m + 1, k):
        mat[i][m] = round(((count2 * mat[i][m] + count1 * mat[k][i]) / (count1 + count2)), 2)
        
    for i in range(k + 1, len(mat)):
        mat[i][m] = round(((count2 * mat[i][m] + count1 * mat[i][k]) / (count1 + count2)), 2)
        del mat[i][k]

    del mat[k]


def wpgma(matrix, letters):
    length = 0
    last = 0
    last_ = 0
    while len(letters) > 1:
        a, b = minimum(matrix)
        length = round(matrix[a][b] / 2, 2)
        insert_matrix(a, b, matrix)

        if letters[a] in let or letters[b] in let:
            last = round(length - last_, 2)
        else:
            last = round(length, 2)
        insert_letters(a, b, letters, length, last)
        last_ = length
    return letters[0]


def upgma(matrix, letters):
    length = 0
    last = 0
    last_ = 0
    while len(letters) > 1:
        a, b = minimum(matrix)
        length = round(matrix[a][b] / 2, 2)
        insert_matrix_u(a, b, matrix)

        if letters[a] in let or letters[b] in let:
            last = round(length - last_, 2)
        else:
            last = round(length, 2)
        insert_letters(a, b, letters, length, last)
        last_ = length
    return letters[0]


if array[1] == 'UPGMA':
    print(upgma(m, letters))
else:
    print(wpgma(m, letters))
