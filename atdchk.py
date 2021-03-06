import sqlite3
import nfctoid
import registration

def atdchk():
    conn = sqlite3.connect("memberlist.db")
    cur = conn.cursor()

    target_card = nfctoid.scan_id()
    print(target_card + "가 인식되었습니다.")

    cur.execute("SELECT COUNT(CARD) FROM MEMBERS WHERE CARD = '" + target_card + "'")
    card_rows = cur.fetchall()
    if card_rows[0][0] == 1:
        cur.execute("SELECT ATT FROM MEMBERS WHERE CARD = '" + target_card + "'")
        att_rows = cur.fetchall()
        attnum = att_rows[0][0]
        cur.execute("UPDATE MEMBERS SET ATT = ?, LASTCHECKED = DATETIME('NOW','LOCALTIME') WHERE CARD = ?", (attnum+1, target_card))
        conn.commit()
    else:
        registration.registration()