import tkinter as tk

from tkinter import messagebox
import time

#set value of n (no of pending approvals)
global n
n = 6


class Example(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)

        data = [
            
            [1,31324,"rfre", "rfre"],
            [2,45436,"ffre", "ffer"],[3,645658,"efrefer","fefe"],
            [4,457658,"hrthtrht", "ggrtg"],[5,4654768,"refgf", "rfre"],
            [6,4546,"gbr", "gfdvd"]
            ]


        self.photo = tk.PhotoImage(file="assets\\admin_bg.png")
        self.grid_columnconfigure(1, weight=1)


        tk.Label(self,
                text="Sr. No",
                fg="#FFFFFF",
                padx=30, 
                font=("yu gothic ui bold", 20 * -1),
                bg="#000000").grid(row=0, column=0, sticky="ew")
        

        tk.Label(self,
                text="Report ID",
                fg="#FFFFFF",
                padx=30, 
                font=("yu gothic ui bold", 20 * -1),
                bg="#000000").grid(row=0, column=1, sticky="ew")
        
        tk.Label(self, 
                text="Reported By   ",
                padx=30,
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#000000").grid(row=0, column=2, sticky="ew")
        

        tk.Label(self,
                text="         Reported To          ",
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#000000").grid(row=0, column=3, sticky="ew")

        tk.Label(self,
                text="  Message  ",
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#000000").grid(row=0, column=4, sticky="ew")

        row = 1

        for (nr, report_id, reported_by, reported_to) in data:
          
            nr_label = tk.Label(self,text=str(nr),
                                fg="#FFFFFF",
                                font=("yu gothic ui bold", 20 * -1),
                                bg="#000000")

            report_id_label = tk.Label(self, 
                                  text=str(report_id),
                                  fg="#FFFFFF",
                                  font=("yu gothic ui bold", 20 * -1),
                                  bg="#000000")

            reported_by_label = tk.Label(self, 
                                  text=str(reported_by),
                                  fg="#FFFFFF",
                                  font=("yu gothic ui bold", 20 * -1),
                                  bg="#000000")



            reported_to_label = tk.Label(self, 
                                  text=str(reported_to),
                                  fg="#FFFFFF",
                                  font=("yu gothic ui bold", 20 * -1),
                                  bg="#000000")



            buttonImage1 = tk.PhotoImage(file="assets\\message_resize.png")
            action_button1 = tk.Button(self,
                                      image=buttonImage1,
                                      borderwidth=0,
                                      highlightthickness=0,
                                      relief="flat",
                                      activebackground="#272A37",
                                      cursor="hand2"
                                      )
            action_button1.image=buttonImage1
            
          

            nr_label.grid(row=row, column=0, sticky="ew")
            report_id_label.grid(row=row, column=1, sticky="ew")
            reported_by_label.grid(row=row, column=2, sticky="ew")
            reported_to_label.grid(row=row, column=3, sticky="ew")
            action_button1.grid(row=row, column=4, sticky="ew")

            row += 1
      



if __name__ == "__main__":
    root = tk.Tk()
    
    height = (n)*38 + 35
    width = 1240
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 4) - (height // 4)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    root.configure(bg="#525561")


    Example(root).pack(side="top", fill="both", expand=True, padx=10, pady=10)


    root.mainloop()