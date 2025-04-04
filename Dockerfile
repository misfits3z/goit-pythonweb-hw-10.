# Базовий образ для Python 3.12
FROM python:3.12-slim

# Встановлюємо Poetry
RUN pip install --no-cache-dir poetry

# Створюємо директорію для застосунку
WORKDIR /app

# Копіюємо файли проєкту
COPY pyproject.toml poetry.lock ./

# Встановлюємо залежності
RUN poetry install --no-root --no-dev

# Копіюємо код проєкту
COPY . .

# Вказуємо команду для запуску
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]