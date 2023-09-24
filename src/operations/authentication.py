from typing import Annotated
import bcrypt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
import datetime

SECRET_KEY = 'example-key'
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def hash_password(password: str, salt_rounds=12):
    """
    Hashes a password securely using bcrypt.

    :param password: The plaintext password to be hashed.
    :param salt_rounds: The number of salt rounds to use (default is 12).
    :return: The hashed password as a byte string.
    """
    # Generate a salt and hash the password
    salt = bcrypt.gensalt(salt_rounds)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    return hashed_password.decode('utf-8')


def verify_password(in_password: str, hashed_password: str):
    """
    Verifies a password against its hashed version.

    :param input_password: The plaintext password to be verified.
    :param hashed_password: The previously hashed password to compare against.
    :return: True if the input password matches the hashed password, False otherwise.
    """
    return bcrypt.checkpw(in_password.encode('utf-8'), hashed_password.encode('utf-8'))


def generate_token(username: str, expiration_minutes=30):  # TODO: Make this configurable
    """
    Generates a JWT token for user authentication.

    :param username: The user's unique username.
    :param expiration_minutes: Token expiration time in minutes (default is 30 minutes).
    :return: A JWT token as a string.
    """
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_token(token: str):
    """
    Verifies a JWT token and returns the user_id if valid.

    :param token: The JWT token to be verified.
    :return: The user_id if the token is valid, None otherwise.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload['username']
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.DecodeError:
        # Token is invalid
        return None
    

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = verify_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
    
