**Project Introduction**

**Project Goal**
The purpose of the NoSQL database we create is to store the song play history infomation by our users for
the management/marketing team to better understand our user preferences to the songs that offer by artists.
By looking at the tables, we will be able to know that the distribution of users and artist base on different
songs.


**Database Schema and ETL Pipeline**
The ETL data pipeline will process the data from even_data/* folder automatically every time it runs.
It will populate the three tables: artist_song_library, artist_song_user_library,and user_song_library. 
Each table has been defined primary key to ensure the 
table uniqueness and query by using the where clause.


**Sample Querys**
##1  Get the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4
/************************************************************************************
Description:
The query will return the artist name, song name, and song length base on the combination
input of sessionId and iteminsession.
************************************************************************************/
SELECT artist as "Artist Name",song as "Song Name", length as "Song Length" 
FROM artist_song_library WHERE sessionId=338 AND itemInSession=4




##2 Get only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
/************************************************************************************
Description:
The query will return the artist name, song name, and first name and last name of 
users base on the combination input of user id and session id.
************************************************************************************/
SELECT artist as "Artist Name",song as "Song Name",firstname as "User First Name",lastname as "User Last Name" 
FROM artist_song_user_library WHERE userid=10 AND sessionid=182




##3 Get every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'
/************************************************************************************
Description:
The query will return the user first name, user last name base on the 
input of song name.
************************************************************************************/
SELECT firstname as "User First Name",lastname as "User Last Name" 
FROM user_song_library WHERE song='All Hands Against His Own'


**Instruction on Python scripts**
First step: Open the test.ipynb, or create another new test file in your IDE.
second step:
Import the create_tables.py script and run the main function:

import create_tables
create_tables.main()
# This will create keyspaces, drop existing tables and recreates new.

Third step:
Import the etl.py file and run the main function:

import etl
etl.main()
# this will process the data file in data folder and produce a main csv file:"event_datafile_new.csv"
# And then load the data two three denomalized tables  artist_song_library, artist_song_user_library,and user_song_library.


**File description**
/data/even_data/../*.csv
This is the feed file that will populate the tables.

Create_tables.py
This is a script to create key space, refresh the tables in NoSQL database.


etl.py
ETL script that process the feed file and populate the tables.

sql_queries.py
Contains all the sql queries that used by create_tables/etl.py scripts.

test.ipynb
A place where you can do unit testing.