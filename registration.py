import sqlite3
import nfctoid

def registration():
    conn = sqlite3.connect("memberlist.db")
    cur = conn.cursor()
    create_table = """CREATE TABLE IF NOT EXISTS MEMBERS(
        CARD TEXT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        ATTNUM INTEGER NOT NULL)"""
    cur.execute(create_table)
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

    # for i in card_rows:
    #     if card == i:
    #         print("이미 등록된 사용자입니다!\n등록을 종료합니다.")
    #         conn.close() 
    #         return None
        

    add_info = "INSERT INTO MEMBERS(CARD, NAME, ATTNUM) VALUES (?, ?, ?)"
    
    cur.execute(add_info, (card, name, 0))
    conn.commit()
    conn.close()

registration()