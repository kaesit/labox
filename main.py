import uvicorn
from dotenv import load_dotenv
import os 
import sys


load_dotenv()

HOME_DIR = os.path.dirname(os.path.abspath(__file__))

class Main():
    def __init__(self, profile:dict):
        self.profile = profile
        self.run()

    def run(self):
        pass

    
if __name__ == "__main__":
    main = Main({"key":"value"})


