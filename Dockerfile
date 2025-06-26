FROM python:3.10.18-bullseye
WORKDIR /code
RUN useradd heart -d /code -s /bin/bash
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
USER heart
CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]
