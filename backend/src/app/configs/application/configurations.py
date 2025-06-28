from dotenv import load_dotenv
import os

load_dotenv()

class Configs:
    def __init__(self):
        self.secret_key = os.getenv("SECRET_KEY")

configs = Configs()