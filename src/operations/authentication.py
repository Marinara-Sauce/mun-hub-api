import bcrypt
from fastapi import Depends, HTTPException
import jwt
import datetime

SECRET_KEY = 'example-key'


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


def generate_token(user_id: int, expiration_minutes=30):  # TODO: Make this configurable
    """
    Generates a JWT token for user authentication.

    :param user_id: The user's unique identifier.
    :param expiration_minutes: Token expiration time in minutes (default is 30 minutes).
    :return: A JWT token as a string.
    """
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def verify_token(token: str):
    """
    Verifies a JWT token and returns the user_id if valid.

    :param token: The JWT token to be verified.
    :return: The user_id if the token is valid, None otherwise.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.DecodeError:
        # Token is invalid
        return None

if __name__ == "__main__":
    user_id = 123
    plaintext_password = "password"
    
    # Hash the password
    hashed_password = hash_password(plaintext_password)

    print(hashed_password)
    
    # Generate a token
    token = generate_token(user_id)
    print("JWT Token:", token)
    
    # Verify a token
    user_id_from_token = verify_token(token)
    if user_id_from_token:
        print(f"Token is valid. User ID: {user_id_from_token}")
    else:
        print("Token is invalid.")