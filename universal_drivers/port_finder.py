import sys, os
import serial.tools.list_ports
import mcu.esp32.core.base import ESP32Model

def find_ports():
    ports = serial.tools.list_ports.comports()
    usb_ports = [port.device for port in ports]

    return usb_ports

