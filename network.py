"""File managing network port.

Using SportDisplay objet and data from data.py"""

import socket
import time
import pickle

from threading import Thread
from data import *


class UdpCommunication(Thread): 
    """Thread managing udp commmunication"""
         
    def __init__(self,SportDisplay): 
        """ Constructor initialize udp communication """       
        Thread.__init__(self)
        self.udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_server_socket.bind((hote, port))
        self.data_udp=data_udp
        self.match=SportDisplay
        
    def run(self):
        print("Enter network read thread")
        while(True):
            self.data_udp = self.udp_server_socket.recvfrom(1024)
            self.data_udp = pickle.loads(self.data_udp[0])
            self.match.udp_data_decode(self.data_udp)
            time.sleep(1)            
        
    def __del__(self):
        """ Destructor close udp communication """
        self.udp_server_socket.close()       