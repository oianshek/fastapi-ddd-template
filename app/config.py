from pydantic_settings import BaseSettings


class Config(BaseSettings):
    PROJECT_NAME: str = ""
    PROJECT_DESCRIPTION: str = ""
    PROJECT_VERSION: str = ""

    DATABASE_PORT: int = 0
    POSTGRES_PASSWORD: str = ""
    POSTGRES_USER: str = ""
    POSTGRES_DB: str = ""
    POSTGRES_HOST: str = ""

    JWT_SECRET_KEY: str = ""
    JWT_ENCODE_ALGORITHM: str = ""
    REFRESH_TOKEN_EXPIRES_IN: int = 0
    ACCESS_TOKEN_EXPIRES_IN: int = 0

    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_SECRET_KEY: str = ""
    GOOGLE_REDIRECT_URI: str = ""
    GOOGLE_TOKEN_URL: str = ""

    @property
    def db_url(self):
        return (f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_HOST}:{self.DATABASE_PORT}/{self.POSTGRES_DB}")

    @property
    def google_redirect_url(self):
        return (f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={self.GOOGLE_CLIENT_ID}"
                f"&redirect_uri={self.GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline")


settings = Config()
