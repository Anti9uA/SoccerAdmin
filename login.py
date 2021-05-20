from tkinter import *
from tkinter import messagebox
import db.db
import board
import signup
import finder
import mainBoard


class LoginWindow:
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

        self.label = Label(self.frame, text="로그인", fg='white', bg='#333438')
        self.label.config(font=("Koverwatch",60,'bold'))
        self.label.place(x=x+160, y=y+30)

        self.idlabel = Label(self.frame, text="ID", fg='white', bg='#333438')
        self.idlabel.config(font=("Koverwatch",30,'bold'))
        self.idlabel.place(x=168, y=y+128)

        self.id = Entry(self.frame, font=('arial 12', 12), bd=0)
        self.id.place(x=220, y=y+135)

        self.pwlabel = Label(self.frame, text="P.W", fg='white', bg='#333438')
        self.pwlabel.config(font=("Koverwatch", 30, 'bold'))
        self.pwlabel.place(x=160, y=y + 190)

        self.password = Entry(self.frame, show='*', font=('arial 12', 12), bd=0)
        self.password.place(x=220, y=y + 195)

        self.button = Button(self.frame, text="  Login  ", font='Koverwatch 30', bd=0,
                             highlightbackground='#28292C', command=self.login)
        self.button.place(x=x+183, y=y+260)

        self.slabel = Label(self.frame, text="회원이 아니신가요?", fg='white', bg='#333438')
        self.slabel.config(font=("Koverwatch", 20, 'bold'))
        self.slabel.place(x=x+315, y=y + 335)

        self.signupButton = Button(self.frame, text='  sign up  ', font='Koverwatch 20',
                                   highlightbackground='#28292C',command=self.signUp)
        self.signupButton.place(x=x+440, y=y+335)

        self.idfindButton = Button(self.frame, text=' ID 찾기 ', font='Koverwatch 20',
                                   highlightbackground='#28292C',command=self.find_ID)
        self.idfindButton.place(x=x-50, y=y+280)

        self.pwfindButton = Button(self.frame, text='P.W 찾기', font='Koverwatch 20',
                                   highlightbackground='#28292C', command=self.find_PW)
        self.pwfindButton.place(x=x-50, y=y+320)

        self.win.mainloop()

    def find_ID(self):
        self.win.destroy()
        find = finder.ID_finder()
        find.add_Frame()

    def find_PW(self):
        self.win.destroy()
        find = finder.PW_finder()
        find.add_Frame()


    def signUp(self):
        self.win.destroy()
        log = signup.signupWindow()
        log.add_Frame()


    def login(self):
        data = (self.id.get(), self.password.get())
        if self.id.get() == "":
            messagebox.showinfo(title="ERROR", message="ID를 입력해주세요!!", icon = 'warning')
        elif self.password.get() == "":
            messagebox.showinfo(title="ERROR", message="비밀번호를 입력해주세요!!", icon = 'warning')
        else:
            reg = db.db.user_login(data)
            if reg:
                messagebox.showinfo("Message", "정상적으로 로그인되었습니다.")
                self.get_id()
                self.win.destroy()
                m = mainBoard.MainWindow()
                m.add_Frame()
            else:
                messagebox.showinfo(title="ERROR", message="ID나 비밀번호가 다릅니다!", icon = 'warning')

    def get_id(self):
        global save
        save = self.id.get()

    def return_id(self):
        return save
