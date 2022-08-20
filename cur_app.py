import database

#add many records


#this is a database file that calls functions which are defined in the database.py source which is also included in thos repository as database

def main():
    #establishing a connection 
    conn=database.create_connection('newsql3.db')
    
    
    table_name="""CREATE TABLE Member(
        USer_id      INTEGER,
        course_id    INTEGER,
          role       INTEGER,
        PRIMARY KEY   (User_id,course_id)
        
    );"""
    
    
    #creating a table using both the connection and the variable table name as parameters
    database.create_table(conn,table_name)
 #calling the function   
if __name__=='__main__':
    main()
    
   
