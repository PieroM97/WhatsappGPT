FROM python:3.10

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 5000

COPY . /opt/app

EXPOSE 5000

CMD python main.py
