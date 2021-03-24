import csv
import cassandra
import getfullcsv as gfcsv
from sql_queries import insert_query1,insert_query2,insert_query3
from cassandra.cluster import Cluster

def connect_keyspace(dbName):
    """
    - Creates and connects to the sparkify database in Apache Cassandra
    :param dbName:Database name
    :return: the connection and cursor to sparkify
    """
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect() 
    session.set_keyspace(dbName)
 
    return cluster,session


def process_csv(session):
    """
    Read the csv file, load data into three tables in cassandra.
    :param session: Carssendra session
    """
    import csv
    file = 'event_datafile_new.csv'
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
            session.execute(insert_query1, (int(line[8]), int(line[3]),line[0],line[9],float(line[5])))
            session.execute(insert_query2, (int(line[10]),int(line[8]), int(line[3]),line[0],line[9],line[1],line[4]))
            session.execute(insert_query3, (line[9],int(line[10]),line[1],line[4]))
            
            

def main():
    """
    get full csv file event_datafile_new.csv to /home/workspace folder.
    Load data to the tables.
    """
    
    gfcsv.main()
    #Connect to the sparkify key space.
    cluster,session=connect_keyspace('sparkify')
    process_csv(session)
    
    session.shutdown()
    cluster.shutdown()
    
if __name__=="__main__":
    main()