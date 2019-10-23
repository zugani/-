#! python3
#積み立て投資シミュレーター
#ver2 期間を一括入力できるように

import re

#入力

#期間の正規表現
time_regex = re.compile(r"(\d+)(\w+)")

while True:
    #期間の入力
    time = input("期間を入力してください(単位：年or月or日)")
    #数字と単位に分ける
    mo = time_regex.search(time)
    period = int(mo.group(1))
    unit = mo.group(2)
    if unit =="年" or unit=="カ月" or  unit=="日":
        break
    else:
        print("単位が間違っています")
        continue

#金額
mon = int(input("何円ずつ入れる？"))
#利回り
profit = int(input("利回りは？(単位:%)"))


#計算
#年に置き換える
if unit=="カ月":
    year = period/12
    money = mon*12
elif unit=="日":
    year = period/365
    money = mon*365
elif unit =="年":
    year = period
    money = mon

saving_money = int(money*year)
invest_money = 0
if type(year) is int:
    for i in range(year):
        invest_money += money*((1+profit/100)**(i+1))
if type(year) is float:
    int_year = int(year)
    float_year = year - int_year
    for i in range(int_year):
        invest_money += money*((1+profit/100)**(i+1))
    invest_money += money*float_year*(1+(profit/100*float_year))
invest_money = int(invest_money)

#出力
print("利回りが{}%のとき、1{}に{}円ずつ積み立てると、{}間で{}円積み立てて{}円になります。".format(profit,unit,mon,time,saving_money,invest_money))
