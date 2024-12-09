import numpy as np

def check_matrix(sm):
    # check for A in middle
    if sm[1][1] != 'A':
        return False
    # check first diagonal (top left bottom right)
    if sm[0][0] == 'M' and sm[2][2] == 'S' or sm[0][0] == 'S' and sm[2][2] == 'M':
        # check second diagonal (top right bottom left)
        if sm[0][2] == 'M' and sm[2][0] == 'S' or sm[0][2] == 'S' and sm[2][0] == 'M':
            return True
    return False

def ceres_search_2():
    with open("input.txt", "r") as file:
        input_data = file.readlines()

    m = list()

    for line in input_data:
        m.append(list(line.rstrip())) # no padding needed

    sum = 0
    for r in range(0,len(m)-2):
        for c in range(0,len(m[0])-2):
            submatrix = np.array([[m[r][c],   m[r][c+1],   m[r][c+2]],
                                  [m[r+1][c], m[r+1][c+1], m[r+1][c+2]],
                                  [m[r+2][c], m[r+2][c+1], m[r+2][c+2]]])
            sum += check_matrix(submatrix)
    print(sum)





ceres_search_2()