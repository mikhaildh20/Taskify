from app.models.ftsk_users_model import Users
from app import db
from app.utils import create_token, verify_password, DtoResponse, hash_password, decode_token
from datetime import datetime

def login_user(data):
    username = data.get("username")
    password = data.get("password")

    # validate mandatory input
    if not username or not password:
        return DtoResponse(False, "Username or password must be filled!", None, 400)
    
    # search logged user
    user = Users.query.filter_by(username=username).first()

    # validate user existence
    if not user:
        return DtoResponse(False, "User not found!", None, 404)
    
    # validate password
    if not verify_password(password, user.password_hash):
        return DtoResponse(False, "Wrong password", None, 401)
    
    # generate JWT token
    token = create_token({
        "user_id": user.id, 
        "username": user.username,
        "iat": datetime.utcnow().timestamp()
    })
    
    return DtoResponse(
        True, 
        "Logged in successfully.", 
        {
            "token": token, 
            "user": user.to_dict()
        },
        200
    )

def register_user(data):
    username = data.get("username")
    email = data.get("email")
    password = date.get("password")
    
    # validate mandatory input
    if not username or not email or not password:
        return DtoResponse(False, "All fields must be filled!", None, 400)
    
    # validate duplicate
    if Users.query.filter_by(username=username).first():
        return DtoResponse(False, "Username already taken!", None, 409)
    
    if Users.query.filter_by(email=email).first():
        return DtoResponse(False, "Email already taken!", None, 409)
    
    # hash user password
    hashed_pw = hash_password(password)
    
    # create new user
    new_user = Users(
        username=username,
        email=email,
        password_hash=hashed_pw,
        created_at=datetime.utcnow()
    )
    
    # insert into database
    db.session.add(new_user)
    db.session.commit()
    
    # response into front end
    return DtoResponse(
        True,
        "User registered successfully.",
        new_user.to_dict(),
        201
    )
    
def get_profile(token):
    """Get user profile from jwt token"""

    # decode token
    decoded = decode_token(token)
    if "error" in decoded:
        return DtoResponse(False, decoded["error"], None, 401)
    
    user_id = decoded.get("user_id")
    if not user_id:
        return DtoResponse(False, "Invalid token payload", None, 401)
    
    # search user in database
    user = Users.query.get(user_id)
    if not user:
        return DtoResponse(False, "User not found", None, 404)
    
    return DtoResponse(True, "Profile reviewed successfully.", user.to_dict(), 200)

def update_profile(token, data):
    """Update user profile data"""

    decoded = decode_token(token)
    if "error" in decoded:
        return DtoResponse(False, decoded["error"], None, 401)

    user_id = decoded.get("user_id")
    user = Users.query.get(user_id)

    if not user:
        return DtoResponse(False, "User not found", None, 404)
    
    # get inputs
    password = data.get("password")
    user.password_hash = hash_password(password)
    
    db.session.commit()

    return DtoResponse(True, "Profile updated successfully", user.to_dict(), 200)