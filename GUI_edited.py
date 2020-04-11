import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk
from ctypes import *
import matplotlib.pyplot as plt
import pandas as pd


########################### MAKE THE BASE WINDOW ################################

# make the root window
root = tk.Tk()

# write the window title
root.title("Tugas Besar PMC - Analisis Rangkaian")

# change the window size
root.geometry("1278x609")
root.resizable(False, False) # make the window unresizable

# insert background image name to a variable
im = Image.open("rangkaian_tubes.png")
im = im.resize((1278, 609)) # resize to fit the window
background_image = ImageTk.PhotoImage(im)

# make a label for the image
background_label = tk.Label(root, image=background_image)

# put the image label at the corner left
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#################################################################################

############################ MAKE ENTRIES FOR INPUT ############################

# Entry for Voltage Source Vs
Entry_Vs = tk.Entry(root, bd=5, width=10, justify="center")
Entry_Vs.place(x=245, y=300)

# Entry for Resistor R1
Entry_R1 = tk.Entry(root, bd=5, width=10, justify="center")
Entry_R1.place(x=290, y=205)

# Entry for Resistor R2
Entry_R2 = tk.Entry(root, bd=5, width=10, justify="center")
Entry_R2.place(x=525, y=205)

# Entry for Resistor R3
Entry_R3 = tk.Entry(root, bd=5, width=10, justify="center")
Entry_R3.place(x=465, y=285)

# Entry for Resistor R4
Entry_R4 = tk.Entry(root, bd=5, width=10, justify="center")
Entry_R4.place(x=672, y=333)

# Entry for Capacitor C
Entry_C = tk.Entry(root, bd=5, width=10, justify="center")
Entry_C.place(x=465, y=400)

# Entry for time interval for taking data, with label
label_deltaT = tk.Label(text="Time Interval (Δt) =", width=20, relief="raised", bg="#CAF1FA")
Entry_deltaT = tk.Entry(root, bd=2, width=10, justify="center", state="disabled")
label_deltaT.place(x=205, y=520)
Entry_deltaT.place(x=350, y=520)

# Entry for maximum time for taking data, with label
label_maxT = tk.Label(text="Maximum Time =", width=20, relief="raised", bg="#CAF1FA")
Entry_maxT = tk.Entry(root, bd=2, width=10, justify="center", state="disabled")
label_maxT.place(x=205, y=540)
Entry_maxT.place(x=350, y=540)

################################################################################

####################################### MAKE COMMANDS FOR THE BUTTONS #######################################

# Function to start the calculations and produce external file using C algorithm
def start_Calculation():

    # if the value is inserted correctly, calculate
    try:
        Vs = float(Entry_Vs.get())
        R1 = float(Entry_R1.get())
        R2 = float(Entry_R2.get())
        R3 = float(Entry_R3.get())
        R4 = float(Entry_R4.get())
        C = float(Entry_C.get())

        # only take deltaT and maxT when in transient mode
        if(mode.get() == 2):
            deltaT = float(Entry_deltaT.get())
            maxT = float(Entry_maxT.get())
        else:
            deltaT = 0
            maxT = 0
        
        # if the value for everything except the voltage source is <= 0, show error message
        if((R1 <= 0) or (R2 <= 0) or (R3 <= 0) or (R4 <= 0) or (C <= 0)):
            # if transient mode, check extra parameters
            if(mode.get() == 2):
                if((deltaT <= 0) or (maxT <= 0)):
                    tkinter.messagebox.showinfo("ERROR", "Ada nilai yang salah! Coba masukkan kembali nilai-nilai yang diinginkan!")
            else:
                tkinter.messagebox.showinfo("ERROR", "Ada nilai yang salah! Coba masukkan kembali nilai-nilai yang diinginkan!")
            
        else:
            # enable result buttons
            button_V1.config(state="active")
            button_V2.config(state="active")
            button_V3.config(state="active")
            button_V4.config(state="active")
            button_I1.config(state="active")
            button_I2.config(state="active")
            button_I3.config(state="active")
            button_I4.config(state="active")
            button_Ic.config(state="active")

            # do the C procedure to produce the external file
            libCall = cdll.LoadLibrary("D:\Kuliah\Materi TEKNIK ELEKTRO\Semester 4\EL2008 Pemecahan Masalah dengan C\TUGAS\Tugas Besar\libPrintTracking.dll")
            libCall.getTracking.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_double, c_double]
            libCall.getTracking(Vs, R1, R2, R3, R4, C, mode.get(), maxT, deltaT) 

            
    # if the value is inserted incorrectly, show error message
    except ValueError:
        tkinter.messagebox.showinfo("ERROR", "Ada nilai yang salah! Coba masukkan kembali nilai-nilai yang diinginkan!")

# Open external File 
dataBase =  pd.read_csv('D:\Kuliah\Materi TEKNIK ELEKTRO\Semester 4\EL2008 Pemecahan Masalah dengan C\TUGAS\Tugas Besar\HasilTracking.txt',
             delimiter=' \t'  , engine='python', skiprows = 1)

# PLOT TRACKING
# getMax value of Y
maxV =  dataBase.iloc[0]['V1']
maxI =  dataBase.iloc[0]['I1']

