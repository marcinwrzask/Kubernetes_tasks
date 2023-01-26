FROM python:3
COPY . /app1
WORKDIR /app1

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["api1.py" ]