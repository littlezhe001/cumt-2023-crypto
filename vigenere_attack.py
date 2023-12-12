from itertools import product



#计算一个数组里的两个元素的重合概率
def coincidence_index(arr):
    if len(arr) < 2:
        return 0
    #统计各个元素出现的次数
    count = {}
    for i in arr:
        if i not in count:
            count[i] = 0
        count[i] += 1
    #计算重合概率
    coincidence_index = 0
    for i in count:
        coincidence_index += count[i] * (count[i] - 1)
    coincidence_index /= len(arr) * (len(arr) - 1)
    return coincidence_index



#使用重合指数法求解密钥长度
def find_key_length(ciphertext):
    max_length = 7
    coincidence_indices = [0] * max_length
    for pro_key_length in range(2, max_length):
        # 将密文分组
        groups = [[] for _ in range(pro_key_length)]
        for i in range(len(ciphertext)):
            groups[i % pro_key_length].append(ciphertext[i])
        # #以字符串的样子输出分组
        # for i in range(pro_key_length):
        #     print("分组为",pro_key_length,"时，第", i, "组：", ''.join(groups[i]))
        # 计算每个分组的重合指数
        for i in range(pro_key_length):
            coincidence_indices[pro_key_length] += coincidence_index(groups[i])
        coincidence_indices[pro_key_length] /= pro_key_length
    # 寻找和0.065最接近的重合指数、
    min_difference = 1
    key_length = 1
    for i in range(2, max_length):
        print("可能密钥长度为", i, "时，重合指数为", coincidence_indices[i])
        if abs(coincidence_indices[i] - 0.065) < min_difference:
            min_difference = abs(coincidence_indices[i] - 0.065)
            key_length = i
    
    return key_length


# def decrypt(ciphertext, key_length):
#     groups = [[] for _ in range(key_length)]
#     for i in range(len(ciphertext)):
#         groups[i % key_length].append(ciphertext[i])
#     temp_groups = [list(group) for group in groups]  
#     min_diff = 0.5
#     permutations = generate_permutations(key_length)
#     for str in permutations:
#         for i in range(key_length):
#             for j in range(len(groups[i])):
#                 temp_groups[i][j] = chr( (ord(groups[i][j]) + ord(str[i]) - 2*ord('a')) % 26 + ord('a') )
#         temp = ''.join(''.join(row) for row in temp_groups)
#         diff = abs(coincidence_index(temp) - 0.065)
#         if str == 'fnd' :
#             record_txt = temp
#             record_diff = diff
#         if diff < min_diff:
#             min_diff = diff
#             key = str
#         print("尝试密钥为", str, "时，位移后的文本为：", temp , "重合指数与0.065绝对值为：", diff)
#     print("最终密钥为", key, "时，位移后的文本为：", temp , "重合指数与0.065绝对值为：", min_diff)
#     print("密钥为'fnd'时，位移后的文本为：", record_txt , "重合指数与0.065绝对值为：", record_diff)
#     return key

def keyword(Ciphertext,keylength):
    ListCiphertext = list(Ciphertext)
    #标准数据来源于课本
    Standard = {'a':0.082,'b':0.015,'c':0.028,'d':0.043,'e':0.127,'f':0.022,'g':0.020,'h':0.061,'i':0.070,'j':0.002,'k':0.008,'l':0.040,'m':0.024,'n':0.067,'o':0.075,'p':0.019,'q':0.001,'r':0.060,'s':0.063,'t':0.091,'u':0.028,'v':0.010,'w':0.023,'x':0.001,'y':0.020,'z':0.001}

    while True:
        KeyResult = []

        for i in range(keylength):
            # 使用切片分组
            PresentCipherList = ListCiphertext[i::keylength]

            #初始化重合指数最大值为０，检验移动位数对应字符以＊代替
            QuCoincidenceMax = 0
            KeyLetter = "*"

            #遍历移动的位数
            #m是密钥对应的英文字母
            for m in range(26):
                #初始化当前移动位数的重合互指数为０
                QuCoincidencePresent = 0

                #遍历计算重合指数：各个字符的频率＊对应英文字符出现的标准频率－－－的和
                for Letter in set(PresentCipherList):
                    #fi/n
                    LetterFrequency = PresentCipherList.count(Letter) / len(PresentCipherList)

                    # 标准频率
                    #ord(Letter) - 65是将letter对应的字母化为26内的数值，然后与m运算，得到的k是对应的明文字母
                    k = chr( ( ord(Letter) - ord('a') - m ) % 26 + ord('a') )
                    StandardFrequency = Standard[k]

                    #计算重合互指数，累加遍历26个英文字母
                    QuCoincidencePresent = QuCoincidencePresent + LetterFrequency * StandardFrequency

                #保存遍历过程中重合指数的最大值，同时保存对应应对的位数，即对应key的字符
                if QuCoincidencePresent > QuCoincidenceMax:
                    QuCoincidenceMax = QuCoincidencePresent
                    #m是26个英文对应的位置，从0开始，+65是因为A在ascii中是65
                    KeyLetter = chr( m + ord('a') )
            print("第",i+1,"个密钥字母为:",KeyLetter,"对应的重合互指数为:",QuCoincidenceMax)
            #保存当前位置key的值，退出循环，进行下一组子密文移动位数的尝试
            KeyResult.append( KeyLetter )
        #列表转为字符串
        Key = "".join(KeyResult)
        break
    return Key


def generate_permutations(key_length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    permutations = [''.join(p) for p in product(alphabet, repeat=key_length)]
    return permutations

if __name__ == '__main__':
    # 输入加密密钥：fhd
    # 输入要加密的文本：todayiloveagirlnamedaliceandsheisgood
    # 加密后的文本： yvgfflqvyjhjnyoshpjkdqpfjhqizkjpvlvri
    arr = "yvgfflqvyjhjnyoshpjkdqpfjhqizkjpvlvri"
    key_length = find_key_length(arr)
    print("密钥长度为", key_length)
    # key = decrypt(arr, key_length)
    key = keyword(arr,key_length)
    print("密钥为", key)
