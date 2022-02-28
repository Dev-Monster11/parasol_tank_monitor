import sqlite3
import datetime

class DB():
    def __init__(self):
        self.con = sqlite3.connect('monitor.db')
        print(self.con)
    def insertPacket(self, packet):
        cur = self.con.cursor()
        cur.execute('INSERT INTO total(tank_id, ph, orp, tlevel, cond, temp, timestamp) VALUES(?, ?, ?, ?, ?, ?, ?)', packet)
    def insertDemo(self, packet):
        # print(packet)
        # cur = self.con.cursor()
        # print(cur)
        self.con.execute('INSERT INTO total(tank_id, ph, orp, tlevel, cond, temp, timestamp) VALUES(?, ?, ?, ?, ?, ?, ?)', packet)
        self.con.commit()
    def levelData(self):
        result = []
        # for i in range(4):

        rows = self.con.execute('SELECT tlevel FROM total WHERE tank_id = 1').fetchAll()