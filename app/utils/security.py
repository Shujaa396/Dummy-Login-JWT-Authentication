import os, datetime as dt
from jose import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
JWT_SECRET = os.getenv("JWT_SECRET", "devsecret")
JWT_ALG = os.getenv("JWT_ALG", "HS256")
JWT_EXPIRE_MIN = int(os.getenv("JWT_EXPIRE_MINUTES", "120"))

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_access_token(subject: str | int) -> str:
    expire = dt.datetime.utcnow() + dt.timedelta(minutes=JWT_EXPIRE_MIN)
    payload = {"sub": str(subject), "exp": expire}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)
