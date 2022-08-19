import database

#add many records




def main():
    
    conn=database.create_connection('newsql3.db')
    
    
    table_name="""CREATE TABLE Member(
        USer_id      INTEGER,
        course_id    INTEGER,
          role       INTEGER,
        PRIMARY KEY   (User_id,course_id)
        
    );"""
    
    
    
    database.create_table(conn,table_name)
    
if __name__=='__main__':
    main()
    
   