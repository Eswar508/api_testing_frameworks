From python:3.12-slim
workdir /app
copy requirements.txt .
run pip install --no-cache-dir -r requirements.txt
copy . .
ENV PYTHONPATH=/app
cmd ["python","-m","flask_api.app"]