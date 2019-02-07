import sqlite3
import nfctoid
import registration

def atdchk():
    conn = sqlite3.connect("memberlist.db")
    cur = conn.cursor()

    target_card = nfctoid.scan_id

    cur.execute("select count(card) from members where card = '" + target_card + "'")
    card_rows = cur.fetchall()
    if card_rows[0][0] == 1:
        cur.execute("select att from members where card = '" + target_card + "'")
        att_rows = cur.fetchall()
        attnum = att_rows[0][0]
        cur.execute("update members set att = ? where card = ?", (attnum+1, target_card))
    # else:
    #     registration