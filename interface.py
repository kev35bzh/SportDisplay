"""File managing serial port.

Using SportDisplay objet and data from data.py"""

import time
import sys

from threading import Thread
from data import *
from function import * 
from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path, PurePath
import os, sys

 
class DisplayInterface(Tk,SportDisplay):
    """ Class managing reading the serial port"""
 
    def __init__(self,SportDisplay):
        """ Constructor initialize interface """
        self.match=SportDisplay
        self.display = Tk.__init__(self)
        self.title("Sport Display")
         
        # Image background (contain on relative path)         
        dirpath=os.path.abspath('')
        self.display_picture = Image.open(os.path.join(dirpath,'background.jpg'))
        self.display_picture = ImageTk.PhotoImage(self.display_picture)#,height=720)
        
        # Create Canvas
        self.display_canvas = Canvas(self.display,height=display_vertical_resolution,width=display_horizontal_resolution)
        self.display_canvas.delete(ALL)  # clear graphic display
         
        # Display picture
        self.match_picture = self.display_canvas.create_image(display_horizontal_resolution/2, display_vertical_resolution/2, image=self.display_picture)
         
        # Interface: Time and Period 
        # Time
        self.match_time = self.display_canvas.create_text(display_horizontal_resolution/2,display_line2,text=self.match.time_match,font=("Arial", 20))
        # Period
        self.display_canvas.create_text(display_horizontal_resolution/2,display_line3,text="Period",font=("Arial", 10))
        self.display_canvas.create_text(display_horizontal_resolution/2,display_line1,text="Time",font=("Arial", 10))
        self.match_period = self.display_canvas.create_text(display_horizontal_resolution/2,display_line4,text=SportDisplay.period,font=("Arial", 20))
        self.match_part1 = self.display_canvas.create_rectangle(rectangle1_X1,rectangle1_Y1,rectangle1_X2,rectangle1_Y2,outline="black",fill="white")
        if SportDisplay.chrono_on_off==1:
            self.display_canvas.itemconfigure(self.match_part1, fill="#9fff33")
        else:
            self.display_canvas.itemconfigure(self.match_part1, fill="red")    
        
         # Interface: Team1 or Local
        self.match_score_team1 = self.display_canvas.create_text(((display_horizontal_resolution/2)-(width_rectangle/2)-space),display_line2,text=SportDisplay.score_team1,font=("Arial,30"))
        self.match_jail_team1 = self.display_canvas.create_text(((display_horizontal_resolution/2)-space-width_rectangle+(width_rectangle/5)),display_line4,text=SportDisplay.jail_team1)
        self.match_jail1_team1 = self.display_canvas.create_text(((display_horizontal_resolution/2)-space-width_rectangle+(width_rectangle/5)*2),display_line4,text=SportDisplay.jail1_team1)
        self.match_jail2_team1 = self.display_canvas.create_text(((display_horizontal_resolution/2)-space-width_rectangle+(width_rectangle/5)*3),display_line4,text=SportDisplay.jail2_team1)
        self.match_jail3_team1 = self.display_canvas.create_text(((display_horizontal_resolution/2)-space-width_rectangle+(width_rectangle/5)*4),display_line4,text=SportDisplay.jail3_team1)
        self.match_part2 = self.display_canvas.create_rectangle(rectangle2_X1,rectangle2_Y1,rectangle2_X2,rectangle1_Y2,outline="black",fill="white")
        self.match_name_team1 = self.display_canvas.create_text(((display_horizontal_resolution/2)-(width_rectangle/2)-space),display_line1,text="LOCAL",font=("Arial,20"))
        self.display_canvas.create_text(((display_horizontal_resolution/2)-space-width_rectangle+(width_rectangle/5)),display_line3,text="Jail#")#,font=("Arial,2"))
        self.display_canvas.create_text(((display_horizontal_resolution/2)-space-width_rectangle+(width_rectangle/5)*2),display_line3,text="Jail1")#,font=("Arial,2"))
        self.display_canvas.create_text(((display_horizontal_resolution/2)-space-width_rectangle+(width_rectangle/5)*3),display_line3,text="Jail2")#,font=("Arial,10"))
        self.display_canvas.create_text(((display_horizontal_resolution/2)-space-width_rectangle+(width_rectangle/5)*4),display_line3,text="Jail3")#,font=("Arial,10"))
        
        # Interface: Team2 or visitor
        self.match_score_team2 = self.display_canvas.create_text(((display_horizontal_resolution/2)+(width_rectangle/2)+space),display_line2,text=SportDisplay.score_team2,font=("Arial,30"))
        self.match_jail_team2 = self.display_canvas.create_text(((display_horizontal_resolution/2)+(width_rectangle/5)+space),display_line4,text=SportDisplay.jail_team2)
        self.match_jail1_team2 = self.display_canvas.create_text(((display_horizontal_resolution/2)+space+(width_rectangle/5)*2),display_line4,text=SportDisplay.jail1_team2)
        self.match_jail2_team2 = self.display_canvas.create_text(((display_horizontal_resolution/2)+space+(width_rectangle/5)*3),display_line4,text=SportDisplay.jail2_team2)
        self.match_jail3_team2 = self.display_canvas.create_text(((display_horizontal_resolution/2)+space+(width_rectangle/5)*4),display_line4,text=SportDisplay.jail3_team2)
        self.match_part3 = self.display_canvas.create_rectangle(rectangle3_X1,rectangle3_Y1,rectangle3_X2,rectangle3_Y2,outline="black",fill="white")
        self.match_name_team2 = self.display_canvas.create_text(((display_horizontal_resolution/2)+(width_rectangle/2)+space),display_line1,text="VISITOR",font=("Arial,20"))
        self.display_canvas.create_text(((display_horizontal_resolution/2)+space+(width_rectangle/5)),display_line3,text="Jail#")#,font=("Arial,2"))
        self.display_canvas.create_text(((display_horizontal_resolution/2)+space+(width_rectangle/5)*2),display_line3,text="Jail1")#,font=("Arial,2"))
        self.display_canvas.create_text(((display_horizontal_resolution/2)+space+(width_rectangle/5)*3),display_line3,text="Jail2")#,font=("Arial,10"))
        self.display_canvas.create_text(((display_horizontal_resolution/2)+space+(width_rectangle/5)*4),display_line3,text="Jail3")#,font=("Arial,10"))             
          
        self.display_canvas.tag_lower(self.match_part1,self.match_time)
        self.display_canvas.tag_lower(self.match_part2,self.match_score_team1)
        self.display_canvas.tag_lower(self.match_part3,self.match_score_team2)
        self.display_canvas.pack()
        self.update()
 
 
    def update(self):
        """ Function updating interface """
        self.display_canvas.itemconfigure(self.match_time, text=self.match.time_match)
        if self.match.chrono_on_off==1:
            self.display_canvas.itemconfigure(self.match_part1, fill="#9fff33")
            self.display_canvas.itemconfigure(self.match_period, text=self.match.period)
        else:
            self.display_canvas.itemconfigure(self.match_part1, fill="red") 
            self.display_canvas.itemconfigure(self.match_period, text="TM")
            
        self.display_canvas.itemconfigure(self.match_name_team1, text=self.match.name_team1)
        self.display_canvas.itemconfigure(self.match_name_team2, text=self.match.name_team2)
            
        
        self.display_canvas.itemconfigure(self.match_score_team1, text=self.match.score_team1)
        self.display_canvas.itemconfigure(self.match_jail_team1, text=self.match.jail_team1)
        self.display_canvas.itemconfigure(self.match_jail1_team1, text=self.match.jail_team1)
        self.display_canvas.itemconfigure(self.match_jail2_team1, text=self.match.jail2_team1)
        self.display_canvas.itemconfigure(self.match_jail3_team1, text=self.match.jail3_team1)
        self.display_canvas.itemconfigure(self.match_score_team2, text=self.match.score_team2)
        self.display_canvas.itemconfigure(self.match_jail_team2, text=self.match.jail_team2)
        self.display_canvas.itemconfigure(self.match_jail1_team2, text=self.match.jail1_team2)
        self.display_canvas.itemconfigure(self.match_jail2_team2, text=self.match.jail2_team2)
        self.display_canvas.itemconfigure(self.match_jail3_team2, text=self.match.jail3_team2)      
          
        self.after(1000, self.update)
 
    def __del__(self):
        """ Destructor interface """