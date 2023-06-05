# -*- coding: utf-8 -*-
import bcrypt
import base64
#pip install pycryptodome 安装pycryptodome库才能用下面2个
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
# RSA私钥是以PKCS#1格式编码的,用rsa库即可；PKCS#8格式编码的，可以使用 cryptography 库来加载该私钥
import rsa
# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_v1_5

def base64_knowledge():
    """Base64是一种用于将二进制数据转换为可打印字符的编码方式,它将输入数据划分为固定长度的块，并将每个块转换为相应的可打印字符。
    在前端中，通过使用Base64编码对密码进行处理，是为了将密码从原始的文本格式转换为Base64编码的字符串，以便在传输过程中能够正确处
    理特殊字符和二进制数据。
    """
    pass

def RSA_knowledge():
    """RSA 非对称加密算法
    算法涉及到两个密钥：公钥和私钥。公钥用于加密数据，私钥用于解密数据。公钥可以公开发布，而私钥则必须保密。
    // 密钥对生成 http://web.chacuo.net/netrsakeypair
    RSA算法具有以下特点：
    加密和解密使用不同的密钥，因此被称为非对称加密算法。
    公钥可以公开发布，私钥必须保密。
    RSA算法在数学上的安全性基于大数分解问题的困难性。
    RSA算法广泛应用于数字签名、数据加密、密钥交换等领域。
    需要注意的是，由于RSA算法的运算速度相对较慢，通常用于加密较小数据或者加密密钥等对称加密算法的密钥。
    而对于大量数据的加密，一般会采用对称加密算法，然后使用RSA算法加密对称加密算法的密钥。这样既能保证安全性，又能提高加密和解密的效率。"""
    pass

def AES_knowledge():
    """是一种对称加密算法,AES 使用相同的密钥对数据进行加密和解密操作
    AES 加密过程包括以下步骤：
    密钥扩展：根据输入的密钥生成轮密钥，用于后续的轮次处理。
    初始轮：将明文与第一个轮密钥进行异或操作。
    轮次处理：根据密钥长度，进行多轮的替换、置换和混淆操作。
    最后一轮：在最后一个轮次中，省略混淆步骤，仅进行替换和置换操作。
    输出密文：将最后一轮处理结果作为加密后的密文输出。
    AES 解密过程与加密过程相似，但使用的是逆向操作，通过应用相同的密钥和相反的操作来还原原始明文。

    AES.new(key, AES.MODE_CBC, iv) 是一个创建 AES 加密对象的方法，用于进行使用 CBC（Cipher Block Chaining）模式的 AES 加密操作。
    在这个方法中，key 是用作密钥的字节序列，iv 是用作初始化向量（Initialization Vector）的字节序列。
    AES 加密中的 CBC 模式是一种块密码模式，它涉及将每个明文块与前一个密文块进行异或操作，然后再进行加密。
    为了保证安全性和随机性，第一个块需要使用一个随机生成的初始化向量。
    下面是对每个参数的详细解释：
    key: 密钥
    这是一个字节序列，用作 AES 加密的密钥。
    密钥的长度可以是 16 字节（128 位）、24 字节（192 位）或 32 字节（256 位），根据所需的加密强度选择合适的密钥长度。

    AES.MODE_CBC: 加密模式
    这是 AES 加密的模式之一，表示使用 CBC 模式。
    在 CBC 模式中，每个明文块会与前一个密文块进行异或操作，然后进行加密。

    iv: 初始化向量
    这是一个字节序列，用作 CBC 模式的初始化向量。
    初始化向量是一个随机生成的值，用于增加加密的随机性和安全性。
    初始化向量的长度应与 AES 块大小相等，通常是 16 字节。
    通过调用 AES.new(key, AES.MODE_CBC, iv)，你可以创建一个用于使用 CBC 模式的 AES 加密对象。然后，你可以使用该对象对明文进行加密操作。"""
    pass

