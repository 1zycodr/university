import hashlib
import os


def hash(password: str) -> tuple[bytes, bytes]:
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        250000,
    )

    return salt, key


def verify(salt: bytes, key: bytes, password: str) -> bool:
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        250000,
    )

    return key == new_key


if __name__ == '__main__':
    print('you should not run this module directly')
