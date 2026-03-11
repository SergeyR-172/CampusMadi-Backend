import bcrypt, secrets, jwt, hashlib
from core.settings import settings
from datetime import timedelta, datetime, timezone

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    pwdbytes = password.encode("utf-8")
    hashed = bcrypt.hashpw(pwdbytes, salt)
    return hashed.decode("utf-8")

def validate_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


def create_refresh_token() -> tuple[str, str]:
    token = secrets.token_urlsafe(64)
    token_hash = hashlib.sha256(token.encode()).hexdigest()
    return token, token_hash

def create_access_token(payload: dict, expire_minutes: int = settings.access_token_expire_minutes) -> str:
    to_encode = payload.copy()
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=expire_minutes)
    to_encode.update({"exp": expire, "iat": now})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

def decode_jwt(token: str | bytes):
    decoded = jwt.decode(
        token,
        settings.secret_key,
        algorithms=[settings.algorithm],
    )
    return decoded