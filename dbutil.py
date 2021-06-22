import pymysql


class DBUtil:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", port=3306, db="wxy", user="root", passwd="root")

    def update(self, sql, values):
        cur = self.conn.cursor()
        try:
            cur.execute(sql, values)
            self.conn.commit()
            return True
        except:
            return False
        finally:
            cur.close()

    def query(self, sql, values):
        cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cur.execute(sql, values)
            return cur.fetchall()
        except:
            return None
        finally:
            cur.close()

    def close(self):
        self.conn.close()
