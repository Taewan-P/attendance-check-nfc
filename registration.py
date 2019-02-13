import sqlite3
import nfctoid            

def registration(card_id):
    ask = input("자람 출석부에 등록하시겠습니까? y/n\n")
    while True:
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
            ccheck_sql = "select count(card) from members where card = '" + card + "'"
            cur.execute(ccheck_sql)
            card_rows = cur.fetchall()
            add_info = "INSERT INTO MEMBERS(CARD, NAME, ATT) VALUES (?, ?, ?)"
        
            cur.execute(add_info, (card, name, 1))
            conn.commit()
            conn.close()
            break
            