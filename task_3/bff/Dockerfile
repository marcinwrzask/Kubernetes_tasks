FROM python:3
COPY . /bff
WORKDIR /bff

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["bff.py" ]