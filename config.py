import os

# os.environ['DATABASE_URL'] = 'postgresql://fjswgwwchhlcup:f84b3ae8fddbb71a91f1096a0d9fa2ceec18df558921ae11278859ed1e1ad259@ec2-54-195-76-73.eu-west-1.compute.amazonaws.com:5432/devi63vo00sj89'
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # SQLALCHEMY_DATABASE_URI = 'postgresql://fjswgwwchhlcup:f84b3ae8fddbb71a91f1096a0d9fa2ceec18df558921ae11278859ed1e1ad259@ec2-54-195-76-73.eu-west-1.compute.amazonaws.com:5432/devi63vo00sj89'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace('postgres', 'postgresql')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

