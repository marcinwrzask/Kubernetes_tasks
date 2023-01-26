FROM python:3
COPY . /app2
WORKDIR /app2

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["api2.py" ]