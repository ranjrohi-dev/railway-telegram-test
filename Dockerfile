FROM python:3.12-slim
WORKDIR /app
RUN python -m pip install --no-cache-dir Telethon==1.45.0
COPY telegram_test.py .
CMD ["python", "-u", "telegram_test.py"]
