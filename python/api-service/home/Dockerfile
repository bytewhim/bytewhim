FROM python:alpine3.19

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

ENV FLASK_APP=/code/app/main.py

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080", "--debug"]