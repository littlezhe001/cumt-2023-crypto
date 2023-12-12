key = [[2,2,1],[3,2,2],[1,2,1]]   
text = [3,2,1]
crypto = [13,12,8]

#向量和矩阵的乘法
def cal_mul(key, text):
    temp = 0
    res = []
    for i in range(len(text)):
        for j in range(len(text)):
            temp += text[j]*key[j][i]
        temp = temp % 26
        res.append(temp)
        temp = 0
    return res
print("密钥", key,"\n明文", text)
print(cal_mul(key, text))
#计算矩阵的行列式
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    else:
        total = 0
        for i in range(n):
            sub_matrix = [row[:i] + row[i+1:] for row in matrix[1:]]
            total += ((-1) ** i) * matrix[0][i] * determinant(sub_matrix)
        return total
# print(determinant(key, 3))
#计算矩阵的转置
def cal_transpose(matrix):
    transpose = []
    for i in range(len(matrix[0])):
        transpose_row = []
        for row in matrix:
            transpose_row.append(row[i])
        transpose.append(transpose_row)
    return transpose
#计算最大公因数
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
#计算矩阵的逆
def cal_inverse(key):
    res = []
    temp = []
    matrix_num = determinant(key)
    if matrix_num == 0 | gcd(matrix_num, 26) != 1:
        print("矩阵不可逆")
        return
    # print(matrix_num,"\n")
    for i in range(len(key)):
        for j in range(len(key)):
            sub_matrix = [row[:j] + row[j+1:] for row in key[:i] + key[i+1:]]
            temp.append(((-1)**(i+j))*determinant(sub_matrix)/matrix_num)
        res.append(temp)
        temp = []
    return cal_transpose(res)
print("逆矩阵", cal_inverse(key))
print("密文", crypto)
print("解密",cal_mul(cal_inverse(key), crypto))