from tkinter import * 

class CAlc:
    def __init__(self, root):
        self.root = root
        root.geometry("360x560")
        root.resizable(False, False)
        root.title("Calculator")
        self.enter = Entry(root ,foreground="#FFFFFF",font = ('Helvetica', 23),
                           borderwidth=10, relief="flat", background='#2F3332')
        self.enter.place(x=1, y=58, width=350, height=50)
        self.c_button()
        root.configure(background='#2F3332')
        
    def c_button(self):
        button = ["1", "2", "3","-",
                  "4", "5", "6","+",
                  "7", "8", "9","*",
                  "0", ".", "C","/",
                  "(", ")", "BACK","="]
        
        r = 108
        c = 0

        for i in button:
            if i == "=":
                but = Button(self.root, text = i, foreground="#FFFFFF", font=("Helvetica", 30),background="#101720"
                             ,relief="flat",overrelief="solid", padx = 5, pady = 0,command=self.exect)
            elif i == "BACK":
                but = Button(self.root, text = i,foreground="#4d4c4b",font=("Helvetica", 15, "bold"),background="#fca103",
                             relief="flat", overrelief="solid",padx = 5, pady = 0, command=self.back)
            elif i == "C":
                but = Button(self.root, text = i, foreground="#4d4c4b",font=("Helvetica", 30),background="#fca103", 
                             relief="flat", overrelief="solid",padx = 5, pady = 0, command=self.clear)
            elif i=="*":
                but = Button(self.root, text = "×", foreground="#4d4c4b",font=("Helvetica", 30),background="#fca103",
                             relief="flat", overrelief="solid",padx = 5, pady = 0, command=lambda a=i:self.pri_ent(a))
            else:
                but = Button(self.root, text = i, foreground="#4d4c4b",font=("Helvetica", 30),background="#fca103", 
                             relief="flat", overrelief="solid",padx = 5, pady = 0, command=lambda a=i:self.pri_ent(a))

            but.place(x=c,y=r, height = 45.2*2, width=45.2*2)
            c+=90.19
            if c > 271.2 : 
                c=0 
                r+=90.14
        
    def pri_ent(self,val):
        pre = self.enter.get()
        self.enter.delete(0, END)
        self.enter.insert(0,pre+val)
    
    def clear(self):
        self.enter.delete(0, END)
    
    def back(self):
        pre = self.enter.get()
        self.enter.delete(len(pre)-1, len(pre))
    
    def exect(self):
        try:
            pre = self.enter.get()
            self.enter.delete(0, END)
            self.enter.insert(0,eval(pre))

        except Exception:
            self.enter.delete(0, END)
            self.enter.insert(0, f"Error")

if __name__=="__main__":
    root = Tk()
    CAlc(root)
    root.mainloop()