def show_V1():
    if(mode.get() == 1):
        print("1-V1")
    else:
        dataBase.plot(x = 'time', y = 'V1')
        plt.ylim(0, 1.1*maxV)
        plt.xlim(0)
        plt.title('Plot Tegangan V1 terhadap waktu (V)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("V1 (V)")
        plt.show()


def show_V2():
    if(mode.get() == 1):
        print("1-V2")
    else:
        dataBase.plot(x = 'time', y = 'V2')
        plt.ylim(0, 1.1*maxV)
        plt.xlim(0)
        plt.title('Plot Tegangan V2 terhadap waktu (V)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("V2 (V)")
        plt.show()

def show_V3():
    if(mode.get() == 1):
        print("1-V3")
    else:
        dataBase.plot(x = 'time', y = 'V3')
        plt.ylim(0, 1.1*maxV)
        plt.xlim(0)
        plt.title('Plot Tegangan V3 terhadap waktu (V)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("V3 (V)")
        plt.show()

def show_V4():
    if(mode.get() == 1):
        print("1-V4")
    else:
        dataBase.plot(x = 'time', y = 'V4')
        plt.ylim(0, 1.1*maxV)
        plt.xlim(0)
        plt.title('Plot Tegangan V4 terhadap waktu (V)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("V4 (V)")
        plt.show()

def show_I1():
    if(mode.get() == 1):
        print("1-I1")
    else:
        dataBase.plot(x = 'time', y = 'I1')
        plt.ylim(0, 1.1*maxI)
        plt.xlim(0)
        plt.title('Plot Tegangan I1 terhadap waktu (A)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("I1 (A)")
        plt.show()

def show_I2():
    if(mode.get() == 1):
        print("1-I2")
    else:
        dataBase.plot(x = 'time', y = 'I2')
        plt.ylim(0, 1.1*maxI)
        plt.xlim(0)
        plt.title('Plot Tegangan I2 terhadap waktu (A)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("I2 (A)")
        plt.show()

def show_I3():
    if(mode.get() == 1):
        print("1-I3")
    else:
        dataBase.plot(x = 'time', y = 'I3')
        plt.ylim(0, 1.1*maxI)
        plt.xlim(0)
        plt.title('Plot Tegangan I3 terhadap waktu (A)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("I3 (A)")
        plt.show()

def show_I4():
    if(mode.get() == 1):
        print("1-I4")
    else:
        dataBase.plot(x = 'time', y = 'I4')
        plt.ylim(0, 1.1*maxI)
        plt.xlim(0)
        plt.title('Plot Tegangan I4 terhadap waktu (A)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("V4 (A)")
        plt.show()

def show_Ic():
    if(mode.get() == 1):
        print("1-Ic")
    else:
        dataBase.plot(x = 'time', y = 'Ic')
        plt.ylim(0, 1.1*maxI)
        plt.xlim(0)
        plt.title('Plot Tegangan Ic terhadap waktu (A)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("Vc (A)")
        plt.show()

# Function to disable all result buttons
def freeze_Button():
    button_V1.config(state="disabled")
    button_V2.config(state="disabled")
    button_V3.config(state="disabled")
    button_V4.config(state="disabled")
    button_I1.config(state="disabled")
    button_I2.config(state="disabled")
    button_I3.config(state="disabled")
    button_I4.config(state="disabled")
    button_Ic.config(state="disabled")

    # if dc analysis, doesn't need deltaT or maxT
    if(mode.get()==1):
        Entry_deltaT.config(state="disabled")
        Entry_maxT.config(state="disabled")
    else:
        Entry_deltaT.config(state="normal")
        Entry_maxT.config(state="normal")


#############################################################################################################

############################################# MAKE THE BUTTONS #############################################

button_Start = tk.Button(root, text="Start", font=("Helvetica", 12, "bold"), command=start_Calculation, width=15)
button_Start.place(x=1060, y=510)

button_V1 = tk.Button(root, text="V1", font=("Helvetica", 12, "bold"), command=show_V1, width=31, state="disabled")
button_V1.place(x=900, y=170)

button_V2 = tk.Button(root, text="V2", font=("Helvetica", 12, "bold"), command=show_V2, width=31, state="disabled")
button_V2.place(x=900, y=205)

button_V3 = tk.Button(root, text="V3", font=("Helvetica", 12, "bold"), command=show_V3, width=31, state="disabled")
button_V3.place(x=900, y=240)

button_V4 = tk.Button(root, text="V4", font=("Helvetica", 12, "bold"), command=show_V4, width=31, state="disabled")
button_V4.place(x=900, y=275)

button_I1 = tk.Button(root, text="I1", font=("Helvetica", 12, "bold"), command=show_I1, width=31, state="disabled")
button_I1.place(x=900, y=310)

button_I2 = tk.Button(root, text="I2", font=("Helvetica", 12, "bold"), command=show_I2, width=31, state="disabled")
button_I2.place(x=900, y=345)

button_I3 = tk.Button(root, text="I3", font=("Helvetica", 12, "bold"), command=show_I3, width=31, state="disabled")
button_I3.place(x=900, y=380)

button_I4 = tk.Button(root, text="I4", font=("Helvetica", 12, "bold"), command=show_I4, width=31, state="disabled")
button_I4.place(x=900, y=415)

button_Ic = tk.Button(root, text="Ic", font=("Helvetica", 12, "bold"), command=show_Ic, width=31, state="disabled")
button_Ic.place(x=900, y=450)

##################################################################################################################################

############################################ MAKE RADIO BUTTONS FOR THE ANALYSIS MODE ############################################

# set a variable for the value of the radio buttons
mode = tk.IntVar()
mode.set(1)             # set initial mode to 1 (DC Analysis)

# create & place the radio buttons
DC_RB = tk.Radiobutton(root, text="DC Analysis", font=("Helvetica", 12, "bold"), variable=mode, indicator=0,
                        value=1, width=15, selectcolor="light blue", command=freeze_Button)
DC_RB.place(x=900, y=100)

tran_RB = tk.Radiobutton(root, text="Transient Analysis", font=("Helvetica", 12, "bold"), variable=mode, indicator=0,
                        value=2, width=15, selectcolor="light blue", command=freeze_Button)
tran_RB.place(x=1060, y=100)

####################################################################################################################################

# loop the root window until closed
root.mainloop()


