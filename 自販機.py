print("硬貨を入れてください")
money = 0
pay = input()
payint = int(pay)
money = money + payint

while money >= 100:
    print ("残り",money,"円。ご注文をどうぞ。")
    print ("天然水　100円")
    print ("コーラ　150円")
    print ("ビール　200円")
    order = input(">>")
    L = {"天然水":100,"コーラ":150,"ビール":200}
    orderint = int(L[order])
    change = money - orderint

    while change < 0:
        print ("お金が不足しています。硬貨を入れてください")
        pay = input(">>")
        payint = int(pay)
        money = money + payint
        change = money - order

    print (order)
    money = change

print("お金が足りません。お手数ですが初めからやり直してください。")
quit()
    
