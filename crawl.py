import requests
from bs4 import BeautifulSoup

# 파싱할 페이지를 요청
html = requests.get('https://sports.news.naver.com/wfootball/news/index.nhn?isphoto=N&type=popular')
# 페이지 정보중 html 코드만 얻어서 파싱
soup = BeautifulSoup(html.text,'html.parser')
# BeautifulSoup의 find(‘태그이름’, {‘속성이름’:’속성값‘}) divs1 = soup.find('div', {'class':'reporter'})
divs_epl = soup.find('div',{'class': 'aside_rank_news'})

# BeautifulSoup의 findAll(‘태그이름‘) => 일치하는 모든 태그의 내용을 찾아서 리스트로 저장 lis1 = divs1.findAll('li')


lis_epl = divs_epl.findAll('ul',{'id':'_ranking_news_list_0'})


for team in lis_epl:
    teamName = team.find('li')
    print(teamName.text)
print("\n===========================")
