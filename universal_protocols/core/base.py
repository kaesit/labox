import os, sys
from psutil import virtual_memory
from dotenv import load_dotenv


load_dotenv()

PROTOCOLS = [protocol for protocol in os.getenv("PROTOCOLS").split(",")]
MEMORY = virtual_memory

# @Incomplete Structure of Protocols
class ProtocolModel():
    global is_protocols_loaded = False
    def __init__(self, protocols, memory):
        self.protocols = PROTOCOLS
        self.memory = MEMORY
    # @Incomplete @Important Memory allocation is so important and it must not be forgotten 
    def VirtualMemoryAllocation(self):
        pass
    # This function returns protocols value
    def GetProtocolsList(self):
        return self.protocols
    def IsProtocolsLoaded(self):
        return is_protocols_loaded
    
    # @Incomplete
    # @F-Test
    # @Scenario: This function will mandate all protocols for all devices and it will be valid for all universal_drivers
    def MandatorationOfProtocols(self, protocol_list: dict) -> None:
        protocol_list.mandate()
        is_protocols_loaded = True


