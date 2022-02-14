FROM python:3.10-alpine

COPY credentials /root/.aws/credentials

WORKDIR /code

ENV FLASK_APP server.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN pip3 install --upgrade pip

RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk add zlib-dev jpeg-dev gcc musl-dev

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["flask", "run" ]