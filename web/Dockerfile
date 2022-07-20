FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# Run this command for the development server ans set DEBUG=0
# CMD python run.py
# Run this for create fake data
#CMD flask add_items && gunicorn --bind 0.0.0.0:6060 -w 3 run:app
CMD gunicorn --bind 0.0.0.0:6060 -w 3 run:app
