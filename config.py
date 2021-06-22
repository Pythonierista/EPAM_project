import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b"\x9a\xc0\xe1\x0f\xcb\xd2\xd1\x00\x94\x90N\x1dj3'\xf3"

    MONGODB_SETTINGS = {'db': 'UTA_Enrollment'}
