FROM python:3
USER root
WORKDIR /stpaul
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD "gunicorn core.wsgi --log-file=-"