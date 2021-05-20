#-*- coding: utf-8 -*-

def closer_shoot(answer1,answer2,answer3):
    # 최근 5경기  유효슈팅  딕셔너리
    import pandas as pd
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','HST','AST']]
    name = data.drop_duplicates('HomeTeam', keep='first')
    a={}
    for index , row in name.iterrows():
        aa=shooting_data[(shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
        cc=aa.tail(5)
        try_shoot=cc.apply(lambda cc:\
        + int(cc['HST'])\
        if cc['HomeTeam']== row['HomeTeam']\
        else + int(cc['AST']),\
               axis=1)
        a['%s' %(row['HomeTeam'])] =try_shoot.mean()
    # 무승부였을 때의 유효슈팅 평균
    import pandas as pd
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','FTR','HST','AST']]
    aa=shooting_data[(shooting_data['FTR'] == 'D' )]

    shoot = aa.apply(lambda aa:\
                        +int(aa['HST'])+int(aa['AST'])\
                        if aa['FTR']=='D'
                        else +0 ,\
                      axis=1)
    mean= shoot.mean()/2

    import pandas as pd
    data = pd.read_csv('%s.csv'%answer3, engine='python')
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
    elif mean < a[answer1] :
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
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','AvgH','AvgA']]
    name = data.drop_duplicates('HomeTeam', keep='first')
    a={}
    for index , row in name.iterrows():
        aa=shooting_data[(shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
        cc=aa.tail(5)
        try_shoot=cc.apply(lambda cc:\
        + int(cc['AvgH'])\
        if cc['HomeTeam']== row['HomeTeam']\
        else + int(cc['AvgA']),\
                axis=1)
        a['%s' %(row['HomeTeam'])] =try_shoot.mean()

    # 무승부였을 때의 배팅평균 평균
    import pandas as pd
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','FTR','AvgH','AvgA']]
    aa=shooting_data[(shooting_data['FTR'] == 'D' )]

    shoot = aa.apply(lambda aa:\
                         +int(aa['AvgH'])+int(aa['AvgA'])\
                         if aa['FTR']=='D'
                         else +0 ,\
                         axis=1)
    mean= shoot.mean()/2

    import pandas as pd
    data = pd.read_csv('%s.csv'%answer3, engine='python')
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
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','FTHG','FTAG']]
    name = data.drop_duplicates('HomeTeam', keep='first')
    a={}
    for index , row in name.iterrows():
        aa=shooting_data[(shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
        cc=aa.tail(5)
        try_shoot=cc.apply(lambda cc:\
        + int(cc['FTHG'])\
        if cc['HomeTeam']== row['HomeTeam']\
        else + int(cc['FTAG']),\
                axis=1)
        a['%s' %(row['HomeTeam'])] =try_shoot.mean()

    # 무승부였을 때의 풀타임득점 평균
    import pandas as pd
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','FTR','FTHG','FTAG']]
    aa=shooting_data[(shooting_data['FTR'] == 'D' )]

    shoot = aa.apply(lambda aa:\
                         +int(aa['FTHG'])+int(aa['FTAG'])\
                         if aa['FTR']=='D'
                         else +0 ,\
                         axis=1)
    mean = shoot.mean()

    import pandas as pd
    data = pd.read_csv('%s.csv'%answer3, engine='python')
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
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','HTHG','HTAG']]
    name = data.drop_duplicates('HomeTeam', keep='first')
    a={}
    for index , row in name.iterrows():
        aa=shooting_data[(shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
        cc=aa.tail(5)
        try_shoot=cc.apply(lambda cc:\
        + int(cc['HTHG'])\
        if cc['HomeTeam']== row['HomeTeam']\
        else + int(cc['HTAG']),\
                axis=1)
        a['%s' %(row['HomeTeam'])] =try_shoot.mean()

    # 무승부였을 때의 하프타임득점 평균
    import pandas as pd
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','FTR','HTHG','HTAG']]
    aa=shooting_data[(shooting_data['FTR'] == 'D' )]

    shoot = aa.apply(lambda aa:\
                         +int(aa['HTHG'])+int(aa['HTAG'])\
                         if aa['FTR']=='D'
                         else +0 ,\
                         axis=1)
    mean= shoot.mean()/2
    import pandas as pd
    data = pd.read_csv('%s.csv'%answer3, engine='python')
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
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    data['SGH'] = data['FTHG']/data['HS']
    data['SGA'] = data['FTAG']/data['AS']
    shooting_data= data[['Date','HomeTeam','AwayTeam','SGH','SGA']]
    name = data.drop_duplicates('HomeTeam', keep='first')
    a={}
    for index , row in name.iterrows():
        aa=shooting_data[(shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
        cc=aa.tail(5)
        try_shoot=cc.apply(lambda cc:\
        + float(cc['SGH'])\
        if cc['HomeTeam']== row['HomeTeam']\
        else + float(cc['SGA']),\
                axis=1)
        a['%s' %(row['HomeTeam'])] =try_shoot.mean()

    # 무승부였을 때의 골성공률 평균
    import pandas as pd
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    data['SGH'] = data['FTHG']/data['HS']
    data['SGA'] = data['FTAG']/data['AS']
    shooting_data= data[['Date','HomeTeam','AwayTeam','FTR','SGH','SGA']]
    aa=shooting_data[(shooting_data['FTR'] == 'D' )]
    shoot = aa.apply(lambda aa:\
                         +float(aa['SGH'])+float(aa['SGA'])\
                         if aa['FTR']=='D'
                         else +0 ,\
                         axis=1)
    mean= shoot.mean()/2
    import pandas as pd
    data = pd.read_csv('%s.csv'%answer3, engine='python')
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
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','HST','AST']]
    name = data.drop_duplicates('HomeTeam', keep='first')
    a={}
    for index , row in name.iterrows():
        aa=shooting_data[(shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
        cc=aa
        try_shoot=cc.apply(lambda cc:\
        + int(cc['HST'])\
        if cc['HomeTeam']== row['HomeTeam']\
        else + int(cc['AST']),\
               axis=1)
        a['%s' %(row['HomeTeam'])] =try_shoot.mean()

    # 무승부였을 때의 유효슈팅 평균
    import pandas as pd
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','FTR','HST','AST']]
    aa=shooting_data[(shooting_data['FTR'] == 'D' )]

    shoot = aa.apply(lambda aa:\
                        +int(aa['HST'])+int(aa['AST'])\
                        if aa['FTR']=='D'
                        else +0 ,\
                      axis=1)
    mean= shoot.mean()/2
    import pandas as pd
    data = pd.read_csv('%s.csv'%answer3, engine='python')
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
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','AvgH','AvgA']]
    name = data.drop_duplicates('HomeTeam', keep='first')
    a={}
    for index , row in name.iterrows():
        aa=shooting_data[(shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
        cc=aa
        try_shoot=cc.apply(lambda cc:\
        + int(cc['AvgH'])\
        if cc['HomeTeam']== row['HomeTeam']\
        else + int(cc['AvgA']),\
                axis=1)
        a['%s' %(row['HomeTeam'])] =try_shoot.mean()
    # 무승부였을 때의 배팅평균 평균
    import pandas as pd
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','FTR','AvgH','AvgA']]
    aa=shooting_data[(shooting_data['FTR'] == 'D' )]

    shoot = aa.apply(lambda aa:\
                         +int(aa['AvgH'])+int(aa['AvgA'])\
                         if aa['FTR']=='D'
                         else +0 ,\
                         axis=1)
    mean= shoot.mean()/2
    import pandas as pd
    data = pd.read_csv('%s.csv'%answer3, engine='python')
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
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','FTHG','FTAG']]
    name = data.drop_duplicates('HomeTeam', keep='first')
    a={}
    for index , row in name.iterrows():
        aa=shooting_data[(shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
        cc=aa
        try_shoot=cc.apply(lambda cc:\
        + int(cc['FTHG'])\
        if cc['HomeTeam']== row['HomeTeam']\
        else + int(cc['FTAG']),\
                axis=1)
        a['%s' %(row['HomeTeam'])] =try_shoot.mean()

    # 무승부였을 때의 풀타임득점 평균
    import pandas as pd
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','FTR','FTHG','FTAG']]
    aa=shooting_data[(shooting_data['FTR'] == 'D' )]

    shoot = aa.apply(lambda aa:\
                         +int(aa['FTHG'])+int(aa['FTAG'])\
                         if aa['FTR']=='D'
                         else +0 ,\
                         axis=1)
    mean= shoot.mean()/2
    import pandas as pd
    data = pd.read_csv('%s.csv'%answer3, engine='python')
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
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','HTHG','HTAG']]
    name = data.drop_duplicates('HomeTeam', keep='first')
    a={}
    for index , row in name.iterrows():
        aa=shooting_data[(shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
        cc=aa
        try_shoot=cc.apply(lambda cc:\
        + int(cc['HTHG'])\
        if cc['HomeTeam']== row['HomeTeam']\
        else + int(cc['HTAG']),\
                axis=1)
        a['%s' %(row['HomeTeam'])] =try_shoot.mean()

    # 무승부였을 때의 하프타임득점 평균
    import pandas as pd
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    shooting_data= data[['Date','HomeTeam','AwayTeam','FTR','HTHG','HTAG']]
    aa=shooting_data[(shooting_data['FTR'] == 'D' )]

    shoot = aa.apply(lambda aa:\
                         +int(aa['HTHG'])+int(aa['HTAG'])\
                         if aa['FTR']=='D'
                         else +0 ,\
                         axis=1)
    mean= shoot.mean()/2
    import pandas as pd
    data = pd.read_csv('%s.csv'%answer3, engine='python')
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
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    data['SGH'] = data['FTHG']/data['HS']
    data['SGA'] = data['FTAG']/data['AS']
    shooting_data= data[['Date','HomeTeam','AwayTeam','SGH','SGA']]
    name = data.drop_duplicates('HomeTeam', keep='first')
    a={}
    for index , row in name.iterrows():
        aa=shooting_data[(shooting_data['HomeTeam'] == row['HomeTeam']) | (shooting_data['AwayTeam'] == row['HomeTeam'])]
        cc=aa
        try_shoot=cc.apply(lambda cc:\
        + float(cc['SGH'])\
        if cc['HomeTeam']== row['HomeTeam']\
        else + float(cc['SGA']),\
                axis=1)
        a['%s' %(row['HomeTeam'])] =try_shoot.mean()

    # 무승부였을 때의 골성공률 평균
    import pandas as pd
    data=pd.read_csv('%s.csv'%answer3, engine='python')
    data['SGH'] = data['FTHG']/data['HS']
    data['SGA'] = data['FTAG']/data['AS']
    shooting_data= data[['Date','HomeTeam','AwayTeam','FTR','SGH','SGA']]
    aa=shooting_data[(shooting_data['FTR'] == 'D' )]
    shoot = aa.apply(lambda aa:\
                         +float(aa['SGH'])+float(aa['SGA'])\
                         if aa['FTR']=='D'
                         else +0 ,\
                         axis=1)
    mean= shoot.mean()/2
    import pandas as pd
    data = pd.read_csv('%s.csv'%answer3, engine='python')
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
while True:
    answer3 = input('리그명:')
    answer1 = input('선호하는 팀명:')
    answer2 = input('상대팀명:')
    add = []
    add2 = []
    closer_shoot(answer1,answer2,answer3)
    if sum(add) > sum(add2):
        print('승률이 큰팀 : %s:' % answer1, sum(add), '승률이 작은팀%s:' % answer2, sum(add2))
    elif sum(add) < sum(add2):
        print( '승률이 큰팀%s:' % answer2, sum(add2),'승률이 작은팀: %s:' % answer1, sum(add))
    else:
        print('%s:' % answer1, sum(add),'무승부','%s:' % answer2, sum(add2))