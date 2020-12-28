FROM python:2

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
RUN python ./setup.py build && python ./setup.py install

CMD [ "python", "./fut/cli.py" ]