import jwt
from utils.config import Config

def generate_token(user_data):
    token_data = f"{user_data['person_id']}-{user_data['first_name']}-{user_data['last_name']}"
    token = jwt.encode({"data": token_data}, Config.SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token):
    try:
        decoded = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
