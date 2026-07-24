import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os 
import sys
import platform
import psutil
import universal_drivers.port_finder as port_finder

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
# @Incomplete
# @Scenario
# What if user just wants to calibrate a barometer instead installing labox firmware to their mcu or board etc..., what should be the getDeviceInfo function then??????? 
@app.get('/device')
async def getDeviceInfo():
    return {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Total Memory": total_ram,
        "Ports": port_finder.find_ports()
    }

"""
@Doubt
@Requirements: Is it enough or are there things that need to be critical for profile structure??? nothing comes mind Sad. Sad.
@Structure
How sould be the profile structure??
role : str : which determines relevancy to field, so it becomes a checkpoint how can we manage to help making user experience better.
interest : str : This is the field of interest of the user, it helps to navigate the user to right resources to install or use right firmware or software for their project device.
device_info : dict : will be fetched by getDeviceInfo() function, which will determine the limitations of what can user install or use on their device.
AI/ML : boolean : Thiss will determine if user may intend to build/use AI/ML based tool/devices or not.
CLI : boolean : We'll learn about if the user wants a CLI feature or not.
GUI : boolean : We'll learn about if the user wants a GUI feature or not.
Simulation: Determines the which simulation test user wants on their device
Scheduler: Determines if user wants scheduler or not
DigitalTwin: Determines if user wants scheduler or not
{
    "role": "bioinformatician",
    "interest": "Array Sequencing",
    "device_info":{},
    "AI/ML": False,
    "CLI": True,
    "GUI": False,
    "Simulation": "Toxicity",
    "Scheduler": True
    "DigitalTwin": False
}
"""

@app.get('/profile')
async def getProfile():
    return {
        "role": "bioinformatician",
        "interest": "Array Sequencing",
        "device_info": await getDeviceInfo(),
        "AI/ML": False,
        "CLI": True,
        "GUI": False,
        "Simulation": "Toxicity",
        "Scheduler": True,
        "DigitalTwin": False
    }

class Main():
    def __init__(self, profile:dict):
        self.profile = profile
        self.run()

    def run(self):
        uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
        
    
if __name__ == "__main__":
    main = Main({"key":"value"})

