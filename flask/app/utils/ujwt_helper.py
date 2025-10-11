import jwt
import os
from datetime import datetime, timedelta

SECRET_KEY = os.getenv("SECRET_KEY")
JWT_EXP_MINUTES = int(os.getenv("JWT_EXP_MINUTES", 30))

def create_token(payload):
    """Generate JWT token"""
    payload_copy = payload.copy()
    payload_copy["exp"] = datetime.utcnow() + timedelta(minutes=JWT_EXP_MINUTES)
    token = jwt.encode(payload_copy, SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token):
    """Verify and decode JWT token"""
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
    except Exception as e:
        return {"error": str(e)}
