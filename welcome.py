from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound
import login


class WelcomeWindow:

    def __init__(self):
        self.win = Tk()
        self.canvas = Canvas(self.win, width=650, height=500, bg='#333438')
        self.canvas.pack(expand=YES, fill=BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "650x500+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)

        self.win.resizable(width=False, height=False)

        self.win.title("WELCOME! | Soccer ADMINISTRATOR")

    def add_frame(self):
        self.frame = Frame(self.win, height=490, width=640, bg='#333438')
        self.frame.place(x=4, y=4)
        x, y = 70, 20

        path1 = "messi.png"
        self.img1 = ImageTk.PhotoImage(Image.open(path1))
        self.label = Label(self.frame, image = self.img1, bg='#333438')
        self.label.place(x=x+400, y=y+290)

        path2 = "python2.png"
        self.img2 = ImageTk.PhotoImage(Image.open(path2))
        self.label = Label(self.frame, image = self.img2, bg='#333438')
        self.label.place(x=x+40, y=y+433)

        self.img3 = PhotoImage(file="fifa.png")
        self.label = Label(self.frame, image=self.img3, bg='#333438')
        self.label.place(x=0, y=0)

        path4 = "gangdu.png"
        self.img4 = ImageTk.PhotoImage(Image.open(path4))
        self.label = Label(self.frame, image=self.img4, bg='#333438')
        self.label.place(x=20, y=110)

        self.label = Label(self.frame, image=self.img4, bg='#333438')
        self.label.place(x=510, y=110)

        # self.img = PhotoImage(file="totoro.jpg")
        # self.label = Label(self.frame, image=self.img)
        # self.label.place(x=x+80, y=y+0)

        self.littlelabel = Label(self.frame, text='Written in')
        self.littlelabel.config(font=('넥슨 풋볼고딕 L', 20), fg='white', bg='#333438')
        self.littlelabel.place(x=x-60, y=y+430)

        self.labeltitle = Label(self.frame, text="예 측 해 축 ?")
        self.labeltitle.config(font=("넥슨 풋볼고딕 B", 70, 'bold'), fg='white', bg = '#333438')
        self.labeltitle.place(x=150, y=y+80)

        self.labelsub = Label(self.frame, text="  (    ͡°   ͜ʖ   ͡°   )  ")
        self.labelsub.config(font=("ariel", 30, 'bold'), fg='white', bg='#333438')
        self.labelsub.place(x=220, y=y + 175)

        self.button = Button(self.frame, text=" S T A R T ", font=('넥슨 풋볼고딕 B', 40), bd=0,
                             highlightbackground='#28292C', fg='white', command=self.login)      # 버튼 박스 색깔이 안바뀜
        self.button.place(x=x+150, y=y+270)
        self.win.mainloop()


    def login(self):
        self.win.destroy()
        log = login.LoginWindow()
        log.add_Frame()


if __name__ == "__main__":
    # playsound('legend.mp3', False)
    x = WelcomeWindow()
    x.add_frame()
