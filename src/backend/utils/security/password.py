from hashlib import md5


def protect(password: str) -> str:
    return md5(password.encode()).hexdigest()


def verify(password: str, protected: str) -> bool:
    return protect(password) == protected
