from tkinter import *
from tkinter import messagebox

window = Tk()

height = 650
width = 1240
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.configure(bg="#525561")

# ================Background Image ====================
backgroundImage = PhotoImage(file="assets\\institute_view_docs_bg.png")
bg_image = Label(
    window,
    image=backgroundImage,
    bg="#525561"
)
bg_image.place(x=0, y=0)


# ================ Header Text Left ====================
headerText_image_left = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label1 = Label(
    bg_image,
    image=headerText_image_left,
    bg="#000000"
)
headerText_image_label1.place(x=60, y=45)

headerText1 = Label(
    bg_image,
    text="View Your Documents",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#000000"
)
headerText1.place(x=110, y=45)


# ================ Line x1 ====================
image2 = PhotoImage(file="assets\\line.png")
image2_Label = Label(
    bg_image,
    image=image2,
    bg="#272A37"
)
image2_Label.place(x=120, y=120)


# ================ Label 1 ====================
image1 = PhotoImage(file="assets\\email.png")
image1_Label = Label(
    bg_image,
    image=image1,
    bg="#000000"
)
image1_Label.place(x=60, y=170)

Label1_text = Label(
    image1_Label,
    text=" Personal Documents",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 23),
    bg="#3d404b"
)
Label1_text.place(x=25, y=0)

# -        ------------ BUTTON 1 ------------- -         

buttonImage1 = PhotoImage(file="assets\\student_view.png")
action_button1 = Button(window,
image=buttonImage1,
borderwidth=0,
highlightthickness=0,
relief="flat",
activebackground="#272A37",
cursor="hand2"
)
action_button1.image=buttonImage1
action_button1.place(x=550, y=175)
            
# ================ Line x2 ====================
image3 = PhotoImage(file="assets\\line.png")
image3_Label = Label(
    bg_image,
    image=image2,
    bg="#272A37"
)
image3_Label.place(x=120, y=280)

# ================ Label 2 ====================

image4_Label = Label(
    bg_image,
    image=image1,
    bg="#000000"
)
image4_Label.place(x=60, y=340)

Label2_text = Label(
    image4_Label,
    text="        Marksheets",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 23),
    bg="#3d404b"
)
Label2_text.place(x=25, y=0)

# -        ------------ BUTTON 2 ------------- -         


action_button2 = Button(window,
image=buttonImage1,
borderwidth=0,
highlightthickness=0,
relief="flat",
activebackground="#272A37",
cursor="hand2"
)
action_button2.image=buttonImage1
action_button2.place(x=550, y=345)
            
# ================ Line x3 ====================
image5 = PhotoImage(file="assets\\line.png")
image5_Label = Label(
    bg_image,
    image=image2,
    bg="#272A37"
)
image5_Label.place(x=120, y=455)

# ================ Label 3 ====================

image5_Label = Label(
    bg_image,
    image=image1,
    bg="#000000"
)
image5_Label.place(x=60, y=520)


Label3_text = Label(
    image5_Label,
    text="         Certificates",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 23),
    bg="#3d404b"
)
Label3_text.place(x=25, y=0)


# -        ------------ BUTTON 2 ------------- -         


action_button3 = Button(window,
image=buttonImage1,
borderwidth=0,
highlightthickness=0,
relief="flat",
activebackground="#272A37",
cursor="hand2"
)
action_button3.image=buttonImage1
action_button3.place(x=550, y=525)
     


window.resizable(False, False)
window.mainloop()
