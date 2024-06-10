import os
from utils.network import NetworkUtils
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '!mF8u88y7Q1w_20a3Z4x5c6V7b8n9m0')
    DB_HOST = os.getenv('DB_HOST', NetworkUtils.get_ipv4_address())
    DB_NAME = os.getenv('DB_NAME', 'loe')
    DB_USER = os.getenv('DB_USER', 'test_dev')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'test')

    @staticmethod
    def init_app(app):
        pass
