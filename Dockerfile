FROM python:3
WORKDIR /stpaul
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python3 manage.py runserver"]