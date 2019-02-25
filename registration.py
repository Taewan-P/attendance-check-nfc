import sqlite3
#import nfctoid
import nfctoid_test            

def registration(card_id):
    while True:
        ask = input("자람 출석부에 등록하시겠습니까? y/n\n")
        if ask == "N" or ask == "n":
            break
        elif ask == "Y" or ask == "y":
            conn = sqlite3.connect("memberlist.db")
            cur = conn.cursor()
            name = input("등록하실 이름을 입력하세요 : ")
            while True:
                if name == "":
                    name = input("등록하실 이름을 입력하세요 : ")
                else:
                    break

            card = card_id
            ccheck_sql = "SELECT COUNT(CARD) FROM MEMBERS WHERE CARD = '" + card + "'"
            cur.execute(ccheck_sql)
            add_info = "INSERT INTO MEMBERS(CARD, NAME, ATD, LASTCHECKED) VALUES (?, ?, ?, DATETIME('NOW','LOCALTIME'))"

            cur.execute(add_info, (card, name, 1))
            conn.commit()
            conn.close()
            print('첫번째 출석을 환영합니다 ' + name + '님!')
            break
        else:
            continue
            