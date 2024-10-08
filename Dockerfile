FROM python:3.13-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "flask", "run"]

