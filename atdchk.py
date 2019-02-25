import sqlite3
#import nfctoid
import nfctoid_test #for test code
import registration
import datetime
from random import randint #for test code


def atdchk():
    conn = sqlite3.connect("memberlist.db")
    cur = conn.cursor()

    #target_card = nfctoid.scan_id()
    target_card = nfctoid_test.scan_id()
    print(target_card + "가 인식되었습니다.")

    cur.execute("SELECT COUNT(CARD) FROM MEMBERS WHERE CARD = '" + target_card + "'")
    card_rows = cur.fetchall()
    if card_rows[0][0] == 1:
        cur.execute("SELECT ATD FROM MEMBERS WHERE CARD = '" + target_card + "'")
        atd_rows = cur.fetchall()
        atdnum = atd_rows[0][0]
        
        now = datetime.datetime.now()
        year_now = now.year
        month_now = now.month
        day_now = now.day
        
        cur.execute("SELECT LASTCHECKED FROM MEMBERS WHERE CARD = '" + target_card + "'")
        last_date = cur.fetchall()[0][0] #last_date is a str
        
        converted_date = datetime.datetime.strptime(last_date.split()[0], "%Y-%m-%d").date() # This will be changed into date object.
        year_checked = converted_date.year
        month_checked = converted_date.month
        day_checked = converted_date.day
        if randint(0,2) == 0: #for test code
            day_now = day_checked+1

        cur.execute("SELECT NAME FROM MEMBERS WHERE CARD = '" + target_card + "'")
        name = cur.fetchall()

        if day_checked == day_now and month_checked == month_now and year_checked == year_now:
            print(name[0][0] + "님은 이미 오늘 출석하셨습니다.")
            print("오늘은 " + str(year_now) + "년 " + str(month_now) +"월 " + str(day_now) + "일입니다.")
            print("마지막으로 출석한 날짜는 " + str(year_checked) + "년 " + str(month_checked) +"월 " + str(day_checked) + "일입니다.\n")
        else:
            cur.execute("UPDATE MEMBERS SET ATD = ?, LASTCHECKED = DATETIME('NOW','LOCALTIME') WHERE CARD = ?", (atdnum+1, target_card))
            conn.commit()
            print(name[0][0] + "님, 출석이 완료되었습니다. 감사합니다!")
            print("오늘은 " + str(year_now) + "년 " + str(month_now) +"월 " + str(day_now) + "일입니다.") #for test code
    else:
        registration.registration(target_card)
