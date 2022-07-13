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

def add_meeting(conn, meeting):
   """
   Create a new meeting into the meetings table
   :param conn:
   :param meeting:
   :return: meeting id
   """
   sql = '''INSERT INTO meetings(title, date)
             VALUES(?,?)'''
   cur = conn.cursor()
   cur.execute(sql, meeting)
   conn.commit()
   return cur.lastrowid

def add_participant(conn, participant):
   """
   Create a new participant into the participants table
   :param conn:
   :param participant:
   :return: participant id
   """
   sql = '''INSERT INTO participants(meeting_id, name, surname, status)
             VALUES(?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, participant)
   conn.commit()
   return cur.lastrowid

if __name__ == "__main__":
   meeting = ("Obiad", "2022-07-15 14:30:00")
   
   conn = create_connection("database.db")

   meeting_id = add_meeting(conn, meeting)
   
   participant = (
       meeting_id,
       "Jan",
       "Kowalski",
       "potwierdzony"
   )

   participant_id = add_participant(conn, participant)

   print(meeting_id, participant_id)
   conn.commit()