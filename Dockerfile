FROM python:3.14-slim
WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .



ENV HOST=0.0.0.0 \
    PORT=7072 \
    WEB1=https://google.com \
    WEB2=https://bing.com \
    RU1=https://ya.ru \
    RU2=https://vk.ru \
    ROUTER=192.168.50.1


EXPOSE 7072

CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7072"]
