import jwt, datetime

from app.configs.application.configurations import configs

class JWT:
    @staticmethod
    def generate_token(user_id: str, role: str) -> str:
        """
        Generates a JWT token.
        """
        payload = {
            "user_id": user_id,
            "role": role,
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        return jwt.encode(payload, configs.secret_key, algorithm="HS256")