import os, sys
from psutil import virtual_memory
from dotenv import load_dotenv

load_dotenv()

PROTOCOLS = [protocol for protocol in os.getenv("PROTOCOLS").split(",")]
MEMORY = virtual_memory

class Protocols():
    def __init__(self, protocols, memory):
        self.protocols = PROTOCOLS
        self.memory = MEMORY
    # @Incomplete @Important Memory allocation is so important and it must not be forgotten 
    def VirtualMemoryAllocation(self):
        pass
    # This function returns protocols value
    def GetProtocolsList(self):
        return self.protocols

