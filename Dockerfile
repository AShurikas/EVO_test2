# pull official base image
FROM python:3.9.5-slim-buster

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/
#ENV DATABASE_URL=postgres://fjswgwwchhlcup:f84b3ae8fddbb71a91f1096a0d9fa2ceec18df558921ae11278859ed1e1ad259@ec2-54-195-76-73.eu-west-1.compute.amazonaws.com:5432/devi63vo00sj89
EXPOSE 5000

# run application when image start
CMD ["python", "app.py"]