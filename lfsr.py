import requests
from bs4 import BeautifulSoup

def lfsr(polynomial, binary):

    bin = binary
    # polynomial 为输入的多项式，binary 为输入的二进制数
    bits = list(binary)

    register = bits.copy()

    register_length = len(register)

    # 创建一个txt文件命名为output加polynomial的值，用于存储输出的序列
    # 以写的格式打开txt文件
    output = open("output"+polynomial+".txt", "w")
    # 清空文件内容
    output.truncate()
    num = 0

    output.write(''.join(register))
    output.write(" / \n")


    while True:
        # 计算异或值
        next_bit = sum(int(register[i]) * int(polynomial[i]) for i in range(register_length)) % 2

        # 左移一位
        register.pop(0)

        # 将异或值添加到最右边
        register.append(str(next_bit))

        # 以字符串的形式写入文件
        temp = ''.join(register)
        
        output.write(temp)
        output.write(" / \n")
        num += 1

        if temp == bin:
            break
    
    return num
#判断polynomial是否是本源多项式
def is_primitive(polynomial):
    polynomial += "1"
    try:
        response = requests.get("http://www.ee.unb.ca/cgi-bin/tervo/factor.pl?binary={}".format(polynomial), timeout=5)
        response.raise_for_status()  # 如果响应状态不是200，引发HTTPError异常
    except requests.exceptions.RequestException as err:
        print ("请求错误：",err)
        return False
    soup = BeautifulSoup(response.text, "html.parser")
    span_tag = soup.find_all('span')
    for spans in span_tag:
        if 'style' in spans.attrs and spans['style'] == "color:grey; font-weight:bold;":
            if spans.string == "IRREDUCIBLE":
                return True
    return False


if __name__ == '__main__':
    polynomial = "10001110"
    binary = "11011000"
    flag = is_primitive(polynomial)
    if flag:
        print("输入{}是本源多项式",polynomial)
    else:
        print("输入不是本源多项式")
    output = lfsr(polynomial, binary)
    print("序列周期是:",output)