def bcrypt_knowledge():
    """bcrypt 是一种密码哈希算法，它是为了提高密码安全性而设计的。它是单向的，意味着无法直接解密哈希值来还原原始密码。
    是一种适合存储密码的哈希函数，它使用了适应性哈希算法，并且会自动处理盐值和哈希迭代次数等参数，以增加密码的安全性。
    在后端中，要解密并验证密码，可以按照以下步骤进行：
    从数据库中获取存储的加密密码（例如，$2a$10$D8I0RDeL2oyupJlNB3qArOYoGwtfo20A3CLCxMSCMn3CqeAJmy96m）以及与之关联的用户信息。
    解密Base64编码的密码。使用Base64解码将其转换回二进制形式的字符串。
    使用bcrypt库中的checkpw函数来验证解密后的密码与数据库中存储的加密密码是否匹配。
    密码验证通常通过将输入的密码使用相同的哈希算法和相同的盐与存储的哈希值进行比较来进行。如果哈希值匹配，那么密码被视为正确。"""
    pass

#公钥和私钥字符串包含了换行符和首尾的标记符号，并且字符串在Python中需要以b前缀表示为字节字符串。
publickey = b'''
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCDb4PRcPMdoX+q2rsFNPkPP/s7
wejFwJGDzcNzlQwzle9iHlWirorYeX6ZZDw3p9n2Dnk6pk1D7TO+b8ZbnWn2ArwR
FF5qnTiodbg9USVWIzl8zQxKVdS9RzQ39GZGVfNSZvuunDsSEWMKMAU2Jtd0N8lT
V/G4JfEFroxQUErL3QIDAQAB
-----END PUBLIC KEY-----
'''

privatekey = b'''
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCDb4PRcPMdoX+q2rsFNPkPP/s7wejFwJGDzcNzlQwzle9iHlWi
rorYeX6ZZDw3p9n2Dnk6pk1D7TO+b8ZbnWn2ArwRFF5qnTiodbg9USVWIzl8zQxK
VdS9RzQ39GZGVfNSZvuunDsSEWMKMAU2Jtd0N8lTV/G4JfEFroxQUErL3QIDAQAB
AoGAEh8yAZKdMpytyZTW7GTdYijkLt0RhxKB/bZFGI6YXBR0KQcdr4x5QFegCO41
D0dpWe+s71U2mgL+e2dV5hPSJBGLjESJF3vRyvpcNeOF6H9TUXeEKLIdpLo6WVVw
nJHv5EJGSj9ELwSWsCfKEAAp4rozptOPidLeHb8lhsSuSwECQQCUaRV8FrZ7963W
0pXxXZ+DwPvIaJmuJUedaEDf74B0Q9l25q8hpPD5v1eTV+2s8+eudDk/wGS5IBHi
zFCw1mLtAkEA4rghVFw2/m1Sq2LByUp9Puxpl81GLcuYzCkEWEpK9zQ5+zqbXobE
B/PMCjLmDCMnydwn1D6Lrd29l00lhic+sQJAVx07zEP0x93Bv/iKpUxEZu0vnhqw
IsWlPONGOWx3ZUeybZXJNSGBhcfoGwgg7kWZOBDmzeIb/YKynQM7ViHxnQJBAKtF
mIAnTbA1HD+20lhjOmyfokF4ZGzSIrMQxWSBc1J+lNKyeo8VVeAAEAMgYmOG51b6
Ruhy+4g0PDahpBhNa3ECQFbTPuUDMlT3qXRnZZL1mKpjZHQk+IWMYg4MQVtEXTv7
HV4K5LIz40RXnvlpkD4awpzSjAG1gVHGEuklY9+zb4A=
-----END RSA PRIVATE KEY-----
'''
def encrypt(txt):
    """RSA加密"""
    public_key=rsa.PublicKey.load_pkcs1_openssl_pem(publickey)
    encrypted_data = rsa.encrypt(txt.encode('utf-8'), public_key)
    print(encrypted_data.hex())
    return encrypted_data.hex()

def decrypt(txt):
    """RSA解密
    binascii.Error: Invalid base64-encoded string: number of data characters (881) cannot be 1 more than a multiple of 4
    错误表明解码的 base64 字符串长度不是 4 的倍数，因此无法进行正确的解码。
    在这种情况下，可能是因为私钥字符串中存在额外的空格、换行符或其他非法字符，导致解码失败。"""
    private_key=rsa.PrivateKey.load_pkcs1(privatekey)
    # decrypted_data = rsa.decrypt(bytes.fromhex(txt), private_key)
    # privatekey_pem = ''.join(privatekey.decode('utf-8').split())
    #load_pkcs1函数用于从 DER 编码的 PKCS#1 格式的数据中加载 RSA 私钥
    # private_key = rsa.PrivateKey.load_pkcs1(base64.b64decode(privatekey))
    decrypted_data = rsa.decrypt(bytes.fromhex(txt), private_key)
    print(decrypted_data.decode('utf-8'))
    return decrypted_data.decode('utf-8')

