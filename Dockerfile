FROM python:3.11-slim

WORKDIR /app

COPY app.py .
COPY bg.png .
COPY NotoSansJP-Regular.ttf .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ポートを指定
ENV PORT=8080

# コンテナ起動時のコマンド
CMD ["python", "app.py"]
