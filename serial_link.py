"""File managing serial port.

Using SportDisplay objet and data from data.py"""

import time
import serial
import sys

from threading import Thread
from data import *
from function import * 
   
            

class ReadSerialPort(Thread):
    """ Class managing reading the serial port"""

    def __init__(self,SportDisplay):
        """ Constructor initialize serial port """
        Thread.__init__(self)
        self.match=SportDisplay
        self.ser = serial.Serial(
            port=port_serie_nom,
            baudrate=port_serie_baudrate,
            bytesize=port_serie_bytesize,
            parity=port_serie_parity,
            stopbits=port_serie_stopbits
        )
        if self.ser.isOpen() == True:
            print("Port {0} open".format(port_serie_nom))
        else:
            print('Port not open please check configuration: \n'
                  'Port:{0}\nBaudrate:{1}\nParity:{2}\nStop Bits:{3}\nByte Size:{4}'
                  .format(port_serie_nom,port_serie_baudrate,port_serie_parity,port_serie_stopbits,port_serie_bytesize))
           
    def run(self):
        """ Thread managing serial port reading """    
        print("Enter serial read thread")
        liste_data=[]
        while True:
            liste_data=self.ser.read(size_frame)
          
            self.match.serial_data_decode(liste_data)
            #print(self.match.time_match)
            #print("thread")
            #self.match.period+=1
            #print("match period write:",self.match.period)
            time.sleep(5)

    def __del__(self):
        """ Destructor close com port """

        if self.ser.isOpen() == True:
            print("Close port {0}".format(port_serie_nom))
            self.ser.close()
        else:
            print("Impossible to close port, {0} not open".format(port_serie_nom))
