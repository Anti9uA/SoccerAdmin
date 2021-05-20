from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time as tm
import login
import webbrowser





class MainWindow:
    def __init__(self):
        self.win = Tk()

        self.canvas = Canvas(self.win, width=900, height=800, bg='#333438')
        self.canvas.pack(expand=YES, fill=BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 900 / 2)
        y = int(height / 2 - 600 / 2)
        str1 = "900x800+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)

        self.win.resizable(width=False, height=False)

        self.win.title("main! | Soccer ADMINISTRATOR")


    def add_Frame(self):
        x, y = 70, 20

        self.frame = Canvas(self.canvas, width=892, height=40, bg="#202124", bd=0, highlightthickness=0)
        self.frame.place(x=3,y=3)

        # self.frame_match_up = Canvas(self.canvas, width=380, height=300, bg='#333438')
        # self.frame_match_up["relief"] = 'solid'
        # self.frame_match_up.place(x=490, y=450)

        self.rankframe=Canvas(self.canvas, width=500, height=400, bg="#202124", bd=1)
        self.frame.place()
        self.usrlabel = Label(self.canvas, text=self.view()+"님 환영합니다!", font=('넥슨 풋볼고딕 L', 20), fg='white', bg='#202124')
        self.usrlabel.place(x=x-25, y=y-15)

        self.naversportsurl = "https://sports.news.naver.com/wfootball/index.nhn"
        self.protourl = "https://www.sportstoto.co.kr/dividend_rate_frame.php?f_id=soccer"
        self.linklabel = Label(self.canvas, text='네이버 스포츠 바로가기', font=('Koverwatch',20), fg = 'white', bg = '#202124')
        self.linklabel.place(x=x+120, y=y+749)
        self.linklabel.bind("<Button-1>", lambda e: self.callback1())

        self.linklabel = Label(self.canvas, text='축구 토토 바로가기', font=('Koverwatch', 20), fg='white', bg='#202124')
        self.linklabel.place(x=x-30, y=y+749)
        self.linklabel.bind("<Button-1>", lambda e: self.callback2())

        self.clocklabel = Label(self.canvas, font=('넥슨 풋볼고딕 L', 20), fg = 'white', bg = '#202124')
        self.clocklabel.grid(row=0, column=0)
        self.clocklabel.place(x=x+600, y=y-15)
        self.display_time()

        self.combocanvas = Canvas(self.canvas, width=350, height=50, bg = '#333438')
        self.combocanvas.place(x=40, y=50)

        self.myteam = StringVar()
        self.combo = ttk.Combobox(self.combocanvas, width=10, textvariable=self.myteam)
        self.combo['values'] = ('EPL', '라리가', '분데스리가','세리에A')
        self.combo.current(0)
        self.combo.grid(row=0, column=0)
        self.combo.place(x=x+50, y=15)

        self.button = ttk.Button(self.combocanvas, text='선택', width=3, command=self.changeteam)
        self.button.place(x=x+200, y=18)

        self.label = Label(self.combocanvas, text='리그 선택', fg='white', bg='#333438')
        self.label.config(font=("넥슨 풋볼고딕 B", 25, 'bold'))
        self.label.place(x=3, y=8)

        self.label = Label(self.canvas, text= '순위표', fg='white', bg='#333438')
        self.label.config(font=("Koverwatch", 60, 'bold'))
        self.label.place(x=x-25, y=y+140)

        self.label = Label(self.canvas, text='승부 예측!', fg='white', bg='#333438')
        self.label.config(font=("Koverwatch", 60, 'bold'))
        self.label.place(x=477, y=y+40)

        self.label = Label(self.canvas, text='경기 조회', fg='white', bg='#333438')
        self.label.config(font=("Koverwatch", 60, 'bold'))
        self.label.place(x=420, y=y + 330)

        self.date=StringVar()
        self.combo = ttk.Combobox(self.canvas, width=10, textvariable=self.date)
        self.combo['values'] = ('어제', '오늘', '내일')
        self.combo.current(1)
        self.combo.grid(row=0, column=0)
        self.combo.place(x=620, y=380)

        self.datebutton = ttk.Button(self.canvas, text='선택', width=3, command=self.dateapply)
        self.datebutton.place(x=750, y=385)



        self.logoutbutton = Button(self.canvas, text=" 로그아웃 ", font='Koverwatch 20', bd=0, fg='black',
                                 highlightbackground='#28292C', command=self.logout)
        self.logoutbutton.place(x=x+150, y=y-10)

        self.match_up_view()

        self.resultframe = Canvas(self.canvas, width=380, height=100, bg="#333438")
        self.resultframe.place(x=490, y=200)

        self.rank_view()

        self.teamvsbox()




    def dateapply(self):
        if self.date.get() == "오늘":
            self.frame_match_up.destroy()
            self.match_up_view()
        elif self.date.get() == "내일":
            self.frame_match_up.destroy()
            self.tomorrow_match_up_view()
        else:
            self.frame_match_up.destroy()
            self.yesterday_match_up_view()


    def apply(self):
        self.resultframe.destroy()
        self.resultframe = Canvas(self.canvas, width=380, height=100, bg="#333438")
        self.resultframe.place(x=490, y=200)
        self.closer_shoot(self.myteam2.get(), self.myteam3.get(), self.myteam.get())

    def teamvsbox(self):
        self.frame_team = Frame(self.canvas, width=500, height=50, bg='#333438')
        self.frame_team["relief"] = 'solid'
        self.frame_team.place(x=390, y=150)

        self.vslabel=Label(self.frame_team, text='V S', fg='white', bg='#333438')
        self.vslabel.config(font=('Koverwatch', 30))
        self.vslabel.place(x=240,y=-2)

        if self.myteam.get() == "EPL":
            self.myteam2 = StringVar()
            self.combo2 = ttk.Combobox(self.frame_team, width=10, textvariable=self.myteam2)  # asdf
            self.combo2['values'] = ('리버풀', '맨시티', '레스터', '첼시', '맨유', '울버햄튼', '셰필드', '토트넘', '팰리스',
                                     '아스널', '에버턴', '뉴캐슬', '사우샘프턴', '번리', '브라이튼', '웨스트햄',
                                     '왓포드', '아스톤', '본머스', '노리치')
            self.combo2.current(0)
            self.combo2.grid(row=0, column=0)
            self.combo2.place(x=100, y=0)
            self.myteam3 = StringVar()

            self.combo3 = ttk.Combobox(self.frame_team, width=10, textvariable=self.myteam3)  # asdf
            self.combo3['values'] = ('리버풀', '맨시티', '레스터', '첼시', '맨유', '울버햄튼', '셰필드', '토트넘', '팰리스',
                                     '아스널', '에버턴', '뉴캐슬', '사우샘프턴', '번리', '브라이튼', '웨스트햄',
                                     '왓포드', '아스톤', '본머스', '노리치')
            self.combo3.current(0)
            self.combo3.grid(row=0, column=0)
            self.combo3.place(x=300, y=0)

            self.combutton = ttk.Button(self.canvas, text='선택', width=3, command=self.apply)
            self.combutton.place(x=820, y=150)

        elif self.myteam.get() == "라리가":
            self.myteam2 = StringVar()
            self.combo2 = ttk.Combobox(self.frame_team, width=10, textvariable=self.myteam2)  # asdf
            self.combo2['values'] = ('바르셀로나', '레알 마드리드', 'AT 마드리드', '세비야', '헤타페', '레알 소시에다드', '발렌시아', '아틀레틱', '비야레알',
                                     '그라나다', '레알 베티스', '레반테', '오사수나', '알라베스', '레알 바야돌리드', '에이바르',
                                     '마요르카', '레가네스', '셀카 데 비고', '에스파뇰')
            self.combo2.current(0)
            self.combo2.grid(row=0, column=0)
            self.combo2.place(x=100, y=0)

            self.myteam3 = StringVar()
            self.combo3 = ttk.Combobox(self.frame_team, width=10, textvariable=self.myteam3)  # asdf
            self.combo3['values'] = ('바르셀로나', '레알 마드리드', 'AT 마드리드', '세비야', '헤타페', '레알 소시에다드', '발렌시아', '아틀레틱', '비야레알',
                                     '그라나다', '레알 베티스', '레반테', '오사수나', '알라베스', '레알 바야돌리드', '에이바르',
                                     '마요르카', '레가네스', '셀타 데 비고', '에스파뇰')
            self.combo3.current(0)
            self.combo3.grid(row=0, column=0)
            self.combo3.place(x=300, y=0)

            self.combutton = ttk.Button(self.canvas, text='선택', width=3, command=self.apply)
            self.combutton.place(x=820, y=150)


        elif self.myteam.get() == '분데스리가':

            self.myteam2 = StringVar()
            self.combo2 = ttk.Combobox(self.frame_team, width=10, textvariable=self.myteam2)  # asdf
            self.combo2['values'] = ('라이프치히', '바이에른 뮌헨', '묀헨글라트바흐', '도르트문트', '샬케 04', '레버쿠젠', '프라이부르크', '호펜하임', '볼프스부르크',
                                     '아우크스부르크', '프랑크푸르트', '레반테', '베를린', '쾰른', '헤르타', '마인츠',
                                     '브레멘', '뒤셀도르프', '파더보른')
            self.combo2.current(0)
            self.combo2.grid(row=0, column=0)
            self.combo2.place(x=100, y=0)

            self.myteam3 = StringVar()
            self.combo3 = ttk.Combobox(self.frame_team, width=10, textvariable=self.myteam3)  # asdf
            self.combo3['values'] = ('라이프치히', '바이에른 뮌헨', '묀헨글라트바흐', '도르트문트', '샬케 04', '레버쿠젠', '프라이부르크', '호펜하임', '볼프스부르크',
                                     '아우크스부르크', '프랑크푸르트', '레반테', '베를린', '쾰른', '헤르타', '마인츠',
                                     '브레멘', '뒤셀도르프', '파더보른')
            self.combo3.current(0)
            self.combo3.grid(row=0, column=0)
            self.combo3.place(x=300, y=0)

            self.combutton = ttk.Button(self.canvas, text='선택', width=3, command=self.apply)
            self.combutton.place(x=820, y=150)

        else:
            self.myteam2 = StringVar()
            self.combo2 = ttk.Combobox(self.frame_team, width=10, textvariable=self.myteam2)  # asdf
            self.combo2['values'] = ('유벤투스', '인테르', '라치오', '로마', '아탈란타', '칼리아리', '파르마 칼초', 'AC 밀란', '토리노',
                                     '베로나', '나폴리', '볼로냐', '피오렌티나', '우디네세', '사수올로', '삼프도리아',
                                     '레체', '브레시아', '제노아', 'SPAL')
            self.combo2.current(0)
            self.combo2.grid(row=0, column=0)
            self.combo2.place(x=100, y=0)

            self.myteam3 = StringVar()
            self.combo3 = ttk.Combobox(self.frame_team, width=10, textvariable=self.myteam3)  # asdf
            self.combo3['values'] = ('유벤투스', '인테르', '라치오', '로마', '아탈란타', '칼리아리', '파르마 칼초', 'AC 밀란', '토리노',
                                     '베로나', '나폴리', '볼로냐', '피오렌티나', '우디네세', '사수올로', '삼프도리아',
                                     '레체', '브레시아', '제노아', 'SPAL')
            self.combo3.current(0)
            self.combo3.grid(row=0, column=0)
            self.combo3.place(x=300, y=0)

            self.combutton = ttk.Button(self.canvas, text='선택', width=3, command=self.apply)
            self.combutton.place(x=820, y=150)

    def callback1(self):
        webbrowser.open_new(self.naversportsurl)

    def callback2(self):
        webbrowser.open_new(self.protourl)

    def view(self):
        log = login.LoginWindow()
        return log.return_id()

    def logout(self):
        msg = messagebox.askquestion('알림','정말 로그아웃 하시겠어요??',icon = 'warning')
        if msg == 'yes':
            messagebox.showinfo("알림", "정상적으로 로그아웃 되었습니다.")
            self.win.destroy()
            log = login.LoginWindow()
            log.add_Frame()
        else:
            messagebox.showinfo("알림", "로그아웃이 취소되었습니다.")

    def rank_view(self):
        self.frame_rank = Canvas(self.canvas, width=300, height=340, bg='#333438', bd=1, )
        self.frame_rank["relief"] = 'solid'
        self.frame_rank.place(x=45, y=230)

        self.labeltitle = Label(self.frame_rank, text=self.rank(), justify="left")
        self.labeltitle.config(font=("넥슨 풋볼고딕 L", 25), fg='white', bg='#333438',bd=1)
        self.labeltitle.place(x=3, y=3)

    def changeteam(self):
        # messagebox.showinfo(title="Message", message=self.myteam.get()+"로 리그가 바뀝니다.")
        self.frame_rank.destroy()
        self.frame_team.destroy()
        self.rank_view()
        self.teamvsbox()

    def display_time(self):
        self.current_time = tm.strftime(' %m월 %d일 (%a) %I:%M ')
        self.clocklabel['text'] = self.current_time
        self.canvas.after(1000, self.display_time)

    def rank(self):
        if self.myteam.get() == "EPL":
            html = requests.get('https://sports.news.naver.com/wfootball/index.nhn')
            soup = BeautifulSoup(html.text, 'html.parser')
            divs_epl = soup.find('div', {'id': '_team_rank_epl'})
            lis_epl = divs_epl.findAll('div', {'class': 'info'})
            view_list_epl = list()
            n = 1
            for team in lis_epl:
                team = ('%d위\t' % n + team.text.strip())

                view_list_epl.append(team)
                n += 1
            epl_rank_str = '\n'.join(view_list_epl)  # 리스트를 str으로 변환  (return후 main의 label에서 text출력에 str넣기위해서

            return epl_rank_str

        elif self.myteam.get() == "라리가":
            html = requests.get('https://sports.news.naver.com/wfootball/index.nhn')
            soup = BeautifulSoup(html.text, 'html.parser')
            divs_lal = soup.find('div', {'id': '_team_rank_primera'})
            lis_lal = divs_lal.findAll('div', {'class': 'info'})
            view_list_lal = list()
            n = 1
            for team in lis_lal:
                team = ('%d위\t' % n + team.text.strip())

                view_list_lal.append(team)
                n += 1
            lal_rank_str = '\n'.join(view_list_lal)  # 리스트를 str으로 변환  (return후 main의 label에서 text출력에 str넣기위해서

            return lal_rank_str

        elif self.myteam.get() == "분데스리가":
            html = requests.get('https://sports.news.naver.com/wfootball/index.nhn')
            soup = BeautifulSoup(html.text, 'html.parser')
            divs_bds = soup.find('div', {'id': '_team_rank_bundesliga'})
            lis_bds = divs_bds.findAll('div', {'class': 'info'})
            view_list_bds = list()
            n = 1
            for team in lis_bds:
                team = ('%d위\t' % n + team.text.strip())

                view_list_bds.append(team)
                n += 1
            bds_rank_str = '\n'.join(view_list_bds)  # 리스트를 str으로 변환  (return후 main의 label에서 text출력에 str넣기위해서

            return bds_rank_str

        else:
            html = requests.get('https://sports.news.naver.com/wfootball/index.nhn')
            soup = BeautifulSoup(html.text, 'html.parser')
            divs_ser = soup.find('div', {'id': '_team_rank_seria'})
            lis_ser = divs_ser.findAll('div', {'class': 'info'})
            view_list_ser = list()
            n = 1
            for team in lis_ser:
                team = ('%d위\t' % n + team.text.strip())

                view_list_ser.append(team)
                n += 1
            ser_rank_str = '\n'.join(view_list_ser)

            return ser_rank_str

    def match_up_view(self):
        self.frame_match_up = Canvas(self.canvas, width=470, height=350, bg='#333438')
        self.frame_match_up["relief"] = 'solid'
        self.frame_match_up.place(x=400, y=430)

        self.labeltitle = Label(self.frame_match_up, text=self.match_up(), justify='left')
        self.labeltitle.config(font=("넥슨 풋볼고딕 L", 15), fg='white', bg='#333438', bd=1)
        self.labeltitle.place(x=25, y=3)

    def match_up(self):
        response_match = requests.get('https://sports.news.naver.com/wfootball/index.nhn')
        html_match = response_match.text

        match_list = list()
        score_list = list()
        state_list = list()
        soup_match = BeautifulSoup(html_match, 'html.parser')  # html.parser를 사용해서 soup에 넣겠다

        for match in soup_match.select('div.inner > span.name'):  # 팀이름 받아오기
            match_list.append(match.text.strip())

        for score in soup_match.select('.score'):  # 점수 받아오기
            score_list.append(score.text.strip())

        for state in soup_match.select(('div.state > div.inner')):  # 경기 상태
            state_list.append(state.text.strip())

        match_up_view = list()

        for x in range(len(state_list)):
            if ":" in state_list[x]:
                y = (match_list[x * 2 + 1].ljust(14) + '\t' + '-' + '\t' + state_list[x] + '\t' + '-' + match_list[
                    x * 2].rjust(15))

                match_up_view.append(y)


            else:
                y = (match_list[x * 2 + 1].ljust(14) + '\t' + score_list[x * 2] + '\t' + state_list[x] + '\t' +
                     score_list[x * 2 + 1] + match_list[x * 2].rjust(15))
                match_up_view.append(y)

            match_up_result = '\n\n'.join(match_up_view)  # 리스트에 \n하면서 str로

        return match_up_result

    def tomorrow_match_up_view(self):
        self.frame_match_up = Canvas(self.canvas, width=470, height=350, bg='#333438')
        self.frame_match_up["relief"] = 'solid'
        self.frame_match_up.place(x=400, y=430)

        self.labeltitle = Label(self.frame_match_up, text=self.tomorrow_match_up(), justify='left')
        self.labeltitle.config(font=("넥슨 풋볼고딕 B", 15), fg='white', bg='#333438')
        self.labeltitle.place(x=3, y=3)

    def tomorrow_match_up(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        # options.add_argument("disable-gpu")

        driver = webdriver.Chrome(
            executable_path='/Users/shimkyubo/Desktop/ToToro_mac/chromedriver',
            chrome_options=options)

        driver.get("https://sports.news.naver.com/wfootball/index.nhn")  # 창

        driver.find_element_by_xpath('//*[@id="_schedule_box"]/div/div[3]/span/a[2]').send_keys(Keys.ENTER)  # 내일클릭

        tm.sleep(0.1)  # 내일버튼클릭을 기다린 후 일정을 가져옴

        text = driver.page_source

        html_match = text  # selenium으로 받은 html을 bs의 html로 복사

        match_list = list()
        score_list = list()
        state_list = list()
        soup_match = BeautifulSoup(html_match, 'html.parser')  # html.parser를 사용해서 soup에 넣겠다

        for match in soup_match.select('div.inner > span.name'):  # 팀이름 받아오기
            match_list.append(match.text.strip())

        for score in soup_match.select('.score'):  # 점수 받아오기
            score_list.append(score.text.strip())

        for state in soup_match.select(('div.state > div.inner')):  # 경기 상태
            state_list.append(state.text.strip())

        match_up_view = list()

        for x in range(len(state_list)):
            if ":" in state_list[x]:
                y = (match_list[x * 2 + 1].ljust(14) + '\t' + '-' + '\t' + state_list[x] + '\t' + '-' + match_list[
                    x * 2].rjust(15))

                match_up_view.append(y)


            else:
                y = (match_list[x * 2 + 1].ljust(14) + '\t' + score_list[x * 2] + '\t' + state_list[x] + '\t' +
                     score_list[x * 2 + 1] + match_list[x * 2].rjust(15))
                match_up_view.append(y)
            match_up_result = '\n\n'.join(match_up_view)  # 리스트에 \n하면서 str로
        return match_up_result

    def yesterday_match_up_view(self):
        self.frame_match_up = Canvas(self.canvas, width=470, height=350, bg='#333438')
        self.frame_match_up["relief"] = 'solid'
        self.frame_match_up.place(x=400, y=430)

        self.labeltitle = Label(self.frame_match_up, text=self.yesterday_match_up(), justify='left')
        self.labeltitle.config(font=("넥슨 풋볼고딕 B", 15), fg='white', bg='#333438')
        self.labeltitle.place(x=3, y=3)

    def yesterday_match_up(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        # options.add_argument("disable-gpu")

        driver = webdriver.Chrome(
            executable_path='/Users/shimkyubo/Desktop/ToToro_mac/chromedriver',
            chrome_options=options)

        driver.get("https://sports.news.naver.com/wfootball/index.nhn")  # 창

        driver.find_element_by_xpath('//*[@id="_schedule_box"]/div/div[3]/span/a[1]').send_keys(Keys.ENTER)  # 내일클릭

        tm.sleep(0.1)  # 내일버튼클릭을 기다린 후 일정을 가져옴

        text = driver.page_source

        html_match = text  # selenium으로 받은 html을 bs의 html로 복사

        match_list = list()
        score_list = list()
        state_list = list()
        soup_match = BeautifulSoup(html_match, 'html.parser')  # html.parser를 사용해서 soup에 넣겠다

        for match in soup_match.select('div.inner > span.name'):  # 팀이름 받아오기
            match_list.append(match.text.strip())

        for score in soup_match.select('.score'):  # 점수 받아오기
            score_list.append(score.text.strip())

        for state in soup_match.select(('div.state > div.inner')):  # 경기 상태
            state_list.append(state.text.strip())

        match_up_view = list()

        for x in range(len(state_list)):
            if ":" in state_list[x]:
                y = (match_list[x * 2 + 1].ljust(14) + '\t' + '-' + '\t' + state_list[x] + '\t' + '-' + match_list[
                    x * 2].rjust(15))

                match_up_view.append(y)


            else:
                y = (match_list[x * 2 + 1].ljust(14) + '\t' + score_list[x * 2] + '\t' + state_list[x] + '\t' +
                     score_list[x * 2 + 1] + match_list[x * 2].rjust(15))
                match_up_view.append(y)

            match_up_result = '\n\n'.join(match_up_view)  # 리스트에 \n하면서 str로
        print(match_up_result)
        return match_up_result

    def closer_shoot(self, answer1, answer2, answer3):
        # 최근 5경기  유효슈팅  딕셔너리
        import pandas as pd
        if answer1 == answer2:
            messagebox.showinfo(title="ERROR", message="같은 팀을 입력하셨어요!!",icon = 'warning')
            return False

        add = []
        add2 = []
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'HST', 'AST']]
        name = data.drop_duplicates('HomeTeam', keep='first')
        a = {}
        for index, row in name.iterrows():
            aa = shooting_data[
                (shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
            cc = aa.tail(5)
            try_shoot = cc.apply(lambda cc: \
                                     + int(cc['HST']) \
                                         if cc['HomeTeam'] == row['HomeTeam'] \
                                         else + int(cc['AST']),
                                 axis=1)
            a['%s' % (row['HomeTeam'])] = try_shoot.mean()
        # 무승부였을 때의 유효슈팅 평균
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'HST', 'AST']]
        aa = shooting_data[(shooting_data['FTR'] == 'D')]

        shoot = aa.apply(lambda aa: \
                             +int(aa['HST']) + int(aa['AST']) \
                                 if aa['FTR'] == 'D'
                             else +0, \
                         axis=1)
        mean = shoot.mean() / 2

        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'HST', 'AST']]
        aa = shooting_data[(shooting_data['FTR'] == 'H') | (shooting_data['FTR'] == 'A')]
        shoot = aa.apply(lambda aa: \
                             +int(aa['HST']) \
                                 if aa['FTR'] == 'H'
                             else +int(aa['AST']), \
                         axis=1)
        maxium = shoot.mean()

        if maxium < a[answer1]:
            add.append(1)
        elif mean < a[answer1]:
            add.append(0.5)
        else:
            add.append(0)

        if maxium < a[answer2]:
            add2.append(1)
        elif mean < a[answer2]:
            add2.append(0.5)
        else:
            add2.append(0)

        # 최근 5경기  배팅평균 딕셔너리
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'AvgH', 'AvgA']]
        name = data.drop_duplicates('HomeTeam', keep='first')
        a = {}
        for index, row in name.iterrows():
            aa = shooting_data[
                (shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
            cc = aa.tail(5)
            try_shoot = cc.apply(lambda cc: \
                                     + int(cc['AvgH']) \
                                         if cc['HomeTeam'] == row['HomeTeam'] \
                                         else + int(cc['AvgA']), \
                                 axis=1)
            a['%s' % (row['HomeTeam'])] = try_shoot.mean()

        # 무승부였을 때의 배팅평균 평균
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'AvgH', 'AvgA']]
        aa = shooting_data[(shooting_data['FTR'] == 'D')]

        shoot = aa.apply(lambda aa: \
                             +int(aa['AvgH']) + int(aa['AvgA']) \
                                 if aa['FTR'] == 'D'
                             else +0, \
                         axis=1)
        mean = shoot.mean() / 2

        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'AvgH', 'AvgA']]
        aa = shooting_data[(shooting_data['FTR'] == 'H') | (shooting_data['FTR'] == 'A')]
        shoot = aa.apply(lambda aa: \
                             +int(aa['AvgH']) \
                                 if aa['FTR'] == 'H'
                             else +int(aa['AvgA']), \
                         axis=1)
        minium = shoot.mean()
        if minium > a[answer1]:
            add.append(1)
        elif mean > a[answer1]:
            add.append(0.5)
        else:
            add.append(0)

        if minium > a[answer2]:
            add2.append(1)
        elif mean > a[answer2]:
            add2.append(0.5)
        else:
            add2.append(0)

        # 최근 5경기  풀타임득점  딕셔너리
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']]
        name = data.drop_duplicates('HomeTeam', keep='first')
        a = {}
        for index, row in name.iterrows():
            aa = shooting_data[
                (shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
            cc = aa.tail(5)
            try_shoot = cc.apply(lambda cc: \
                                     + int(cc['FTHG']) \
                                         if cc['HomeTeam'] == row['HomeTeam'] \
                                         else + int(cc['FTAG']), \
                                 axis=1)
            a['%s' % (row['HomeTeam'])] = try_shoot.mean()

        # 무승부였을 때의 풀타임득점 평균
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'FTHG', 'FTAG']]
        aa = shooting_data[(shooting_data['FTR'] == 'D')]

        shoot = aa.apply(lambda aa: \
                             +int(aa['FTHG']) + int(aa['FTAG']) \
                                 if aa['FTR'] == 'D'
                             else +0, \
                         axis=1)
        mean = shoot.mean()

        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'FTHG', 'FTAG']]
        aa = shooting_data[(shooting_data['FTR'] == 'H') | (shooting_data['FTR'] == 'A')]
        shoot = aa.apply(lambda aa: \
                             +int(aa['FTHG']) \
                                 if aa['FTR'] == 'H'
                             else +int(aa['FTAG']), \
                         axis=1)
        maxium = shoot.mean()

        if maxium < a[answer1]:
            add.append(1)
        elif mean < a[answer1]:
            add.append(0.5)
        else:
            add.append(0)

        if maxium < a[answer2]:
            add2.append(1)
        elif mean < a[answer2]:
            add2.append(0.5)
        else:
            add2.append(0)

        # 최근 5경기  하프타임득점  딕셔너리
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'HTHG', 'HTAG']]
        name = data.drop_duplicates('HomeTeam', keep='first')
        a = {}
        for index, row in name.iterrows():
            aa = shooting_data[
                (shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
            cc = aa.tail(5)
            try_shoot = cc.apply(lambda cc: \
                                     + int(cc['HTHG']) \
                                         if cc['HomeTeam'] == row['HomeTeam'] \
                                         else + int(cc['HTAG']), \
                                 axis=1)
            a['%s' % (row['HomeTeam'])] = try_shoot.mean()

        # 무승부였을 때의 하프타임득점 평균
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'HTHG', 'HTAG']]
        aa = shooting_data[(shooting_data['FTR'] == 'D')]

        shoot = aa.apply(lambda aa: \
                             +int(aa['HTHG']) + int(aa['HTAG']) \
                                 if aa['FTR'] == 'D'
                             else +0, \
                         axis=1)
        mean = shoot.mean() / 2
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'HTHG', 'HTAG']]
        aa = shooting_data[(shooting_data['FTR'] == 'H') | (shooting_data['FTR'] == 'A')]
        shoot = aa.apply(lambda aa: \
                             +int(aa['HTHG']) \
                                 if aa['FTR'] == 'H'
                             else +int(aa['HTAG']), \
                         axis=1)
        maxium = shoot.mean()

        if maxium < a[answer1]:
            add.append(1)
        elif mean < a[answer1]:
            add.append(0.5)
        else:
            add.append(0)

        if maxium < a[answer2]:
            add2.append(1)
        elif mean < a[answer2]:
            add2.append(0.5)
        else:
            add2.append(0)

        # 최근 5경기  골성공률  딕셔너리
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        data['SGH'] = data['FTHG'] / data['HS']
        data['SGA'] = data['FTAG'] / data['AS']
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'SGH', 'SGA']]
        name = data.drop_duplicates('HomeTeam', keep='first')
        a = {}
        for index, row in name.iterrows():
            aa = shooting_data[
                (shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
            cc = aa.tail(5)
            try_shoot = cc.apply(lambda cc: \
                                     + float(cc['SGH']) \
                                         if cc['HomeTeam'] == row['HomeTeam'] \
                                         else + float(cc['SGA']), \
                                 axis=1)
            a['%s' % (row['HomeTeam'])] = try_shoot.mean()

        # 무승부였을 때의 골성공률 평균
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        data['SGH'] = data['FTHG'] / data['HS']
        data['SGA'] = data['FTAG'] / data['AS']
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'SGH', 'SGA']]
        aa = shooting_data[(shooting_data['FTR'] == 'D')]
        shoot = aa.apply(lambda aa: \
                             +float(aa['SGH']) + float(aa['SGA']) \
                                 if aa['FTR'] == 'D'
                             else +0, \
                         axis=1)
        mean = shoot.mean() / 2
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        data['SGH'] = data['FTHG'] / data['HS']
        data['SGA'] = data['FTAG'] / data['AS']
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'SGH', 'SGA']]
        aa = shooting_data[(shooting_data['FTR'] == 'H') | (shooting_data['FTR'] == 'A')]
        shoot = aa.apply(lambda aa: \
                             +int(aa['SGH']) \
                                 if aa['FTR'] == 'H'
                             else +int(aa['SGA']), \
                         axis=1)
        maxium = shoot.mean()

        if maxium < a[answer1]:
            add.append(1)
        elif mean < a[answer1]:
            add.append(0.5)
        else:
            add.append(0)

        if maxium < a[answer2]:
            add2.append(1)
        elif mean < a[answer2]:
            add2.append(0.5)
        else:
            add2.append(0)

        # 전 경기  유효슈팅  딕셔너리
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'HST', 'AST']]
        name = data.drop_duplicates('HomeTeam', keep='first')
        a = {}
        for index, row in name.iterrows():
            aa = shooting_data[
                (shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
            cc = aa
            try_shoot = cc.apply(lambda cc: \
                                     + int(cc['HST']) \
                                         if cc['HomeTeam'] == row['HomeTeam'] \
                                         else + int(cc['AST']), \
                                 axis=1)
            a['%s' % (row['HomeTeam'])] = try_shoot.mean()

        # 무승부였을 때의 유효슈팅 평균
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'HST', 'AST']]
        aa = shooting_data[(shooting_data['FTR'] == 'D')]

        shoot = aa.apply(lambda aa: \
                             +int(aa['HST']) + int(aa['AST']) \
                                 if aa['FTR'] == 'D'
                             else +0, \
                         axis=1)
        mean = shoot.mean() / 2
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'HST', 'AST']]
        aa = shooting_data[(shooting_data['FTR'] == 'H') | (shooting_data['FTR'] == 'A')]
        shoot = aa.apply(lambda aa: \
                             +int(aa['HST']) \
                                 if aa['FTR'] == 'H'
                             else +int(aa['AST']), \
                         axis=1)
        maxium = shoot.mean()

        if maxium < a[answer1]:
            add.append(1)
        elif mean < a[answer1]:
            add.append(0.5)
        else:
            add.append(0)

        if maxium < a[answer2]:
            add2.append(1)
        elif mean < a[answer2]:
            add2.append(0.5)
        else:
            add2.append(0)

        # 전경기  배팅평균 딕셔너리
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'AvgH', 'AvgA']]
        name = data.drop_duplicates('HomeTeam', keep='first')
        a = {}
        for index, row in name.iterrows():
            aa = shooting_data[
                (shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
            cc = aa
            try_shoot = cc.apply(lambda cc: \
                                     + int(cc['AvgH']) \
                                         if cc['HomeTeam'] == row['HomeTeam'] \
                                         else + int(cc['AvgA']), \
                                 axis=1)
            a['%s' % (row['HomeTeam'])] = try_shoot.mean()
        # 무승부였을 때의 배팅평균 평균
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'AvgH', 'AvgA']]
        aa = shooting_data[(shooting_data['FTR'] == 'D')]

        shoot = aa.apply(lambda aa: \
                             +int(aa['AvgH']) + int(aa['AvgA']) \
                                 if aa['FTR'] == 'D'
                             else +0, \
                         axis=1)
        mean = shoot.mean() / 2
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'AvgH', 'AvgA']]
        aa = shooting_data[(shooting_data['FTR'] == 'H') | (shooting_data['FTR'] == 'A')]
        shoot = aa.apply(lambda aa: \
                             +int(aa['AvgH']) \
                                 if aa['FTR'] == 'H'
                             else +int(aa['AvgA']), \
                         axis=1)
        minium = shoot.mean()
        if minium > a[answer1]:
            add.append(1)
        elif mean > a[answer1]:
            add.append(0.5)
        else:
            add.append(0)

        if minium > a[answer2]:
            add2.append(1)
        elif mean > a[answer2]:
            add2.append(0.5)
        else:
            add2.append(0)

        # 전경기 풀타임득점  딕셔너리
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']]
        name = data.drop_duplicates('HomeTeam', keep='first')
        a = {}
        for index, row in name.iterrows():
            aa = shooting_data[
                (shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
            cc = aa
            try_shoot = cc.apply(lambda cc: \
                                     + int(cc['FTHG']) \
                                         if cc['HomeTeam'] == row['HomeTeam'] \
                                         else + int(cc['FTAG']), \
                                 axis=1)
            a['%s' % (row['HomeTeam'])] = try_shoot.mean()

        # 무승부였을 때의 풀타임득점 평균
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'FTHG', 'FTAG']]
        aa = shooting_data[(shooting_data['FTR'] == 'D')]

        shoot = aa.apply(lambda aa: \
                             +int(aa['FTHG']) + int(aa['FTAG']) \
                                 if aa['FTR'] == 'D'
                             else +0, \
                         axis=1)
        mean = shoot.mean() / 2
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'FTHG', 'FTAG']]
        aa = shooting_data[(shooting_data['FTR'] == 'H') | (shooting_data['FTR'] == 'A')]
        shoot = aa.apply(lambda aa: \
                             +int(aa['FTHG']) \
                                 if aa['FTR'] == 'H'
                             else +int(aa['FTAG']), \
                         axis=1)
        maxium = shoot.mean()

        if maxium < a[answer1]:
            add.append(1)
        elif mean < a[answer1]:
            add.append(0.5)
        else:
            add.append(0)

        if maxium < a[answer2]:
            add2.append(1)
        elif mean < a[answer2]:
            add2.append(0.5)
        else:
            add2.append(0)
        # 전경기 하프타임득점  딕셔너리
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'HTHG', 'HTAG']]
        name = data.drop_duplicates('HomeTeam', keep='first')
        a = {}
        for index, row in name.iterrows():
            aa = shooting_data[
                (shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
            cc = aa
            try_shoot = cc.apply(lambda cc: \
                                     + int(cc['HTHG']) \
                                         if cc['HomeTeam'] == row['HomeTeam'] \
                                         else + int(cc['HTAG']), \
                                 axis=1)
            a['%s' % (row['HomeTeam'])] = try_shoot.mean()

        # 무승부였을 때의 하프타임득점 평균
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'HTHG', 'HTAG']]
        aa = shooting_data[(shooting_data['FTR'] == 'D')]

        shoot = aa.apply(lambda aa: \
                             +int(aa['HTHG']) + int(aa['HTAG']) \
                                 if aa['FTR'] == 'D'
                             else +0, \
                         axis=1)
        mean = shoot.mean() / 2
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'HTHG', 'HTAG']]
        aa = shooting_data[(shooting_data['FTR'] == 'H') | (shooting_data['FTR'] == 'A')]
        shoot = aa.apply(lambda aa: \
                             +int(aa['HTHG']) \
                                 if aa['FTR'] == 'H'
                             else +int(aa['HTAG']), \
                         axis=1)
        maxium = shoot.mean()

        if maxium < a[answer1]:
            add.append(1)
        elif mean < a[answer1]:
            add.append(0.5)
        else:
            add.append(0)

        if maxium < a[answer2]:
            add2.append(1)
        elif mean < a[answer2]:
            add2.append(0.5)
        else:
            add2.append(0)

        # 전경기  골성공률  딕셔너리
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        data['SGH'] = data['FTHG'] / data['HS']
        data['SGA'] = data['FTAG'] / data['AS']
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'SGH', 'SGA']]
        name = data.drop_duplicates('HomeTeam', keep='first')
        a = {}
        for index, row in name.iterrows():
            aa = shooting_data[
                (shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
            cc = aa
            try_shoot = cc.apply(lambda cc: \
                                     + float(cc['SGH']) \
                                         if cc['HomeTeam'] == row['HomeTeam'] \
                                         else + float(cc['SGA']), \
                                 axis=1)
            a['%s' % (row['HomeTeam'])] = try_shoot.mean()

        # 무승부였을 때의 골성공률 평균
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        data['SGH'] = data['FTHG'] / data['HS']
        data['SGA'] = data['FTAG'] / data['AS']
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'SGH', 'SGA']]
        aa = shooting_data[(shooting_data['FTR'] == 'D')]
        shoot = aa.apply(lambda aa: \
                             +float(aa['SGH']) + float(aa['SGA']) \
                                 if aa['FTR'] == 'D'
                             else +0, \
                         axis=1)
        mean = shoot.mean() / 2
        import pandas as pd
        data = pd.read_csv('%s.csv' % answer3, engine='python')
        data['SGH'] = data['FTHG'] / data['HS']
        data['SGA'] = data['FTAG'] / data['AS']
        shooting_data = data[['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'SGH', 'SGA']]
        aa = shooting_data[(shooting_data['FTR'] == 'H') | (shooting_data['FTR'] == 'A')]
        shoot = aa.apply(lambda aa: \
                             +int(aa['SGH']) \
                                 if aa['FTR'] == 'H'
                             else +int(aa['SGA']), \
                         axis=1)
        maxium = shoot.mean()

        if maxium < a[answer1]:
            add.append(1)
        elif mean < a[answer1]:
            add.append(0.5)
        else:
            add.append(0)

        if maxium < a[answer2]:
            add2.append(1)
        elif mean < a[answer2]:
            add2.append(0.5)
        else:
            add2.append(0)

        if sum(add) > sum(add2):
            self.resultlabel1 = Label(self.resultframe, text=str(sum(add))+" "+str(self.myteam2.get())+'  vs  '+ str(self.myteam3.get())+" "+str(sum(add2)),
                                      font=('Koverwatch',30), fg = 'white', bg = '#333438')
            self.resultlabel1.place(x=3,y=3)
            self.resultlabel2 = Label(self.resultframe, text=self.myteam2.get() + "팀이 더 유리한 경기네요!",
                                      font=('Koverwatch', 30), fg='white', bg='#333438')
            self.resultlabel2.place(x=3, y=63)

        elif sum(add2) > sum(add):
            self.resultlabel1 = Label(self.resultframe, text=str(sum(add)) + " " + str(self.myteam2.get()) + '  vs  ' + str(self.myteam3.get()) + " " + str(sum(add2)),
                                      font=('Koverwatch', 30), fg='white', bg='#333438')
            self.resultlabel1.place(x=3, y=3)

            self.resultlabel2= Label(self.resultframe, text=self.myteam3.get()+"팀이 더 유리한 경기네요!",
                                     font=('Koverwatch', 30), fg='white', bg='#333438')
            self.resultlabel2.place(x=3, y=63)
        else:
            self.resultlabel1 = Label(self.resultframe,text=("두팀 다 막상막하에요!"), font=('Koverwatch', 30), fg='white', bg='#333438')
            self.resultlabel1.place(x=3, y=3)
            '''
            add[]간의 차이가 4점이상일때는 압도적이다.
            add[]간의 차이가 1점이하 일땐 미비하다.
            전력차가 미비해서 역배를 가보는것도 좋을거 같아요!
            else
            
            '''