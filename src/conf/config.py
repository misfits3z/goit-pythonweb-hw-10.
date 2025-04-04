class Config:

    DB_URL = "postgresql+asyncpg://postgres:goit@localhost:5432/contacts"

    JWT_SECRET = "your_secret_key"  # Секретний ключ для токенів
    JWT_ALGORITHM = "HS256"  # Алгоритм шифрування токенів
    JWT_EXPIRATION_SECONDS = 3600  # Час дії токена (1 година)


config = Config
