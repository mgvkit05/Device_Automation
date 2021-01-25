'''
Script to interact with UE using AT CMDs
'''

#pip install pyserial
#https://pythonhosted.org/pyserial/

import serial
#from serial import SerialException
import time, sys
ser = serial.Serial()
print(ser)
print("\n")

try:
    ser.baudrate = 19200
    ser.port = 'COM74'
    ser.open()
    
except serial.SerialException as err:
    print("Error:{}".format(err))

while True:
    option = input("Attach: 1, Detach: 2 --> ")

    if option == '1':
        # Attach
        ser.write("at+cfun=1\r".encode()) # imp:\r is for return carriage.#works
        #ser.write("at+cgdcont=1,1\r".encode()) # imp:\r is for return carriage.
        ser.flush()
        time.sleep(1)
        print(ser.is_open)
        #ser.read()
        print(ser.read(ser.inWaiting()))
        #print(ser.read(10))
        #ser.close()

    elif option == '2':
        #Detach
        #time.sleep(10)
        ser.write("at+cfun=0\r".encode()) # imp:\r is for return carriage.#works
        #ser.write("at+cgdcont=1,1\r".encode()) # imp:\r is for return carriage.
        ser.flush()
        time.sleep(1)
        print(ser.is_open)
        #ser.read()
        print(ser.read(ser.inWaiting()))
        #print(ser.read(10))
        #ser.close()

    else:
        print("Invalid input")
        sys.exit()
# OUTPUT


#RESTART: C:\Users\m.gulam\Desktop\pyRevolution\SEA\tera_term\tera_term.py =
#Serial<id=0x4d81830, open=False>(port=None, baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)


#True
#b'at+cgatt=0\r\r\nOK\r\n'
 
#= RESTART: C:\Users\m.gulam\Desktop\pyRevolution\SEA\tera_term\tera_term.py =
#Serial<id=0x4c71830, open=False>(port=None, baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)


#True
#b'at+cgatt=1\r\r\n+CME ERROR: no network service\r\n=


