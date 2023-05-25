from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt
import PoseEstimationCurl as curl
root=Tk()
root.title('Sanjay.com')
root.iconbitmap('')
root.geometry("400x200")

def graph():
    lAngle=curl.left_angle
    rAngle=curl.counts
    plt.plot(lAngle,rAngle)
    plt.show()
my_Btn=Button(root,text="Graph It!",command=graph)
my_Btn.pack()
root.mainloop()