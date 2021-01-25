'''
Script to interact with UE using AT CMDs
'''


import serial
#from serial import SerialException
import time
ser1 = serial.Serial()
ser2 = serial.Serial()
ser3 = serial.Serial()
print(ser)
print("\n")

try:
    ser1.baudrate = 19200
    ser1.port = 'COM6'
    ser1.open()
    
except serial.SerialException as err:
    print("Error:{}".format(err))


try:
    ser2.baudrate = 19200
    ser2.port = 'COM6'
    ser2.open()
    
except serial.SerialException as err:
    print("Error:{}".format(err))

try:
    ser3.baudrate = 19200
    ser3.port = 'COM6'
    ser3.open()
    
except serial.SerialException as err:
    print("Error:{}".format(err))



def detach():
    #Detach
    time.sleep(2)
    ser1.write("at+cgatt=0\r".encode()) # imp:\r is for return carriage.#works
    ser1.flush()
    time.sleep(10)
    print(ser1.is_open)
    #ser.read()
    print(ser1.read(ser.inWaiting()))
    #print(ser.read(10))
    #ser.close()


    time.sleep(2)
    ser2.write("at+cgatt=0\r".encode()) # imp:\r is for return carriage.#works
    ser2.flush()
    time.sleep(10)
    print(ser2.is_open)
    #ser.read()
    print(ser2.read(ser.inWaiting()))
    #print(ser.read(10))
    #ser.close()

    time.sleep(2)
    ser3.write("at+cgatt=0\r".encode()) # imp:\r is for return carriage.#works
    ser3.flush()
    time.sleep(10)
    print(ser3.is_open)
    #ser.read()
    print(ser3.read(ser.inWaiting()))
    #print(ser.read(10))
    #ser.close()



def attach():

    # Attach
    ser1.write("at+cgatt=1\r".encode()) # imp:\r is for return carriage.#works
    ser1.flush()
    time.sleep(5)
    print(ser1.is_open)
    #ser.read()
    print(ser1.read(ser1.inWaiting()))
    #print(ser.read(10))
    #ser.close()


    ser2.write("at+cgatt=1\r".encode()) # imp:\r is for return carriage.#works
    #ser.write("at+cgdcont=1,1\r".encode()) # imp:\r is for return carriage.
    ser2.flush()
    time.sleep(5)
    print(ser2.is_open)
    #ser.read()
    print(ser2.read(ser2.inWaiting()))
    #print(ser.read(10))
    #ser.close()

    ser3.write("at+cgatt=1\r".encode()) # imp:\r is for return carriage.#works
    ser3.flush()
    time.sleep(5)
    print(ser3.is_open)
    #ser.read()
    print(ser3.read(ser3.inWaiting()))
    #print(ser.read(10))
    #ser.close()



while True:
    
    user_input = input("Attach-->1, Detach-->2")
    if user_input == '1':
        attach()

    elif user_input == '2':
        detach()


