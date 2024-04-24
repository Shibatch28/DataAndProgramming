'''
---------------------------
    課題1: 段階的詳細化
    日付: 2024/04/24
    学籍番号: 50111012
    名前: 大芝 峻平
    どんな処理か: 3元1次方程式をLU分解法により解く
---------------------------
'''

# Doolittle法に基づいて対角成分を振り分ける
def doolittle(component):
    return 1, component

# 3行3列の配列に対してLU分解を行い，
# 配列lowerとupperに結果を返す
def LU_dec(array):
    m = [[0] * 3 for i in range(3)]
    lower = [[0] * 3 for i in range(3)]
    upper = [[0] * 3 for i in range(3)]

    for i in range(3):
        for k in range(i + 1, 3):
            m[k][i] = array[k][i] / array[i][i]
            lower[k][i] = m[k][i]
            for j in range(i + 1, 3):
                array[k][j] = array[k][j] - m[k][i] * array[i][j]
        for j in range(i + 1, 3):
            upper[i][j] = array[i][j]
        lower[i][i], upper[i][i] = doolittle(array[i][i])
    return lower, upper

# LU分解法を用いて3元連立方程式を解く
def solve_equation(coefficient, vector):
    lower, upper = LU_dec(coefficient)
    y = [0] * 3
    # 前進代入: Ly = b
    for i in range(3):
        y[i] = vector[i]
        for j in range(i):
            y[i] -= lower[i][j] * y[j]
        y[i] /= lower[i][i]
    
    x = [0] * 3
    # 後進代入: Ux = y
    for i in range(2, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, 3):
            x[i] -= upper[i][j] * x[j]
        x[i] /= upper[i][i]
    return x

# 3次方程式を表示する
def printm(arr33, arr31):
    for i in range(3):
        print('|', end=' ')
        for j in range(3):
            print(arr33[i][j],end=' ')
        print('|', end='')
        if i == 1:
            print(f'|x{i}|=|{arr31[i]:.2f}|')
        else:
            print(f'|x{i}| |{arr31[i]:.2f}|')


arr = [ [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1] ]
vec = [1, 2, 3]
print('solve this')
printm(arr, vec)
ans = solve_equation(arr, vec)
print(ans)
