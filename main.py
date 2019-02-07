import nfctoid
import sqlite3

a = nfctoid.idtest()
print(a)

def main():
    conn = sqlite3.connect("memberlist.db")
    cur = conn.cursor()
    create_table = """CREATE TABLE IF NOT EXISTS MEMBERS(
        CARD TEXT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        ATT INTEGER NOT NULL)"""
    cur.execute(create_table)
    
    while(True):
        print("자람웹실 출석체크 시스템")

    conn.close()