import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import cv2

from keras.models import load_model
model = load_model('./cat_n_dog.h5')
# model=None
classes = { 
    0:'its a cat',
    1:'its a dog',
}
#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Cats and Dogs Classification')
top.configure(background='#CDCDCD')
label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = cv2.imread(file_path,1)
    pi=cv2.resize(image,(40,40))
    p=np.array(pi)
    p=p/255.0
    p=p.reshape((1,40,40,3))
    pr=model.predict(p)#[0.6,0.4] sum = 1
    clas=[np.argmax(e) for e in pr]
    ac=str(int(pr[0][clas[0]]*100))
    sign=classes[clas[0]] + " ("+ac+"%)"
    label.configure(foreground='#011638', text=sign) 

def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",
   command=lambda: classify(file_path),
   padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',
font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),
    (top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Cats and Dogs Classification",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()

top.mainloop()
