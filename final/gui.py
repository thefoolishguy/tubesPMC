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

# set icon
root.iconbitmap("./resistor_icon.ico")

# insert background image name to a variable
im = Image.open("./rangkaian_tubes.png")
im = im.resize((1278, 609)) # resize to fit the window
background_image = ImageTk.PhotoImage(im)

# make a label for the image
background_label = tk.Label(root, image=background_image)

# put the image label at the corner left
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# create label for the member's names + NIM
member_title_label = tk.Label(root, text="Kelompok 11", font=("Helvetica", 15, "bold"), bg="white", justify="left", padx=15)
member_title_label.pack(anchor="nw")

member_label = tk.Label(root, text="Agung Dwi Laksana (13218034)\nMatthew Ryo Kianijaya (13218035)\nChyndi Octavia Devi (13218039)\nAmelia Khoirurrahma (18318003)",
                        bg="white", font=("Helvetica", 12), justify="left", padx=15)
member_label.pack(anchor="nw")

#################################################################################

############################ MAKE ENTRIES FOR INPUT ############################

# Entry for Voltage Source Vs + Unit Label
Entry_Vs = tk.Entry(root, bd=5, width=10, justify="center")
Entry_Vs.place(x=245, y=300)
label_Vs = tk.Label(root, text="V", font=("Helvetica", 10, "bold"), bg="white")
label_Vs.place(x=320, y=300)


# Entry for Resistor R1 + Unit Label
Entry_R1 = tk.Entry(root, bd=5, width=10, justify="center")
Entry_R1.place(x=290, y=205)
label_R1 = tk.Label(root, text="Ω", font=("Helvetica", 10, "bold"), bg="white")
label_R1.place(x=365, y=205)

# Entry for Resistor R2 + Unit Label
Entry_R2 = tk.Entry(root, bd=5, width=10, justify="center")
Entry_R2.place(x=465, y=285)
label_R2 = tk.Label(root, text="Ω", font=("Helvetica", 10, "bold"), bg="white")
label_R2.place(x=540, y=285)

# Entry for Resistor R3 + Unit Label
Entry_R3 = tk.Entry(root, bd=5, width=10, justify="center")
Entry_R3.place(x=525, y=205)
label_R3 = tk.Label(root, text="Ω", font=("Helvetica", 10, "bold"), bg="white")
label_R3.place(x=600, y=205)

# Entry for Resistor R4 + Unit Label
Entry_R4 = tk.Entry(root, bd=5, width=10, justify="center")
Entry_R4.place(x=672, y=333)
label_R4 = tk.Label(root, text="Ω", font=("Helvetica", 10, "bold"), bg="white")
label_R4.place(x=747, y=333)

# Entry for Capacitor C + Unit Label
Entry_C = tk.Entry(root, bd=5, width=10, justify="center")
Entry_C.place(x=465, y=400)
label_C = tk.Label(root, text="F", font=("Helvetica", 10, "bold"), bg="white")
label_C.place(x=540, y=400)

# Entry for time interval for taking data, with label
label_deltaT = tk.Label(text="Time Interval (s) =", width=20, relief="raised", bg="#CAF1FA")
Entry_deltaT = tk.Entry(root, bd=2, width=10, justify="center", state="disabled")
label_deltaT.place(x=205, y=520)
Entry_deltaT.place(x=350, y=520)

# Entry for maximum time for taking data, with label
label_maxT = tk.Label(text="Maximum Time (s) =", width=20, relief="raised", bg="#CAF1FA")
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

            # if it's dc analysis, make maxT and deltaT = 0 to avoid error
            if(mode.get() == 1):
                maxT = 0
                deltaT = 0

            # do the C procedure to produce the external file
            so_file = "./TugasBesarStatic.so"
            calc_function = cdll.LoadLibrary(so_file)
            
            calc_function.getTracking.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_double, c_double]
            calc_function.getTracking(Vs, R1, R2, R3, R4, C, mode.get(), maxT, deltaT)    
            
    # if the value is inserted incorrectly, show error message
    except ValueError:
        tkinter.messagebox.showinfo("ERROR", "Ada nilai yang salah! Coba masukkan kembali nilai-nilai yang diinginkan!")

