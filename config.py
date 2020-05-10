import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment',
                    'host': 'mongodb+srv://test:test@cluster0-13gle.gcp.mongodb.net/UTA_Enrollment?retryWrites=true&w=majority' }
    
