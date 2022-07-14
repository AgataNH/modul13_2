import sqlite3
from sqlite3 import Error
from create_tables import create_connection

def select_all(conn, table):
   """
   Query all rows in the table
   :param conn: the Connection object
   :return:
   """
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")
   rows = cur.fetchall()

   return rows

def select_where(conn, table, **query):
   """
   Query tasks from table with data from **query dict
   :param conn: the Connection object
   :param table: table name
   :param query: dict of attributes and values
   :return:
   """
   cur = conn.cursor()
   qs = []
   values = ()
   for k, v in query.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)
   cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
   rows = cur.fetchall()
   return rows

if __name__ == "__main__":
    conn = create_connection("database.db")
    select_all(conn, "meetings")

    print(select_all(conn, "meetings"))
    conn.commit()

    select_all(conn, "participants")

    print(select_all(conn, "participants"))
    conn.commit()

    select_where(conn, "participants", status="potwierdzony")

    print(select_where(conn, "participants", status="potwierdzony"))
    conn.commit()
