FROM python:3.8.8-alpine


RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# COPY . /app
COPY . .

WORKDIR /

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]