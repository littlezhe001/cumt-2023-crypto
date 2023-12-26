import random

# 模幂运算
def mod_exp(a, b, n):
    res = 1
    while b != 0:
        if b & 1:
            res = (res * a) % n
        b >>= 1
        a = (a * a) % n
    return res

 # test mod_exp
# a = 3
# b = 5
# n = 7
# print(mod_exp(a, b, n))

# 最大公因数(非递归)
def gcd (a, b):
    a, b = max(a, b), min(a, b)
    while b != 0:
        a, b = b, a % b
    return a

# ranbin-miller 素性检测
def miller_rabin(n, s=50):
    if n in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        return True
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        if n % p == 0:
            return False
    # n-1 = 2^t * u
    u = n - 1
    t = 0
    while u % 2 == 0:
        t += 1
        u //= 2
    # 测试s次
    for i in range(s):
        a = random.randint(1, n-1)
        x = mod_exp(a, u, n)
        for j in range(t):
            y = (x * x) % n
            if y == 1 and x != 1 and x != n-1:
                return False
            x = y
        if x != 1:
            return False
    return True

# 生成大素数
def gen_prime(n):
    while True:
        p = random.randint(2**(n-1), 2**n)
        if miller_rabin(p):
            return p

# 拓展欧几里得算法
def ex_gcd(a, b):
    if b == 0:
        return (1, 0)
    x, y = ex_gcd(b, a % b)
    return (y, x - a // b * y)

# 求模逆
def mod_inverse(a, n):
    x, y = ex_gcd(a, n)
    return x % n
    

# test mod_inverse
# a = 3
# n = 11
# print(mod_inverse(a, n))

# 生成密钥
def gen_key(n):
    p = gen_prime(n)
    q = gen_prime(n//2+1)
    n = p * q
    print("p = %d" % p)
    print("q = %d" % q)
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi)
    d = mod_inverse(e, phi)
    return (n, e, d)

# 加密
def encrypt(msg, n, e):
    return mod_exp(msg, e, n)

# 解密
def decrypt(cipher, n, d):
    return mod_exp(cipher, d, n)


# 测试
if __name__ == '__main__':
    n, e, d = gen_key(30)
    msg = 12345
    cipher = encrypt(msg, n, e)
    msg_ = decrypt(cipher, n, d)
    print("明文: %d" % msg)
    print("密文: %d" % cipher)
    print("解密: %d" % msg_)
