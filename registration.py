import sqlite3
import nfctoid

def registration():
    conn = sqlite3.connect("memberlist.db")
    cur = conn.cursor()
    create_table = """CREATE TABLE IF NOT EXISTS MEMBERS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        CARD TEXT NOT NULL,
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

    add_info = "INSERT INTO MEMBERS(NAME, CARD, ATTNUM) VALUES (?, ?, ?)"
    
    cur.execute(add_info, (name, card, 0))
    conn.commit()





    conn.close()

registration()