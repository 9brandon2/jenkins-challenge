FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP /code/build.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY . /code
EXPOSE 5000
CMD ["flask", "run"]