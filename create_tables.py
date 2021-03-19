import cassandra
from sql_queries import create_table_queries, drop_table_queries


def create_keyspace():
    """
    - Creates and connects to the sparkify database in Apache Cassandra
    - Returns the connection and cursor to sparkify
    """
    from cassandra.cluster import Cluster
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    
    # create sparkify keyspace 
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS sparkify
        WITH REPLICATION = 
        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
    """)
    
    #set current keyspace to sparkify
    session.set_keyspace('sparkify')
  
    return cluster,session


def drop_tables(session):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        session.execute(query)



def create_tables(session):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        session.execute(query)



def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    session to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the session and shutdown the cluster. 
    """
    cluster,session = create_keyspace()
    
    drop_tables(session)
    create_tables(session)

    session.shutdown()
    cluster.shutdown()
    

if __name__ == "__main__":
    main()