def show_V1():
    dataBase = pd.read_csv("./HasilTracking.txt", delimiter=" \t", engine="python", skiprows=1)
    maxV =  dataBase.iloc[0]['V1']
    maxI =  dataBase.iloc[0]['I1']

    # if DC analysis, the result is only on the 1st row
    if(mode.get() == 1):
        tkinter.messagebox.showinfo("Hasil Perhitungan V1               ", "V1 = " + str(dataBase.iloc[0]['V1']) + " [V]")
    # if transient analysis, plot the graph and show it
    else:
        dataBase.plot(x = 'time', y = 'V1')
        plt.ylim(0, 1.1*maxV)
        plt.xlim(0)
        plt.title('Plot Tegangan V1 Terhadap Waktu (V)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("V1 (V)")
        plt.show()

def show_V2():
    dataBase = pd.read_csv("./HasilTracking.txt", delimiter=" \t", engine="python", skiprows=1)
    maxV =  dataBase.iloc[0]['V1']
    maxI =  dataBase.iloc[0]['I1']

    # if DC analysis, the result is only on the 1st row
    if(mode.get() == 1):
        tkinter.messagebox.showinfo("Hasil Perhitungan V2               ", "V2 = " + str(dataBase.iloc[0]['V2']) + " [V]")
    # if transient analysis, plot the graph and show it
    else:
        dataBase.plot(x = 'time', y = 'V2')
        plt.ylim(0, 1.1*maxV)
        plt.xlim(0)
        plt.title('Plot Tegangan V2 Terhadap Waktu (V)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("V2 (V)")
        plt.show()

def show_V3():
    dataBase = pd.read_csv("./HasilTracking.txt", delimiter=" \t", engine="python", skiprows=1)
    maxV =  dataBase.iloc[0]['V1']
    maxI =  dataBase.iloc[0]['I1']

    # if DC analysis, the result is only on the 1st row
    if(mode.get() == 1):
        tkinter.messagebox.showinfo("Hasil Perhitungan V3               ", "V3 = " + str(dataBase.iloc[0]['V3']) + " [V]")
    # if transient analysis, plot the graph and show it
    else:
        dataBase.plot(x = 'time', y = 'V3')
        plt.ylim(0, 1.1*maxV)
        plt.xlim(0)
        plt.title('Plot Tegangan V3 Terhadap Waktu (V)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("V3 (V)")
        plt.show()

def show_V4():
    dataBase = pd.read_csv("./HasilTracking.txt", delimiter=" \t", engine="python", skiprows=1)
    maxV =  dataBase.iloc[0]['V1']
    maxI =  dataBase.iloc[0]['I1']

    # if DC analysis, the result is only on the 1st row
    if(mode.get() == 1):
        tkinter.messagebox.showinfo("Hasil Perhitungan V4               ", "V4 = " + str(dataBase.iloc[0]['V4']) + " [V]")
    # if transient analysis, plot the graph and show it
    else:
        dataBase.plot(x = 'time', y = 'V4')
        plt.ylim(0, 1.1*maxV)
        plt.xlim(0)
        plt.title('Plot Tegangan V4 Terhadap Waktu (V)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("V4 (V)")
        plt.show()

def show_I1():
    dataBase = pd.read_csv("./HasilTracking.txt", delimiter=" \t", engine="python", skiprows=1)
    maxV =  dataBase.iloc[0]['V1']
    maxI =  dataBase.iloc[0]['I1']

    # if DC analysis, the result is only on the 1st row
    if(mode.get() == 1):
        tkinter.messagebox.showinfo("Hasil Perhitungan I(R1)               ", "I(R1) = " + str(dataBase.iloc[0]['I1']) + " [A]")
    # if transient analysis, plot the graph and show it
    else:
        dataBase.plot(x = 'time', y = 'I1')
        plt.ylim(0, 1.1*maxI)
        plt.xlim(0)
        plt.title('Plot Arus I(R1) Terhadap Waktu (A)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("I(R1) (A)")
        plt.show()

def show_I2():
    dataBase = pd.read_csv("./HasilTracking.txt", delimiter=" \t", engine="python", skiprows=1)
    maxV =  dataBase.iloc[0]['V1']
    maxI =  dataBase.iloc[0]['I1']

    # if DC analysis, the result is only on the 1st row
    if(mode.get() == 1):
        tkinter.messagebox.showinfo("Hasil Perhitungan I(R2)               ", "I(R2) = " + str(dataBase.iloc[0]['I2']) + " [A]")
    # if transient analysis, plot the graph and show it
    else:
        dataBase.plot(x = 'time', y = 'I2')
        plt.ylim(0, 1.1*maxI)
        plt.xlim(0)
        plt.title('Plot Arus I(R2) Terhadap Waktu (A)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("I(R2) (A)")
        plt.show()

def show_I3():
    dataBase = pd.read_csv("./HasilTracking.txt", delimiter=" \t", engine="python", skiprows=1)
    maxV =  dataBase.iloc[0]['V1']
    maxI =  dataBase.iloc[0]['I1']

    # if DC analysis, the result is only on the 1st row
    if(mode.get() == 1):
        tkinter.messagebox.showinfo("Hasil Perhitungan I(R3)               ", "I(R3) = " + str(dataBase.iloc[0]['I3']) + " [A]")
    # if transient analysis, plot the graph and show it
    else:
        dataBase.plot(x = 'time', y = 'I3')
        plt.ylim(0, 1.1*maxI)
        plt.xlim(0)
        plt.title('Plot Arus I(R3) Terhadap Waktu (A)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("I(R3) (A)")
        plt.show()

def show_I4():
    dataBase = pd.read_csv("./HasilTracking.txt", delimiter=" \t", engine="python", skiprows=1)
    maxV =  dataBase.iloc[0]['V1']
    maxI =  dataBase.iloc[0]['I1']

    # if DC analysis, the result is only on the 1st row
    if(mode.get() == 1):
        tkinter.messagebox.showinfo("Hasil Perhitungan I(R4)               ", "I(R4) = " + str(dataBase.iloc[0]['I4']) + " [A]")
    # if transient analysis, plot the graph and show it
    else:
        dataBase.plot(x = 'time', y = 'I4')
        plt.ylim(0, 1.1*maxI)
        plt.xlim(0)
        plt.title('Plot Arus I(R4) Terhadap Waktu (A)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("I(R4) (A)")
        plt.show()

def show_Ic():
    dataBase = pd.read_csv("./HasilTracking.txt", delimiter=" \t", engine="python", skiprows=1)
    maxV =  dataBase.iloc[0]['V1']
    maxI =  dataBase.iloc[0]['I1']

    # if DC analysis, the result is only on the 1st row
    if(mode.get() == 1):
        tkinter.messagebox.showinfo("Hasil Perhitungan Ic               ", "Ic = " + str(dataBase.iloc[0]['Ic']) + " [A]")
    # if transient analysis, plot the graph and show it
    else:
        dataBase.plot(x = 'time', y = 'Ic')
        plt.ylim(0, 1.1*maxI)
        plt.xlim(0)
        plt.title('Plot Arus Ic Terhadap Waktu (A)')
        plt.xlabel("Waktu (s)")
        plt.ylabel("Ic (A)")
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

button_I1 = tk.Button(root, text="I(R1)", font=("Helvetica", 12, "bold"), command=show_I1, width=31, state="disabled")
button_I1.place(x=900, y=310)

button_I2 = tk.Button(root, text="I(R2)", font=("Helvetica", 12, "bold"), command=show_I2, width=31, state="disabled")
button_I2.place(x=900, y=345)

button_I3 = tk.Button(root, text="I(R3)", font=("Helvetica", 12, "bold"), command=show_I3, width=31, state="disabled")
button_I3.place(x=900, y=380)

button_I4 = tk.Button(root, text="I(R4)", font=("Helvetica", 12, "bold"), command=show_I4, width=31, state="disabled")
button_I4.place(x=900, y=415)

button_Ic = tk.Button(root, text="Ic", font=("Helvetica", 12, "bold"), command=show_Ic, width=31, state="disabled")
button_Ic.place(x=900, y=450)

############################################################################################################

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