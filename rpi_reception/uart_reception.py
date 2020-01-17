'''
UART communication on Raspberry Pi using Pyhton
'''
import serial
from time import sleep

ser = serial.Serial ("/dev/ttyS0", 115200)    #Open port with baud rate
data = ""
while True:
    while True:
        ser.read_until("TR")
        break
    data = ser.read_until("ZZ")
    data = data[2:2]
