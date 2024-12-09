import numpy as np

def scan_matrix(sm):
    xmas = 0
    for rotation in range(0,4):
        # scan the first row
        if ''.join(sm[0]) == 'XMAS':
            xmas +=1
        # scan the one diagonal from top left to bottom right:
        if ''.join([sm[0][0],sm[1][1],sm[2][2],sm[3][3]]) == 'XMAS':
            xmas += 1
        # rotate the matrix by 90 degrees
        sm = np.rot90(sm)
    return xmas

def ceres_search_1():
    with open("input.txt", "r") as file:
        input_data = file.readlines()

    m = list()

    for line in input_data:
        m.append(list('...' + line.rstrip() + '...')) # includes 3 columns padding before & after
    for i in range(0,3):
        m.insert(0,list('.'*len(m[0]))) # add 3 rows padding before
        m.append(list('.'*len(m[0]))) # add 3 rows padding after

    sum = 0
    for r in range(0,len(m)-3):
        for c in range(0,len(m[0])-3):
            submatrix = np.array([[m[r][c],   m[r][c+1],   m[r][c+2],   m[r][c+3]],
                                  [m[r+1][c], m[r+1][c+1], m[r+1][c+2], m[r+1][c+3]],
                                  [m[r+2][c], m[r+2][c+1], m[r+2][c+2], m[r+2][c+3]],
                                  [m[r+3][c], m[r+3][c+1], m[r+3][c+2], m[r+3][c+3]]])
            sum += scan_matrix(submatrix)
    print(sum)





ceres_search_1()