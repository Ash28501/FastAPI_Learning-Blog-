from datetime import datetime, timedelta
from typing import Optional
from jose import jwt,JWTError
from . import schemas

SECRET_KEY = "9f3c8e2a7d6b4c1f8a9d0e3b5c7f2a1e6d8c9b0f3a2e4d5c6b7a8f9e0d1c2b3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_token(token : str, credential_execption ):
    try:
        payload =jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email : str = payload.get("sub")
        if email is None:
            raise credential_execption
        token_data = schemas.TokenData(email=email)
    
    except JWTError:
        raise credential_execption