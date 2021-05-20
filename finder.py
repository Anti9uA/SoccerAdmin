from tkinter import *
from tkinter import messagebox
import db.db
import login
import smtplib
from email.mime.text import MIMEText


class ID_finder:
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

        self.label = Label(self.frame, text="ID 찾기", fg='white', bg='#333438')
        self.label.config(font=("Koverwatch", 60, 'bold'))
        self.label.place(x=x + 150, y=y + 30)

        self.elabel = Label(self.frame, text="이메일", fg='white', bg='#333438')
        self.elabel.config(font=("Koverwatch", 20, 'bold'))
        self.elabel.place(x=150, y=y + 128)

        self.email = Entry(self.frame, font=('arial 12', 12), bd=0)
        self.email.place(x=230, y=y + 130)


        self.button = Button(self.frame, text=" ID 조회하기 ", font='Koverwatch 30', bd=0,
                             highlightbackground='#28292C', command=self.checkID)
        self.button.place(x=x + 155, y=y + 240)

        self.backbutton = Button(self.frame, text=" back ", font='Koverwatch 20', bd=0, fg='black',
                             highlightbackground='#28292C', command=self.back)
        self.backbutton.place(x=x-50, y=y)


    def checkID(self):
        data = self.email.get()
        reg = db.db.check_ID(data)
        if self.email.get() == "":
            messagebox.showinfo(title="ERROR", message="이메일을 입력해주세요!!")
        if reg:
            # reg 다음에 문자열을 출력하고 싶은데 튜플 오류가 뜸...
            print(reg)
            messagebox.showinfo("Message", reg[0]+"입니다.")
            self.win.destroy()
            log = login.LoginWindow()
            log.add_Frame()
        else:
            messagebox.showinfo("Message", "해당 ID가 없습니다..ㅠㅠ")


    def back(self):
        self.win.destroy()
        log = login.LoginWindow()
        log.add_Frame()


class PW_finder:
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

        self.label = Label(self.frame, text="PW 찾기", fg='white', bg='#333438')
        self.label.config(font=("Koverwatch", 60, 'bold'))
        self.label.place(x=x + 130, y=y + 30)

        self.elabel = Label(self.frame, text="이메일", fg='white', bg='#333438')
        self.elabel.config(font=("Koverwatch", 20, 'bold'))
        self.elabel.place(x=120, y=y + 140)

        self.email = Entry(self.frame, font=('arial 12', 15), bd=0)
        self.email.place(x=200, y=y + 150)

        self.idlabel = Label(self.frame, text="ID", fg='white', bg='#333438')
        self.idlabel.config(font=("Koverwatch", 25, 'bold'))
        self.idlabel.place(x=153, y=y + 200)

        self.id = Entry(self.frame, font=('arial 12', 15), bd=0)
        self.id.place(x=200, y=y + 210)

        self.button = Button(self.frame, text=" P.W 조회하기 ", font='Koverwatch 30', bd=0,
                             highlightbackground='#28292C', command=self.checkPW)
        self.button.place(x=x + 135, y=y + 260)

        self.backbutton = Button(self.frame, text=" back ", font='Koverwatch 20', bd=0, fg='black',
                                 highlightbackground='#28292C', command=self.back)
        self.backbutton.place(x=x - 50, y=y)

    def checkPW(self):
        data = (self.email.get(), self.id.get())
        reg = db.db.check_PW(data)
        if self.email.get() == "":
            messagebox.showinfo(title="ERROR", message="이메일을 입력해주세요!!")
        elif self.id.get() == "":
            messagebox.showinfo(title="ERROR", message="ID를 입력해주세요!!")
        if reg:
            self.info = reg
            self.send()
            messagebox.showinfo("Message", "등록하신 이메일로 PW 정보가 전송되었습니다!")
            self.win.destroy()
            log = login.LoginWindow()
            log.add_Frame()
        else:
            messagebox.showinfo("Message", "해당 ID가 없습니다..ㅠㅠ")

    def send(self):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('didlaak6000@gmail.com', '') # 본인 gmail 아이디 비밀번호 치시면 됩니다
        msg = MIMEText(self.info[0], 'utf-8')
        msg['To'] = self.email.get()
        s.sendmail("didlaak6000@gmail.com", self.email.get(), self.info[0])
        s.quit()

    def back(self):
        self.win.destroy()
        log = login.LoginWindow()
        log.add_Frame()