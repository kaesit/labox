import os, sys
from psutil import virtual_memory
from dotenv import load_dotenv

load_dotenv()

PROTOCOLS = [protocol for protocol in os.getenv("PROTOCOLS").split(",")]