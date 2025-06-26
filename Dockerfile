FROM python:3.11-alpine3.21
WORKDIR /code
RUN adduser heart -D --home /code -s /bin/sh
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
USER heart
CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]