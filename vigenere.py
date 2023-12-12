

def vigenere_encrypt(plaintext, key):
    ciphertext = []
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    plaintext = []
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            plaintext.append(decrypted_char)
        else:
            plaintext.append(char)
    return ''.join(plaintext)

if __name__ == '__main__':
    while True:
        mode = eval(input("选择模式（加密(0)/解密(1)):"))
        if mode == 0:
            key = input("输入加密密钥：")
            plaintext = input("输入要加密的文本：")
            ciphertext = vigenere_encrypt(plaintext, key)
            print("加密后的文本：", ciphertext)
        elif mode == 1:
            key = input("输入解密密钥：")
            ciphertext = input("输入要解密的文本：")
            plaintext = vigenere_decrypt(ciphertext, key)
            print("解密后的文本：", plaintext)
        else:
            print("无效模式，请选择 '加密' 或 '解密'")

