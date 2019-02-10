import sqlite3
import nfctoid            

def registration():
    ask = input("자람 출석부에 등록하시겠습니까? y/n\n")
    while True:
        if ask == "N" or "n":
            exit()
        if ask == "Y" or "y":
            conn = sqlite3.connect("memberlist.db")
            cur = conn.cursor()
    
            name = input("등록하실 이름을 입력하세요 : ")
            while True:
                if name == "":
                    name = input("등록하실 이름을 입력하세요 : ")
                else:
                    break

            print("등록하실 카드를 찍어 주세요.")
            card = nfctoid.scan_id()

            ccheck_sql = "select count(card) from members where card = '" + card + "'"
            cur.execute(ccheck_sql)
            card_rows = cur.fetchall()
            print(card_rows)

            if card_rows[0][0] == 1:
                print("이미 등록된 사용자입니다!\n등록을 종료합니다.")
                conn.close()
            else:
                add_info = "INSERT INTO MEMBERS(CARD, NAME, ATTNUM) VALUES (?, ?, ?)"
            
                cur.execute(add_info, (card, name, 0))
                conn.commit()
                conn.close()
            