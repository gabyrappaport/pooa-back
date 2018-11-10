import sqlite3


class Database:
    conn = sqlite3.connect("itn.db", check_same_thread=False)

    @staticmethod
    def delete_table(table_name):
        cursor = Database.conn.cursor()
        cursor.execute("DROP TABLE %s" % table_name)
        Database.conn.commit()
        cursor.close()

    @staticmethod
    def query(sql, value=None):
        cursor = Database.conn.cursor()
        if value is None:
            query = cursor.execute(sql)
        else:
            query = cursor.execute(sql, value)
        Database.conn.commit()
        return query
