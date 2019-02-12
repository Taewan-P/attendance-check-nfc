import nfctoid
import atdchk
import sqlite3

# a = nfctoid.idtest()
# print(a)

def main():
    conn = sqlite3.connect("memberlist.db")
    cur = conn.cursor()
    create_table = """CREATE TABLE IF NOT EXISTS MEMBERS(
        CARD TEXT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        ATT INTEGER NOT NULL,
        LASTCHECKED DATE NOT NULL)"""
    cur.execute(create_table)
    conn.close()
    
    while(True):
        atdchk.atdchk()
        
main()