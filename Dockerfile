# ベースイメージを指定
FROM python:3.9-slim-buster

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    git \
    && rm -rf /var/lib/apt/lists/*

# ワーキングディレクトリを設定
WORKDIR /app

# Pythonの依存パッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションをコピー
COPY . .

# ポートを公開
EXPOSE 5000

# アプリケーションを起動
CMD ["flask", "run", "--host=0.0.0.0"]