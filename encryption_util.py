import base64
from Crypto.Cipher import AES, DES, DES3,PKCS1_OAEP
from Crypto.PublicKey import DSA, ECC, RSA
from Crypto.Hash import MD5, SHA1


def Base64Encrythion(content):
    return base64.b64encode(str(content).encode("utf-8")).decode()


def MD5Encrytion(content):
    return MD5.MD5Hash(str(content).encode("utf-8")).hexdigest()


def SHA1Encrytion(content):
    return SHA1.SHA1Hash(str(content).encode("utf-8")).hexdigest()


#######################################AES加密##########################################

#  bytes不是32的倍数那就补足为32的倍数
def add_to_32(value):
    while len(value) % 32 != 0:
        value += b'\x00'
    return value  # 返回bytes


# str转换为bytes超过32位时处理
def cut_value(org_str):
    org_bytes = str.encode(org_str)
    n = int(len(org_bytes) / 32)
    i = 0
    new_bytes = b''
    while n >= 1:
        i = i + 1
        new_byte = org_bytes[(i - 1) * 32:32 * i - 1]
        new_bytes += new_byte
        n = n - 1
    if len(org_bytes) % 32 == 0:  # 如果是32的倍数，直接取值
        all_bytes = org_bytes
    elif len(org_bytes) % 32 != 0 and n > 1:  # 如果不是32的倍数，每次截取32位相加，最后再加剩下的并补齐32位
        all_bytes = new_bytes + add_to_32(org_bytes[i * 32:])
    else:
        all_bytes = add_to_32(org_bytes)  # 如果不是32的倍数，并且小于32位直接补齐
    return all_bytes


def AES_encrypt(org_str, key):
    try:
        # 初始化加密器
        aes = AES.new(cut_value(key), AES.MODE_ECB)
        # 先进行aes加密
        encrypt_aes = aes.encrypt(cut_value(org_str))
        # 用base64转成字符串形式
        encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
        return (encrypted_text)
    except:
        return None


def AES_decrypt(secret_str, key):
    try:
        # 初始化加密器
        aes = AES.new(cut_value(key), AES.MODE_ECB)
        # 优先逆向解密base64成bytes
        base64_decrypted = base64.decodebytes(secret_str.encode(encoding='utf-8'))
        # 执行解密密并转码返回str
        decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')
        return decrypted_text
    except:
        return None


#######################################END AES加密##########################################


#######################################DES加密##############################################

def DESEncrytion(text, key):
    try:
        key=key.encode()
        # 需要去生成一个DES对象
        des = DES.new(key, DES.MODE_ECB)
        # 需要加密的数据
        text = text + (8 - (len(text) % 8)) * '\0'
        text = text.encode()
        # 加密的过程
        encrypto_text = des.encrypt(text)
        return base64.b64encode(encrypto_text).decode()
    except:
        return None


def DESDecryption(text, key):
    try:
        text=base64.b64decode(text)
        key = key.encode()
        # 需要去生成一个DES对象
        des = DES.new(key, DES.MODE_ECB)
        # 加密的过程
        decrypt_text = des.decrypt(text)
        return decrypt_text.decode().rstrip("\0")
    except:
        return None


#######################################END DES加密##############################################


#######################################3DES加密##############################################

BS = DES3.block_size


def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def unpad(s):
    return s[0:-ord(s[-1])]


class DES3Encryt():
    def __init__(self, key):
        self.key = key
        self.mode = DES3.MODE_ECB

    def encrypt(self, text):
        try:
            text = pad(text)
            cryptor = DES3.new(self.key, self.mode)
            x = len(text) % 8
            if x != 0:
                text = text + '\0' * (8 - x)
            # print(text)
            self.ciphertext = cryptor.encrypt(text.encode())
            return base64.standard_b64encode(self.ciphertext).decode("utf-8")
        except:
            return None

    def decrypt(self, text):
        try:
            cryptor = DES3.new(self.key, self.mode)
            de_text = base64.standard_b64decode(text)
            plain_text = cryptor.decrypt(de_text)
            st = str(plain_text.decode("utf-8")).rstrip('\0')
            out = unpad(st)
            return out
        except:
            return None


#######################################END 3DES加密##############################################


#######################################RSA加密##############################################

def get_rsa_key():
    key = RSA.generate(2048)
    return key.export_key(), key.publickey().export_key()

def RSAEncryt(text,key):
    key=RSA.import_key(key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_data = cipher.encrypt(text.encode())
    encrypted_data = base64.b64encode(encrypted_data)
    return encrypted_data.decode()

def RSADecrypt(text,key):
    key = RSA.import_key(key)
    cipher = PKCS1_OAEP.new(key)
    data = cipher.decrypt(base64.b64decode(text))
    return data.decode("utf-8")


if __name__ == '__main__':
    # print(Base64Encrythion("我是李浩wqewqeqwe"))
    # print(SHA1Encrytion("12"))
    # print(AES_encrypt("我叫李好", "123"))
    # print(AES_decrypt(AES_encrypt("我叫李好", "123"), "123"))
    #
    # print(DESEncrytion("woshilihao", b'12345678'))
    # print(DESDecryption(DESEncrytion("woshilihao", b'12345678'), b"12345678"))
    #
    # des3 = DES3Encryt("kkk1111121311111".encode())
    # print(des3.encrypt("我是李浩"))
    # print(des3.decrypt(des3.encrypt("我是李浩")))

    # private_key ,public_key= get_rsa_key()
    #
    # # 加密
    # print(RSAEncryt("李浩",public_key))
    #
    # # 解密
    # print(RSADecrypt(RSAEncryt("李浩",public_key),private_key))
    print(DESDecryption("yR1Em4q0avo=","12345678"))
    print(DESEncrytion("老李","12345678"))
    pass










