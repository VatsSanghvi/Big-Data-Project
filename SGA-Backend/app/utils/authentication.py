from passlib.context import CryptContext

passCrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return passCrypt.hash(password)

def verify_password(actual_password: str, hashed_password: str) -> bool:
    return passCrypt.verify(actual_password, hashed_password)
