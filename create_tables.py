import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)
   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == "__main__":

   create_meetings_sql = """
   -- meetings table
   CREATE TABLE IF NOT EXISTS meetings (
      id integer PRIMARY KEY,
      title text NOT NULL,
      date text
   );
   """

   create_participants_sql = """
   -- participants table
   CREATE TABLE IF NOT EXISTS participants (
      id integer PRIMARY KEY,
      meeting_id integer NOT NULL,
      name VARCHAR(250) NOT NULL,
      surname VARCHAR(250) NOT NULL,
      status VARCHAR(15) NOT NULL,
      FOREIGN KEY (meeting_id) REFERENCES meetings (id)
   );
   """

   db_file = "database.db"
   conn = create_connection(db_file)

   if conn is not None:
       execute_sql(conn, create_meetings_sql)
       execute_sql(conn, create_participants_sql)
       conn.close()
