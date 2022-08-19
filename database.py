from sqlite3 import Error
import sqlite3


def create_connection(db_file):
    
    conn=None
    
    try:
        conn=sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def create_table(conn,name):
    
    
    try:
           cur=conn.cursor()
           cur.execute(name)
           print("commit successful")
           conn.commit()
           conn.close()
    except Error as e:
        print(e)
    

def show_all(conn,db_file):
    
    
    conn=sqlite3.connect(db_file)

    cur=conn.cursor()

    #create a table


    #update records

    
    cur.execute("SELECT rowid, * FROM Student ")
    items=cur.fetchall()


    for item in  items:
         print(item )
    #order by 

    # print("commit successful ")
    #commit the command
    conn.commit()

    #close the connection
    conn.close()
#add a new record to the table   
def add_one(first,last,age,mat_no):
    
    conn=sqlite3.connect('school_register.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO Student VALUES (?,?,?,?)",(first,last,age,mat_no))
    conn.commit()
    conn.close()

def delete_row(id):
    
    conn=sqlite3.connect('school_register.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM Student WHERE rowid=(?)",id)
    conn.commit()
    conn.close()

#add many records to table   
def add_many(list):
    
    conn=sqlite3.connect('school_register.db')
    cur=conn.cursor()
    cur.executemany("INSERT INTO Student VALUES (?,?,?,?)",(list))
    conn.commit()
    conn.close()

def lookup(age):
    
    conn=sqlite3.connect('school_register.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM Student WHERE age==(?)",(age,))
    items=cur.fetchall()
    
    for item in items:
        print(item)
    conn.commit()
    conn.close()
    