import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os 
import sys
import platform
import psutil

svmem = psutil.virtual_memory()
total_ram = round(svmem.total / (1024 ** 3), 2)

load_dotenv()
HOME_DIR = os.path.dirname(os.path.abspath(__file__))
app = FastAPI(title="LABOX SERVICE", description="LABOX SERVICE", version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "LABOX SERVICE is running!"}

@app.get('/device')
async def getDeviceInfo():
    return {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Total Memory": total_ram,
    }


class Main():
    def __init__(self, profile:dict):
        self.profile = profile
        self.run()

    def run(self):
        uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
    
if __name__ == "__main__":
    main = Main({"key":"value"})

