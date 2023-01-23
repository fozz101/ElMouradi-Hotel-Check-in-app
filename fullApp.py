# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 07:41:54 2022

@author: fedig
"""
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import time
import threading
import os
import sys


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
#os.chdir(r"C:\Users\fedig\Desktop\check-in app")

config_name = 'myapp.cfg'

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

config_path = os.path.join(application_path, config_name)


def generatePDF():
    '''
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont
    from tkinter.messagebox import showinfo
'''
    file = filedialog.askopenfile(parent=window,mode='rb',title="Choose participants' sheet")
    if file != None:
        sheet = pd.read_csv(file.name,encoding = "ISO-8859-1", engine='python')
        fullName=sheet["Full Name"]
        email=sheet["IEEE Email"]
        birth=sheet["Date and place of birth "]
        address=sheet["Full adress( Street, City )"]
        cin=sheet["ID Card , Issued on, By (Exp: 98****** Issued on 12/11/2020 By Tunis)  "]
        phoneNumber=sheet["Phone Number"]
        label = Label( window, text="Loaded participants: "+str(len(fullName))).place(x = 0,y = 0)
        for i in (range(0,len(fullName))):
            img = Image.open("fiche_voyageur.jpg")
            I1 = ImageDraw.Draw(img)
            font = ImageFont.truetype("arial.ttf", 70)
            '''
            I1.text((2100, 1175), email[i], fill =(0, 0, 0),font=font)
            I1.text((2500, 1550), fullName[i], fill =(0, 0, 0),font=font)
            I1.text((2500, 2010), birth[i], fill =(0, 0, 0),font=font)
            I1.text((2200, 2890), address[i], fill =(0, 0, 0),font=font)
            I1.text((2900, 4450), cin[i], fill =(0, 0, 0),font=font)
            '''
            threading.Thread(target=I1.text((2700, 3280), str(phoneNumber[i]), fill =(0, 0, 0),font=font)).start()
            threading.Thread(target=I1.text((2100, 1175), email[i], fill =(0, 0, 0),font=font)).start()
            threading.Thread(target=I1.text((2500, 1550), fullName[i], fill =(0, 0, 0),font=font)).start()
            ##Birth DATE
            try:
                threading.Thread(target=I1.text((2500, 2010), birth[i].split(" ")[0], fill =(0, 0, 0),font=font)).start()
            except:
                pass
                #print("No Birth Date")
            
            ##Birth Place
            try:
                if len(birth[i].split(" "))>2:
                    threading.Thread(target=I1.text((2500, 2220), birth[i].split(" ")[len(birth[i].split(" "))-1], fill =(0, 0, 0),font=font)).start()
                else:   
                    threading.Thread(target=I1.text((2500, 2220), birth[i].split(" ")[1], fill =(0, 0, 0),font=font)).start()
            except:
                pass
                #print("No Birth Place")
            
            #threading.Thread(target=I1.text((2500, 2010), birth[i], fill =(0, 0, 0),font=font)).start()
            threading.Thread(target=I1.text((2200, 2890), address[i], fill =(0, 0, 0),font=font)).start()
            #threading.Thread(target=I1.text((2900, 4450), cin[i], fill =(0, 0, 0),font=font)).start()
            ##CIN ID
            threading.Thread(target=I1.text((3100, 4345), cin[i].lower().split("issued on")[0], fill =(0, 0, 0),font=font)).start()
            ##CIN DATE
            try:
                threading.Thread(target=I1.text((3580, 4540), cin[i].lower().split("issued on")[1].split("by")[0], fill =(0, 0, 0),font=font)).start()
                #print(cin[i].lower().split("issued on")[1].split("by")[0])
            except:
                pass
                #print("No CIN Date")
            
            ##CIN By
            try:
                threading.Thread(target=I1.text((2900, 4540), cin[i].lower().split("issued on")[1].split("by")[1], fill =(0, 0, 0),font=font)).start()
                #print(cin[i].lower().split("issued on")[1].split("by")[1])
            except:
                pass
                #print("No CIN Place")
            im_1 = img.convert('RGB')
            #im_1.save("output/"+str(i)+"_"+fullName[i]+".pdf")
            im_1.save("output/"+str(i)+"_"+fullName[i]+".pdf")
            my_progress["value"]+=int(100/len(fullName))
            #window.update_idletasks()
            #time.sleep(1)
            progressStatus = Label (window,text="Done: "+str(i+1)).place(x=110,y=230)
        my_progress.stop()
        messagebox.showinfo("Complete", "Done !")


    else:
        print("error")






if __name__ == "__main__":
    config_name = 'myapp.cfg'

# determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)
    
    config_path = os.path.join(application_path, config_name)
    window = Tk()
    window.iconbitmap("icon.ico")
    messagebox.showinfo("Information", "- The process takes some minutes... \n- While generating PDFs, The window may look freezed, don't panic and leave it alone !\n- PDFs are generated in the output directory !")
    window.geometry("400x400")
    window.title("Generate PDF")


    bg = PhotoImage(file = "bg.png")
    limg= Label(window, image=bg)
    limg.pack()






    my_progress = ttk.Progressbar(window, orient=HORIZONTAL, length = 200 , mode= "determinate")
    my_progress.pack()







    stopBtn=Button(window, text ="Close(stop :3)",command=window.destroy)
    stopBtn.pack(pady=10,padx=10)
    stopBtn.place(x=240, y=270)


    generateBtn=Button(window, text ="Generate files", command = threading.Thread(target=generatePDF).start())
    #generateBtn=Button(window, text ="Generate files", command = generatePDF)
    #generateBtn.pack()
    generateBtn.pack_forget()
    #generateBtn.place(x=110, y=270)

    window.mainloop()

