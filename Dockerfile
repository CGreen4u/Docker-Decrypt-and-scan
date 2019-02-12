FROM python:3

ADD python-main-function.py /

RUN pip install pystrich

CMD [ "python", "./python-main-function.py" ]