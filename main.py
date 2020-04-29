"""Fichier chargée de lancer le programme et gérer le port série et l'interface

On utilise le fichier donnees.py pour les données du programme, le fichier
interface pour gérer la partie graphique et le fichier liaison serie pour
la liaison série"""

import time
import serial

from tkinter import *
from threading import Thread, RLock
from interface import *
from data import *
from serial_link import *
from network import  *

# define match class
match=SportDisplay()

# Thread declaration
thread_serialport = ReadSerialPort(match)
thread_interface = DisplayInterface(match)
thread_udp = UdpCommunication(match)

# Thread Start
thread_serialport.start()
thread_udp.start()
thread_interface.mainloop()

#thread_serialport.join()

# Thread Stop
del thread_serialport 
del thread_udp

