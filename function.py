from data import *
import datetime
import threading
import socket
import sys
from threading import Thread


class SportDisplay:
    """Function managing decoding receive from serial link and use in display"""
        
    def __init__(self):        
        # Match Parameters
        self.time_match=datetime.time()
        self.name_team1="LOCAL"
        self.name_team2="VISITOR"
        self.score_team1=0
        self.score_team2=0
        self.period=0
        self.jail_team1=0
        self.jail_team2=0
        self.chrono_on_off=0
        self.jail1_team1=0
        self.jail2_team1=0
        self.jail3_team1=0
        self.jail1_team2=0
        self.jail2_team2=0
        self.jail3_team2=0   
        self.lock = threading.Lock()

    def udp_data_decode(self,liste_data):    
        self.lock.acquire()
        try:
            # Decod chrono on off
            if liste_data[2] == "ON":
                self.chrono_on_off=1
            else:    
                self.chrono_on_off=0
            # Decod name team1 and 2    
            self.name_team1=liste_data[0]
            self.name_team2=liste_data[1]
            
        finally:
            self.lock.release()
            
    def serial_data_decode(self,liste_data):
        self.lock.acquire()
        try:
            # Detect Byte Synchro Frame
            if ((liste_data[0]==frame["B1_SYNCHRO"][1])and
                (liste_data[1]==frame["B2_SYNCHRO"][1])and
                (liste_data[2]==frame["B3_SYNCHRO"][1])and
                (liste_data[3]==frame["B4_SYNCHRO"][1])):
                print("Synchro Byte receive")
                # Detect Byte End Frame
                if (liste_data[55]==frame["B56_END"][1]):
                    print("End Byte receive")
                    # Frame format correct : decode informations
                    
                    # Decod Match Time
                    # Match Time : Minute Ten
                    if(liste_data[6]>=48 and liste_data[6]<=57):
                        min_ten=int(float(chr(liste_data[6])))
                    else:
                        min_ten=0   
                    # Match Time : Minute Unit                 
                    if(liste_data[7]>=48 and liste_data[7]<=57):
                        min_unit=int(float(chr(liste_data[7])))
                    else:
                        min_unit=0                
                    match_minute=min_ten*10+min_unit 
                    # Match Time : Second Ten
                    if(liste_data[8]>=48 and liste_data[8]<=57):
                        sec_ten=int(float(chr(liste_data[8])))
                    else:
                        sec_ten=0   
                    # Match Time : Second Unit                 
                    if(liste_data[9]>=48 and liste_data[9]<=57):
                        sec_unit=int(float(chr(liste_data[9])))
                    else:
                        sec_unit=0                
                    match_second=sec_ten*10+sec_unit                             
                    self.time_match=datetime.time(hour=0,minute=match_minute,second=match_second)
                    if DEBUG: print("Time:",self.time_match)   
                    
                    # Decod Score Team 1
                    if(liste_data[10]>=48 and liste_data[10]<=57):
                        score_team1_hundred=int(float(chr(liste_data[10])))
                    else:
                        score_team1_hundred=0  
                    if(liste_data[11]>=48 and liste_data[11]<=57):
                        score_team1_ten=int(float(chr(liste_data[11])))
                    else:
                        score_team1_ten=0 
                    if(liste_data[12]>=48 and liste_data[12]<=57):
                        score_team1_unit=int(float(chr(liste_data[12])))
                    else:
                        score_team1_unit=0    
                    self.score_team1=score_team1_hundred*100+score_team1_ten*10+score_team1_unit
                    if DEBUG: print("Score Team 1:",self.score_team1)   
                     
                    # Decod Score Team 2
                    if(liste_data[13]>=48 and liste_data[13]<=57):
                        score_team2_hundred=int(float(chr(liste_data[13])))
                    else:
                        score_team2_hundred=0  
                    if(liste_data[14]>=48 and liste_data[14]<=57):
                        score_team2_ten=int(float(chr(liste_data[14])))
                    else:
                        score_team2_ten=0 
                    if(liste_data[15]>=48 and liste_data[15]<=57):
                        score_team2_unit=int(float(chr(liste_data[15])))
                    else:
                        score_team2_unit=0    
                    self.score_team2=score_team2_hundred*100+score_team2_ten*10+score_team2_unit                                   
                    if DEBUG: print("Score Team 2:",self.score_team2) 
                        
                    # Decod period
                    if(liste_data[16]>=48 and liste_data[16]<=57):
                        self.period=int(float(chr(liste_data[16])))
                    else:    
                        self.period=0
                    if DEBUG: print("Period:",self.period)
                                    
                    # Decod jail team1
                    if(liste_data[17]>=48 and liste_data[17]<=57):
                        self.jail_team1=int(float(chr(liste_data[17])))
                    else:    
                        self.jail_team1=0
                    if DEBUG: print("Jail Team 1:",self.jail_team1) 
                    
                    # Decod jail_team2
                    if(liste_data[18]>=48 and liste_data[18]<=57):
                        self.jail_team2=int(float(chr(liste_data[18])))
                    else:    
                        self.jail_team2=0
                    if DEBUG: print("Jail Team 2:",self.jail_team2) 
                              
                    # Decod jail1_team1
                    if(liste_data[24]>=48 and liste_data[24]<=57):
                        jail1_team1_ten=int(float(chr(liste_data[24])))
                    else:
                        jail1_team1_ten=0  
                    if(liste_data[25]>=48 and liste_data[25]<=57):
                        jail1_team1_unit=int(float(chr(liste_data[25])))
                    else:
                        jail1_team1_unit=0 
                    if(liste_data[26]>=48 and liste_data[26]<=57):
                        jail1_team1_tenth=int(float(chr(liste_data[26])))
                    else:
                        jail1_team1_tenth=0    
                    self.jail1_team1=jail1_team1_ten*100+jail1_team1_unit*10+jail1_team1_tenth
                    if DEBUG: print("Jail 1 Team 1:",self.jail1_team1) 
                    
                    # Decod jail2_team1
                    if(liste_data[27]>=48 and liste_data[27]<=57):
                        jail2_team1_ten=int(float(chr(liste_data[27])))
                    else:
                        jail2_team1_ten=0  
                    if(liste_data[28]>=48 and liste_data[28]<=57):
                        jail2_team1_unit=int(float(chr(liste_data[28])))
                    else:
                        jail2_team1_unit=0 
                    if(liste_data[29]>=48 and liste_data[29]<=57):
                        jail2_team1_tenth=int(float(chr(liste_data[29])))
                    else:
                        jail2_team1_tenth=0    
                    self.jail2_team1=jail2_team1_ten*100+jail2_team1_unit*10+jail2_team1_tenth
                    if DEBUG: print("Jail 2 Team 1:",self.jail2_team1) 
                    
                    # Decod jail3_team1
                    if(liste_data[30]>=48 and liste_data[30]<=57):
                        jail3_team1_ten=int(float(chr(liste_data[30])))
                    else:
                        jail3_team1_ten=0  
                    if(liste_data[31]>=48 and liste_data[31]<=57):
                        jail3_team1_unit=int(float(chr(liste_data[31])))
                    else:
                        jail3_team1_unit=0 
                    if(liste_data[32]>=48 and liste_data[32]<=57):
                        jail3_team1_tenth=int(float(chr(liste_data[32])))
                    else:
                        jail3_team1_tenth=0    
                    self.jail3_team1=jail3_team1_ten*100+jail3_team1_unit*10+jail3_team1_tenth
                    if DEBUG: print("Jail 3 Team 1:",self.jail3_team1) 
                    
                    # Decod jail1_team2
                    if(liste_data[37]>=48 and liste_data[37]<=57):
                        jail1_team2_ten=int(float(chr(liste_data[37])))
                    else:
                        jail1_team2_ten=0  
                    if(liste_data[38]>=48 and liste_data[38]<=57):
                        jail1_team2_unit=int(float(chr(liste_data[38])))
                    else:
                        jail1_team2_unit=0 
                    if(liste_data[39]>=48 and liste_data[39]<=57):
                        jail1_team2_tenth=int(float(chr(liste_data[39])))
                    else:
                        jail1_team2_tenth=0    
                    self.jail1_team2=jail1_team2_ten*100+jail1_team2_unit*10+jail1_team2_tenth
                    if DEBUG: print("Jail 1 Team 2:",self.jail1_team2) 
                    
                    # Decod jail2_team2
                    if(liste_data[40]>=48 and liste_data[40]<=57):
                        jail2_team2_ten=int(float(chr(liste_data[40])))
                    else:
                        jail2_team2_ten=0  
                    if(liste_data[41]>=48 and liste_data[41]<=57):
                        jail2_team2_unit=int(float(chr(liste_data[41])))
                    else:
                        jail2_team2_unit=0 
                    if(liste_data[42]>=48 and liste_data[42]<=57):
                        jail2_team2_tenth=int(float(chr(liste_data[42])))
                    else:
                        jail2_team2_tenth=0    
                    self.jail2_team2=jail2_team2_ten*100+jail2_team2_unit*10+jail2_team2_tenth
                    if DEBUG: print("Jail 2 Team 2:",self.jail2_team2) 
                    
                    # Decod jail3_team2
                    if(liste_data[43]>=48 and liste_data[43]<=57):
                        jail3_team2_ten=int(float(chr(liste_data[43])))
                    else:
                        jail3_team2_ten=0  
                    if(liste_data[44]>=48 and liste_data[44]<=57):
                        jail3_team2_unit=int(float(chr(liste_data[44])))
                    else:
                        jail3_team2_unit=0 
                    if(liste_data[45]>=48 and liste_data[45]<=57):
                        jail3_team2_tenth=int(float(chr(liste_data[45])))
                    else:
                        jail3_team2_tenth=0    
                    self.jail3_team2=jail3_team2_ten*100+jail3_team2_unit*10+jail3_team2_tenth
                    if DEBUG: print("Jail 3 Team 2:",self.jail3_team2)         
                else:
                    print("False End Byte")
            else:
                print("Receive {0} - {1} - {2} - {3}".format(liste_data[0],liste_data[1],liste_data[2],liste_data[3]))
                print("Expect {0} - {1} - {2} - {3}".format(frame["B1_SYNCHRO"][1],frame["B2_SYNCHRO"][1],frame["B3_SYNCHRO"][1],frame["B4_SYNCHRO"][1])) 
                print("False Synchro Byte")
    
        finally:
            self.lock.release()