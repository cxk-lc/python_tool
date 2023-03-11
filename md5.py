import hashlib

def md5(data_string: str):
    salt = '123456'
    md5_encryption = hashlib.md5(salt.encode('utf-8'))
    md5_encryption.update(data_string.encode('utf-8'))
    return md5_encryption.hexdigest()
