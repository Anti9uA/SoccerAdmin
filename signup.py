from tkinter import *
from tkinter import messagebox
import db.db
import login
import board

class signupWindow:
    def __init__(self):
        self.win = Tk()
        self.canvas = Canvas(self.win, width=600, height=400, bg='#333438')
        self.canvas.pack(expand=YES, fill=BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        self.win.resizable(width=False, height=False)

        self.win.title("WELCOME! | Soccer ADMINISTRATOR")

    def add_Frame(self):
        self.frame = Frame(self.win, height=392, width=592, bg='#333438')
        self.frame.place(x=4, y=4)
        x, y = 70, 20

        self.label = Label(self.frame, text="회원가입", fg='white', bg='#333438')
        self.label.config(font=("Koverwatch", 60, 'bold'))
        self.label.place(x=x + 140, y=y + 30)

        self.elabel = Label(self.frame, text="new email", fg='white', bg='#333438')
        self.elabel.config(font=("Koverwatch", 30, 'bold'))
        self.elabel.place(x=120, y=y + 128)

        self.email = Entry(self.frame, font=('arial 12', 12), bd=0)
        self.email.place(x=260, y=y + 130)

        self.idlabel = Label(self.frame, text="new ID", fg='white', bg='#333438')
        self.idlabel.config(font=("Koverwatch", 30, 'bold'))
        self.idlabel.place(x=120, y=y + 180)

        self.id = Entry(self.frame, font=('arial 12', 12), bd=0)
        self.id.place(x=260, y=y + 180)

        self.pwlabel = Label(self.frame, text="new p.w", fg='white', bg='#333438')
        self.pwlabel.config(font=("Koverwatch", 30, 'bold'))
        self.pwlabel.place(x=120, y=y + 230)

        self.password = Entry(self.frame, show='*', font=('arial 12', 12), bd=0)
        self.password.place(x=260, y=y + 230)

        self.button = Button(self.frame, text=" Sign Up ", font='Koverwatch 30', bd=0,
                             highlightbackground='#28292C', command=self.signup)
        self.button.place(x=250, y=y + 290)

        self.backbutton = Button(self.frame, text=" back ", font='Koverwatch 20', bd=0, fg='black',
                                 highlightbackground='#28292C', command=self.back)
        self.backbutton.place(x=x - 50, y=y)

        self.canvas.mainloop()

    def signup(self):
        data = (self.email.get(), self.id.get(), self.password.get())
        if self.email.get() == "":
            messagebox.showinfo(title="ERROR", message="이메일을 입력해주세요!!")
        elif self.id.get() == "":
            messagebox.showinfo(title="ERROR", message="ID를 입력해주세요!!")
        elif self.password.get() == "":
            messagebox.showinfo(title="ERROR", message="비밀번호를 입력해주세요!!")
        else:
            reg = db.db.user_signup(data)
            if reg:
                messagebox.showinfo("알림", "환영해요!\n회원가입이 완료되었습니다.")
                self.win.destroy()
                log = login.LoginWindow()
                log.add_Frame()
            else:
                messagebox.showinfo(title="ERROR", message="이미 존재하는 ID입니다..",icon = 'warning')


    def back(self):
        self.win.destroy()
        log = login.LoginWindow()
        log.add_Frame()

