

CREATE DATABASE AmericanElectionTweets;#Erstellt MYSQL Datenbank

CREATE TABLE Tweets(#Erstellt Tabelle mit Werten für Entität Tweet

	HANDLE varchar(20),
	INHALT varchar(256) not null,
	IS_RETWEET tinyint not null,
	AUTHOR varchar(30),
	DATUM datetime not null,
	ANTWORT_AUF varchar(30),
	RETWEETS int not null,
	FAVORITES int not null,
	TWEET_ID int not null AUTO_INCREMENT,
	PRIMARY KEY (TWEET_ID)
);


#SQL Befehl für das Laden der Tweet CSV Daten in den Table Hashtag
#wird im Python Datenimport verwendet
LOAD DATA LOW_PRIORITY LOCAL INFILE 'C:\\Users\\topsen\\Desktop\\new-american-election.csv' 
INTO TABLE `americanelectiontweets`.`tweets` 
CHARACTER SET ascii FIELDS 
TERMINATED BY ';' 
ENCLOSED BY '"' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n' 
IGNORE 1 LINES (`HANDLE`, `INHALT`, `IS_RETWEET`, `AUTHOR`, `DATUM`, `ANTWORT_AUF`, `IS_QUOTE`, `RETWEETS`, `FAVORITES`, `TWEET_ID`);


CREATE TABLE Hashtag(#Erstellt Tabelle mit Werten für Entität Hashtags
	INDEX_TWEET int not null,
	HASHTAGS varchar(256) not null,
	HASHTAG_ID int not null AUTO_INCREMENT,
	PRIMARY KEY (HASHTAG_ID)
);

#SQL Befehl für das Laden der HASHTAG CSV Daten in den Table Hashtag
#wird im Python Datenimport verwendet
LOAD DATA LOW_PRIORITY LOCAL INFILE 'C:\\Users\\topsen\\Desktop\\hashtags.csv' 
INTO TABLE `americanelectiontweets`.`hashtag` 
CHARACTER SET ascii FIELDS 
TERMINATED BY ';' 
ENCLOSED BY '"' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n' (`INDEX_TWEET`, `HASHTAGS`, `HASHTAG_ID`);

#LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/american-election.csv" INTO table all_data
#       columns terminated by ";"
#       lines terminated by "\n"
#       ignore 1 lines;

#Erstellt Tabelle für die Relation Contains
CREATE TABLE Contains
	HASHTAG_ID INT NOT NULL,
	TWEET_ID INT NOT NULL,
	PRIMARY KEY (HASHTAG_ID, TWEET_ID),
  	CONSTRAINT HASHTAG_ID
    	   FOREIGN KEY ()
   	   REFERENCES AmericanElectionTweets.Hashtag ()
   	   ON DELETE NO ACTION
   	   ON UPDATE NO ACTION,
  	CONSTRAINT TWEET_ID
    	   FOREIGN KEY ()
    	   REFERENCES AmericanElectionTweets.Tweets ()
   	   ON DELETE NO ACTION
    	   ON UPDATE NO ACTION
);
