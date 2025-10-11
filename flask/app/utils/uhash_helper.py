from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password: str) -> str:
    """Password hash using werzeug (bcrypt by default)."""
    return generate_password_hash(password)

def verify_password(hashed_password: str, plain_password: str) -> bool:
    """Password hash verification"""
    return check_password_hash(hashed_password, plain_password)