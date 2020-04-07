import tkinter as tk

# make a new window
win = tk.Tk()
# write the window title
win.title("Testing GUI")
# change the window size
screen_x = win.winfo_screenwidth()
screen_y = win.winfo_screenheight()
# win.geometry("{0}x{1}+0+0".format(screen_x, screen_y))
win.geometry("800x600")
win.resizable(False, False)
# make the window zoomed (max size, fit to screen)
# win.state("zoomed")
# insert background image name to a variable
background_image = tk.PhotoImage(file="rangkaian_tubes.png")
# make a label for the image
background_label = tk.Label(win, image=background_image)
# put the image label at the corner left
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.pack(fill="both", expand="yes")
# create a text label
label1 = tk.Label(win, text="Screen width = {}".format(screen_x), pady=5)
# put the label using pack
label1.pack(side="top", expand="yes", fill="both")
label2 = tk.Label(win, text="Screen height = {}".format(screen_y), pady=5)
label2.pack(side="top")
# loop the window until closed
win.mainloop()