FROM python:3

RUN apk-install python3 python3-dev python3-pip build-essential libgmp-dev libmpfr-dev libmpc-dev

RUN pip3 install gmpy2

COPY src/requirements.txt .
RUN apk --update add --virtual build-dependencies py-pip \
  && pip install -r requirements.txt \
  && apk del build-dependencies

COPY src /code
WORKDIR /code

EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
