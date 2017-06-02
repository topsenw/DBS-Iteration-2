
import MySQLdb
#Läd die Daten über MYSQL nach Verbindung mit der Datenbank
#über eine SQL Querie in die election Datenbank
#der Cursor ermöglicht die connection und execute führt die jeweiligen
#Sql Statements aus!
connection = MySQLdb.Connect(host='localhost', user='topsen', passwd='hallo123', db='election')
cursor = connection.cursor()
query1 = "LOAD DATA LOW_PRIORITY LOCAL INFILE 'C:/Users/topsen/Desktop/new-american-election.csv' INTO TABLE tweets CHARACTER SET ascii FIELDS TERMINATED BY ';' ENCLOSED BY '\"' ESCAPED BY '\"' LINES TERMINATED BY '\\r\n' IGNORE 1 LINES (`HANDLE`, `INHALT`, `IS_RETWEET`, `AUTHOR`, `DATUM`, `ANTWORT_AUF`, `RETWEETS`, `FAVORITES`, `TWEET_ID`);"
query2 = "LOAD DATA LOW_PRIORITY LOCAL INFILE 'C:/Users/topsen/Desktop/hashtags.csv' INTO TABLE hashtag CHARACTER SET ascii FIELDS TERMINATED BY ';' ENCLOSED BY '\"' ESCAPED BY '\"' LINES TERMINATED BY '\\r\n' (`INDEX_TWEET`, `HASHTAGS`, `HASHTAG_ID`);"
cursor.execute( query1 )
cursor.execute( query2 )
connection.commit()