def encryption(params):
    """前端密码加密逻辑，AES加密"""
    data = params['data']
    type = params['type']
    param = params['param']
    result = data.copy()
    if type == 'Base64':
        for ele in param:
            result[ele] = base64.b64encode(result[ele].encode('utf-8')).decode('utf-8')
    else:
        for ele in param:
            data = result[ele]
            key = params['key'].encode('utf-8')
            iv = key
            cipher = AES.new(key, AES.MODE_CBC, iv)
            encrypted_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
            result[ele] = base64.b64encode(encrypted_data).decode('utf-8')
    # print(result)
    return result

def handleSubmit(values):
    """提交实际登录数据接口，调用encryption加密函数"""
    try:
        encodeData = encryption({
            'data': values,
            'type': 'Base6',
            'key': 'king,house,cloud',
            'param': ['password'],
        })
        # 登录
        queryParams = {
            'username': encodeData['username'],
            'password': encodeData['password'],
        }
        # 继续处理登录逻辑...
        print(queryParams)
    except Exception as error:
        # 处理错误...
        pass

def decryption(encrypted_data, key):
    """AES解密"""
    try:
        key = key.encode('utf-8')
        iv = key
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = base64.b64decode(encrypted_data)
        decrypted_data = cipher.decrypt(encrypted_data)
        decrypted_data = unpad(decrypted_data, AES.block_size)
        print(decrypted_data)
        return decrypted_data.decode('utf-8')
    except Exception as error:
        # 处理解密错误...
        print(error)

def decode_base64_password(encoded_password):
    """base64.b64decode将 Base64 编码的数据解码回原始的二进制数据。接受一个 Base64 字符串作为输入，并返回解码后的原始二进制数据。"""
    decoded_password = base64.b64decode(encoded_password.encode('utf-8')).decode('utf-8')
    return decoded_password

def hash_password(password):
    """对密码进行bcrypt加密"""
    # 生成随机盐值
    salt = bcrypt.gensalt()
    # 使用盐值对密码进行哈希加密
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    print(hashed_password.decode('utf-8'))
    return hashed_password

def verify_password(plain_password, hashed_password):
    """对比原密码和数据库存的hash密码是否匹配"""
    is_matched = bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    if is_matched:
        print('matched')
    else:
        print('not matched')

# 从数据库中获取存储的leo和admin的bcrypt加密密码
hashed_password_from_database = ["$2a$10$D8I0RDeL2oyupJlNB3qArOYoGwtfo20A3CLCxMSCMn3CqeAJmy96m",
"$2a$10$21p3WzAEF4d0seY9iTLzPeb6.7AJy9xren8hPXHXtUXIQ0fkMxOYO"]

# 假设从前端接收到的加密数据为：
LoginParams = {
    'username': 'leo',
    'password': '123456',
    'autoLogin': False,
    'type': 'account'
}
user={
  'data': {'username': 'admin', 'password': '123456'},
  'type': '',
  'key': 'king,house,cloud',
  'param': ['password'],
}
# 解密密码
key = 'king,house,cloud'
# decrypted_password = decodeData['password']
encrypted_data = 'gukhm0l9dmNWrDcflceoQ/lzVaE6owHsd3EuWpOURpqwjJwECwjiFr7Pnat0TUEzxGtLyp/Cfe3o1SvAWFKMpRXUKTPX1DeKVJijQVI39Eo04Cfd4vPLUz/tRsIuL9SHSR2JyBlLxWKJOTrVklBf454X6M7XSg9pwkXpw0OlywA='
# encryption(user)
# decryption(encrypted_data, key)
# decrypt(encrypt('123456'))
# handleSubmit(LoginParams)
hash_password('123456')
verify_password('123456', hashed_password_from_database[0])