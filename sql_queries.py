# DROP TABLES
drop_query1_table="DROP TABLE IF EXISTS artist_song_library"
drop_query2_table="DROP TABLE IF EXISTS artist_song_user_library"
drop_query3_table="DROP TABLE IF EXISTS user_song_library"

# CREATE TABLES
create_query1_table="""
        CREATE TABLE IF NOT EXISTS artist_song_library
        (sessionid int, iteminsession int,artist varchar,song varchar,length float,PRIMARY KEY(sessionId,itemInSession))
"""
create_query2_table="""
    CREATE TABLE IF NOT EXISTS artist_song_user_library (
                                                          userid int,sessionid int,iteminsession int,artist varchar,
                                                          song varchar,firstname varchar,lastname varchar,
                                                          PRIMARY KEY((userid,sessionid),iteminsession)
                                                        )
"""

create_query3_table="""
    CREATE TABLE IF NOT EXISTS user_song_library (
                                                          song varchar,userid int,firstname varchar,lastname varchar,
                                                          PRIMARY KEY(song,userid)
                                                  )
"""

# INSERT RECORDS
insert_query1="""
            INSERT INTO artist_song_library (sessionid, iteminsession,artist,song,length)
             VALUES (%s, %s, %s, %s, %s)
"""
insert_query2="""INSERT INTO artist_song_user_library (userid,sessionid,iteminsession,artist,song,firstname,lastname)
             VALUES (%s, %s, %s, %s, %s,%s, %s)
"""
insert_query3 ="""INSERT INTO user_song_library (song ,userid,firstname ,lastname)
             VALUES (%s, %s,%s, %s)
"""

# QUERY LISTS
create_table_queries = [create_query1_table, create_query2_table, create_query3_table]
drop_table_queries = [drop_query1_table, drop_query2_table, drop_query3_table]
