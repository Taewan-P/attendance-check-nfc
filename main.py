import nfctoid
import sqlite3

a = nfctoid.idtest()
print(a)

def main():
    conn = sqlite3.connect("memberlist.db")
    cur = conn.cursor()

    while(True):
        print("자람웹실 출석체크 시스템")



    conn.close()



