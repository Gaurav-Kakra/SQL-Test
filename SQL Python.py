import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_Movies(conn, Movies):
    sql = """INSERT INTO Movies(Sr_no, Movie_name, Actor_name, Actress_name, Director_name, year_of_release)VALUES(?,?,?,?,?,?)"""
    c = conn.cursor()
    c.execute(sql,Movies)
    conn.commit()

def select_all_Movies(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Movies")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_Movie_by_actor(conn, actor):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param actor:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT Movie_name FROM Movies WHERE Actor_name=?", (actor,))

    rows = cur.fetchall()

    for row in rows:
        print(row)
        
def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    sql_create_Movies_table =  """CREATE TABLE IF NOT EXISTS Movies (
                                        Sr_no integer PRIMARY KEY,
                                        Movie_name text NOT NULL,
                                        Actor_name text,
                                        Actress_name text,
                                        Director_name text,
                                        year_of_release text
                                    );"""


    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_Movies_table)

    else:
        print("Error! cannot create the database connection.")


        

    with conn:
        Movie_1 = (1, "Mimi", "Pankaj Tripathi", "Kriti Sanaon", "Laxman Utekar", "2021-07-26")
        Movie_2 = (2, "Piku", "Amitabh Bacchhan", "Deepika Padukone", "Shoojit Sircar", "2015-05-08")
        Movie_3 = (3, "Baby", "Akshay Kumar", "Madhurima Tuli", "Neeraj Pandey", "2015-01-23")
        Movie_4 = (4, "Jolly LLB 2", "Akshay Kumar", "Huma Querishi", "Subhash Kapoor", "2017-02-10")
        Movie_5 = (5, "3 Idiots", "Aamir Khan", "Kareena Kapoor", "Rajkumar Hirani", "2009-12-25")

        create_Movies(conn,Movie_1)
        create_Movies(conn, Movie_2)
        create_Movies(conn, Movie_3)
        create_Movies(conn, Movie_4)
        create_Movies(conn, Movie_5)

        select_all_Movies(conn)
        select_Movie_by_actor(conn,"Akshay Kumar")

if __name__ == '__main__':
    main()