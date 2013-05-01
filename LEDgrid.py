#!/usr/bin/python

import os
import sys


from Tkinter import *
from functools import partial

# import CreateAllNightSkyStrings
import NSEphem

class LEDGrid:
    
    def __init__(self, top):

        file = sys.argv[0]
        __dir__ = os.path.dirname(file)
        # __dir__ = os.path.dirname(os.path.abspath(__file__))
        self.LED_red_on_photo = PhotoImage(file=os.path.join(__dir__,'LED-red-on.gif'))
        self.LED_yellow_on_photo = PhotoImage(file=os.path.join(__dir__,'LED-yellow-on.gif'))
        self.LED_blue_on_photo = PhotoImage(file=os.path.join(__dir__,'LED-blue-on.gif'))
        self.LED_orange_on_photo = PhotoImage(file=os.path.join(__dir__,'LED-orange-on.gif'))
        self.LED_white_on_photo = PhotoImage(file=os.path.join(__dir__,'LED-white-on.gif'))
        self.LED_red_dim_photo = PhotoImage(file=os.path.join(__dir__,'LED-red-dim.gif'))
        self.LED_yellow_dim_photo = PhotoImage(file=os.path.join(__dir__,'LED-yellow-dim.gif'))
        self.LED_blue_dim_photo = PhotoImage(file=os.path.join(__dir__,'LED-blue-dim.gif'))
        self.LED_orange_dim_photo = PhotoImage(file=os.path.join(__dir__,'LED-orange-dim.gif'))
        self.LED_white_dim_photo = PhotoImage(file=os.path.join(__dir__,'LED-white-dim.gif'))
        self.LED_off_photo = PhotoImage(file=os.path.join(__dir__,'LED-off.gif'))
        self.Earth_photo = PhotoImage(file=os.path.join(__dir__,'earth.gif'))
        self.Sun_photo = PhotoImage(file=os.path.join(__dir__,'sun.gif'))
        self.Moon_photo = PhotoImage(file=os.path.join(__dir__,'moon.gif'))
        self.ISS_photo = PhotoImage(file=os.path.join(__dir__,'ISS.gif'))
        self.Venus_photo = PhotoImage(file=os.path.join(__dir__,'venus.gif'))
        self.Mars_photo = PhotoImage(file=os.path.join(__dir__,'mars.gif'))
        self.Jupiter_photo = PhotoImage(file=os.path.join(__dir__,'jupiter.gif'))
        self.Saturn_photo = PhotoImage(file=os.path.join(__dir__,'saturn.gif'))
        self.Seven_photo = PhotoImage(file=os.path.join(__dir__,'Seven.gif'))
        self.Eight_photo = PhotoImage(file=os.path.join(__dir__,'Eight.gif'))
        self.Nine_photo = PhotoImage(file=os.path.join(__dir__,'Nine.gif'))
        self.Ten_photo = PhotoImage(file=os.path.join(__dir__,'Ten.gif'))
        self.Eleven_photo = PhotoImage(file=os.path.join(__dir__,'Eleven.gif'))
        self.Twelve_photo = PhotoImage(file=os.path.join(__dir__,'Twelve.gif'))
        self.One_photo = PhotoImage(file=os.path.join(__dir__,'One.gif'))
        self.Two_photo = PhotoImage(file=os.path.join(__dir__,'Two.gif'))
        self.H_Wood_photo = PhotoImage(file=os.path.join(__dir__,'H-Wood.gif'))
        self.V_Wood_photo = PhotoImage(file=os.path.join(__dir__,'V-Wood.gif'))
        self.bg_color = "#D2691E"
        self.border_color = "#000000"
        self.ticks = 0
        
        self.top = top
        self.button_dic = {}     ## pointer to buttons and StringVar()
        self.button_state_dic = {"on":[], "off":[], "dim":[], "flash1":[], "flash2":[], "flash3":[], "flash4":[], "flash5":[], "flash6":[]}

        self.top.title('Night Sky Orb')
        self.top_frame = Frame(self.top, width =700, height=700, bg=self.bg_color)
        self.buttons()
        self.top_frame.grid(row=0, column=1)
        
        self.create_left_labels()
        
        # self.All_NS_obj = CreateAllNightSkyStrings.CreateAllNightSkyStrings()
        self.All_NS_obj = NSEphem.CreateAllNightSkyStrings()

        #exit = Button(self.top_frame, text='Exit', \
        #     command=self.top.quit).grid(row=10,column=0, columnspan=5)
        
        #update = Button(self.top_frame, text='Update', \
        #     command=self.update_cb_handler).grid(row=10,column=2, columnspan=5)

        all_NS_strings = self.All_NS_obj.get_all_NS_strings()

        for i, aNightSkyString in enumerate(all_NS_strings):      
            
            NS_object_string = aNightSkyString
            row = i + 1
            
            # test code for flashing test
            #if row == 4:
            #    NS_object_string = "X48lgahaijkZ"
            
            
            #print "row, string", row, NS_object_string
            print NS_object_string
            

            
            self.update_LED_row(row, NS_object_string)
                            
        #print "creating bottom labels"    
        self.create_bottom_labels(10)
        
        self.blink()        
        
    def create_left_labels(self):
        for j in range(0,11):
            ColLbl = Label(self.top_frame,image=self.V_Wood_photo,height=54,width=54,relief="flat",fg=self.border_color,bd=0)
            ColLbl.grid(row=j, column=0)
                  
    def create_top_labels(self):
        for j in range(1,10):
            ColLbl = Label(self.top_frame,image=self.H_Wood_photo,height=54,width=66,relief="flat",bd=0)
            ColLbl.grid(row=0, column=j)
        ColLbl = Label(self.top_frame, bg=self.bg_color)
        ColLbl.grid(row=1, column=1)
        ColLbl = Label(self.top_frame, image=self.Seven_photo, bg=self.bg_color,height=50,width=50)
        ColLbl.grid(row=1, column=2)
        ColLbl = Label(self.top_frame, image=self.Eight_photo, bg=self.bg_color,height=50,width=50)
        ColLbl.grid(row=1, column=3)
        ColLbl = Label(self.top_frame, image=self.Nine_photo, bg=self.bg_color,height=50,width=50)
        ColLbl.grid(row=1, column=4)
        ColLbl = Label(self.top_frame, image=self.Ten_photo, bg=self.bg_color,height=50,width=50)
        ColLbl.grid(row=1, column=5)
        ColLbl = Label(self.top_frame, image=self.Eleven_photo, bg=self.bg_color,height=50,width=50)
        ColLbl.grid(row=1, column=6)
        ColLbl = Label(self.top_frame, image=self.Twelve_photo, bg=self.bg_color,height=50,width=50)
        ColLbl.grid(row=1, column=7)
        ColLbl = Label(self.top_frame, image=self.One_photo, bg=self.bg_color,height=50,width=50)
        ColLbl.grid(row=1, column=8)
        ColLbl = Label(self.top_frame, image=self.Two_photo, bg=self.bg_color,height=50,width=50)
        ColLbl.grid(row=1, column=9)
        
    def create_bottom_labels(self,row_num):
        for j in range(1,10):
            ColLbl = Label(self.top_frame,image=self.H_Wood_photo,height=54,width=66,relief="flat",fg=self.border_color,bd=0)
            ColLbl.grid(row=row_num, column=j)

    def button_flasher(self, square_number, flash_count ):
            if self.ticks == 0:
                self.button_dic[square_number][1].config(image=self.LED_blue_on_photo)        
            if self.ticks == 1:
                self.button_dic[square_number][1].config(image=self.LED_off_photo)
            if self.ticks == 2:
                self.button_dic[square_number][1].config(image=self.LED_blue_on_photo)
                
            if self.ticks == 3 and flash_count > 1:
                self.button_dic[square_number][1].config(image=self.LED_off_photo)
            if self.ticks == 4 and flash_count > 1:
                self.button_dic[square_number][1].config(image=self.LED_blue_on_photo)

            if self.ticks == 5 and flash_count > 2:
                self.button_dic[square_number][1].config(image=self.LED_off_photo)
            if self.ticks == 6 and flash_count > 2:
                self.button_dic[square_number][1].config(image=self.LED_blue_on_photo)

            if self.ticks == 7 and flash_count > 3:
                self.button_dic[square_number][1].config(image=self.LED_off_photo)
            if self.ticks == 8 and flash_count > 3:
                self.button_dic[square_number][1].config(image=self.LED_blue_on_photo)

            if self.ticks == 9 and flash_count > 4:
                self.button_dic[square_number][1].config(image=self.LED_off_photo)
            if self.ticks == 10 and flash_count > 4:
                self.button_dic[square_number][1].config(image=self.LED_blue_on_photo)

            if self.ticks == 11 and flash_count > 5:
                self.button_dic[square_number][1].config(image=self.LED_off_photo)
            if self.ticks == 12 and flash_count > 5:
                self.button_dic[square_number][1].config(image=self.LED_blue_on_photo)        
        
        
    def blink(self): 
        #print "do blinky stuff here"
        self.ticks = self.ticks + 1
        if self.ticks > 30:
            self.ticks = 0
        #print "ticks = ", self.ticks
        
        self.top.after(300, self.blink)

        for square_number in self.button_state_dic["flash1"]:            
            #print "found a flash1 for square =", square_number            
            self.button_flasher(square_number, 1)
        
        #flash2 is on on ticks 0 and 2
        for square_number in self.button_state_dic["flash2"]:            
            #print "found a flash2 for square =", square_number
            self.button_flasher(square_number, 2)                         

        for square_number in self.button_state_dic["flash3"]:
            self.button_flasher(square_number, 3)             

        for square_number in self.button_state_dic["flash4"]:            
            #print "found a flash4 for square =", square_number
            self.button_flasher(square_number, 4) 

        for square_number in self.button_state_dic["flash5"]:            
            #print "found a flash5 for square =", square_number
            self.button_flasher(square_number, 5) 
        
        for square_number in self.button_state_dic["flash6"]:            
            #print "found a flash6 for square =", square_number
            self.button_flasher(square_number, 6)       
        
    def create_row_label(self,b_row):
            if (b_row ==1):
                RowLbl = Label(self.top_frame,image=self.Earth_photo)
                RowLbl.config(bg=self.bg_color)
                RowLbl.config(relief="flat")
                RowLbl.grid(row=2, column=1)
            if (b_row ==2):
                RowLbl = Label(self.top_frame,image=self.Sun_photo)
                RowLbl.config(bg=self.bg_color)
                RowLbl.config(relief="flat")
                RowLbl.grid(row=3, column=1)
            if (b_row ==3):
                RowLbl = Label(self.top_frame,image=self.Moon_photo)
                RowLbl.config(bg=self.bg_color)
                RowLbl.config(relief="flat")
                RowLbl.grid(row=4, column=1)
            if (b_row ==4):
                RowLbl = Label(self.top_frame,image=self.ISS_photo)
                RowLbl.config(bg=self.bg_color)
                RowLbl.config(relief="flat")
                RowLbl.grid(row=5, column=1)
            if (b_row ==5):
                RowLbl = Label(self.top_frame,image=self.Venus_photo)
                RowLbl.config(bg=self.bg_color)
                RowLbl.config(relief="flat")
                RowLbl.grid(row=6, column=1)
            if (b_row ==6):
                RowLbl = Label(self.top_frame,image=self.Mars_photo)
                RowLbl.config(bg=self.bg_color)
                RowLbl.config(relief="flat")
                RowLbl.grid(row=7, column=1)
            if (b_row ==7):
                RowLbl = Label(self.top_frame,image=self.Jupiter_photo)
                RowLbl.config(bg=self.bg_color)
                RowLbl.config(relief="flat")
                RowLbl.grid(row=8, column=1)
            if (b_row ==8):
                RowLbl = Label(self.top_frame,image=self.Saturn_photo)
                RowLbl.config(bg=self.bg_color)
                RowLbl.config(relief="flat")
                RowLbl.grid(row=9, column=1)
        
    def buttons(self):
        """ create 64 buttons, a 8x8 grid
        """
        
        self.create_top_labels()
                
        b_row=1
        b_col=0
        for j in range(1, 65):
            
            if (b_col==0):
                self.create_row_label(b_row)
                            
            sv=StringVar()
            sv.set(j)
            b = Button(self.top_frame, bitmap='gray50', \
                    command=partial(self.cb_handler, j), bg='black')
            
            #print( "j, r, c", j, b_row, b_col)
            b.grid(row=b_row+1, column=b_col+2)
            self.button_dic[j]=[sv, b] ## button number-->(StringVar, Tkinter ID)
            self.button_state_dic["off"].append(j)

            b_col += 1
            if b_col > 7:
                b_col = 0
                b_row += 1
                
    def set_LED_off(self, square_number):
            self.button_dic[square_number][1].config(bg=self.bg_color)
            self.button_dic[square_number][1].config(relief="flat")
            self.button_dic[square_number][1].config(image=self.LED_off_photo)
            self.button_state_dic["off"].append(square_number)
    
    def set_LED_on(self, square_number,color):
            self.button_dic[square_number][1].config(bg=self.bg_color)
            self.button_dic[square_number][1].config(relief="flat")
            if color == "red":
                self.button_dic[square_number][1].config(image=self.LED_red_on_photo)
            if color == "white":
                self.button_dic[square_number][1].config(image=self.LED_white_on_photo)
            if color == "blue":
                self.button_dic[square_number][1].config(image=self.LED_blue_on_photo)
            if color == "yellow":
                self.button_dic[square_number][1].config(image=self.LED_yellow_on_photo)
            if color == "orange":
                self.button_dic[square_number][1].config(image=self.LED_orange_on_photo)
            self.button_state_dic["on"].append(square_number)

    def set_LED_dim(self, square_number,color):
            self.button_dic[square_number][1].config(bg=self.bg_color)
            self.button_dic[square_number][1].config(relief="flat")
            
            if color == "red":
                self.button_dic[square_number][1].config(image=self.LED_red_dim_photo)
            if color == "white":
                self.button_dic[square_number][1].config(image=self.LED_white_dim_photo)
            if color == "blue":
                self.button_dic[square_number][1].config(image=self.LED_blue_dim_photo)
            if color == "yellow":
                self.button_dic[square_number][1].config(image=self.LED_yellow_dim_photo)
            if color == "orange":
                self.button_dic[square_number][1].config(image=self.LED_orange_dim_photo)
            self.button_state_dic["dim"].append(square_number)

    def set_LED_flash1(self, square_number):
            self.button_dic[square_number][1].config(bg=self.bg_color)
            self.button_dic[square_number][1].config(relief="flat")        
            self.button_dic[square_number][1].config(image=self.LED_blue_on_photo)
            self.button_state_dic["flash1"].append(square_number)

    def set_LED_flash2(self, square_number):        
            self.button_dic[square_number][1].config(bg=self.bg_color)
            self.button_dic[square_number][1].config(relief="flat")        
            self.button_dic[square_number][1].config(image=self.LED_blue_on_photo)
            self.button_state_dic["flash2"].append(square_number)

    def set_LED_flash3(self, square_number):
            self.button_dic[square_number][1].config(bg=self.bg_color)
            self.button_dic[square_number][1].config(relief="flat")        
            self.button_dic[square_number][1].config(image=self.LED_blue_on_photo)
            self.button_state_dic["flash3"].append(square_number)        

    def set_LED_flash4(self, square_number):        
            self.button_dic[square_number][1].config(bg=self.bg_color)
            self.button_dic[square_number][1].config(relief="flat")        
            self.button_dic[square_number][1].config(image=self.LED_blue_on_photo)
            self.button_state_dic["flash4"].append(square_number)

    def set_LED_flash5(self, square_number):        
            self.button_dic[square_number][1].config(bg=self.bg_color)
            self.button_dic[square_number][1].config(relief="flat")        
            self.button_dic[square_number][1].config(image=self.LED_blue_on_photo)
            self.button_state_dic["flash5"].append(square_number)

    def set_LED_flash6(self, square_number):        
            self.button_dic[square_number][1].config(bg=self.bg_color)
            self.button_dic[square_number][1].config(relief="flat")        
            self.button_dic[square_number][1].config(image=self.LED_blue_on_photo)
            self.button_state_dic["flash6"].append(square_number)

    def get_square(self,r,c):
        square = (r-1)*8+c
        return square


    def cb_handler(self, square_number):

        print "cb_handler update data"
        all_NS_strings = self.All_NS_obj.get_all_NS_strings()

        for i, aNightSkyString in enumerate(all_NS_strings):      
            
            NS_object_string = aNightSkyString
            row = i + 1
            #print "row, string", row, NS_object_string
            print NS_object_string
            self.update_LED_row(row, NS_object_string)
            
    def update_LED_row(self, row, r_str):
        
        if row == 1:
            color = "blue"
        if row == 2:
            color = "yellow"
        if row == 3:
            color = "white"
        if row == 4:
            color = "blue"
        if row == 5:
            color = "white"
        if row == 6:
            color = "red"
        if row == 7:
            color = "orange"
        if row == 8:
            color = "yellow" 
        for col in range (1,9):     
            square_number = self.get_square(row, col)
            char = r_str[col+2]
            if (char=='a'):
                self.set_LED_off(square_number)
            elif (char=='b'):
                self.set_LED_dim(square_number,color)
            elif (char=='c'):
                self.set_LED_on(square_number,color)
            elif (char=='g'):
                self.set_LED_flash1(square_number)
            elif (char=='h'):
                self.set_LED_flash2(square_number)
            elif (char=='i'):
                self.set_LED_flash3(square_number)
            elif (char=='j'):
                self.set_LED_flash4(square_number)
            elif (char=='k'):
                self.set_LED_flash5(square_number)
            elif (char=='l'):
                self.set_LED_flash6(square_number)
                                
            ColLbl = Label(self.top_frame,image=self.V_Wood_photo,height=54,width=54,relief="flat",fg=self.border_color,bd=0)
            ColLbl.grid(row=row+1, column=10)
            
            #ColLbl = Label(self.top_frame,image=self.V_Wood_photo,height=50,width=60,relief="flat",fg=self.border_color,bd=0)
            #ColLbl.grid(row=row+1, column=0)
            
            
        ColLbl = Label(self.top_frame,image=self.V_Wood_photo,height=54,width=54,relief="flat",fg=self.border_color,bd=0)
        ColLbl.grid(row=0, column=10)                  
        ColLbl = Label(self.top_frame,image=self.V_Wood_photo,height=54,width=54,relief="flat",fg=self.border_color,bd=0)
        ColLbl.grid(row=1, column=10)
        ColLbl = Label(self.top_frame,image=self.V_Wood_photo,height=54,width=54,relief="flat",fg=self.border_color,bd=0)
        ColLbl.grid(row=10, column=10)                  

    def update_cb_handler(self):
            
        #print "update cb handler"
                    
        all_NS_strings = self.All_NS_obj.get_all_NS_strings()

        for i, aNightSkyString in enumerate(all_NS_strings):      
            
            NS_object_string = aNightSkyString
            row = i + 1
            #print "row, string", row, NS_object_string
            print NS_object_string
            self.update_LED_row(row, NS_object_string)



root = Tk()
BT=LEDGrid(root)
root.mainloop()
