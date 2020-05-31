import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xf4\x9f\xfd\xce\x7fo/l\x1ci{\x94\x9d\xb3\xe8_'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment',
                    'host': 'mongodb+srv://test:test@cluster0-13gle.gcp.mongodb.net/UTA_Enrollment?retryWrites=true&w=majority' }
