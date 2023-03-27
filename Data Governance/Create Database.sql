CREATE DATABASE songsDB ;
USE songsDB; 

CREATE TABLE Albums (
  album_id VARCHAR(255) NOT NULL PRIMARY KEY,
  album_name VARCHAR(255),
  album_type VARCHAR(255),
  album_tracks INT,
  album_url VARCHAR(255),
  album_release_date DATE
);

CREATE TABLE Artists (
  artist_id VARCHAR(255) NOT NULL ,
  artist_name VARCHAR(255),
  artist_url VARCHAR(255),
  artist_genre VARCHAR(255),
  artist_followers INT,
  artist_popularity INT,
  record_date DATE Not NUll,
  PRIMARY KEY (artist_id, record_date)
);


CREATE TABLE Tracks (
	track_id VARCHAR(255)  NOT NULL,
	album_id VARCHAR(255) NOT NULL,
	artist_id VARCHAR(255) NOT NULL,
	record_date DATE NOT NULL,
	track_url VARCHAR(255),
	track_popularity INT,
	danceability FLOAT,
	energy FLOAT,
	key_ INT,
	loudness FLOAT,
	mode_ INT,
	speechiness FLOAT,
	acousticness FLOAT,
	instrumentalness FLOAT,
	liveness FLOAT,
	valence FLOAT,
	tempo FLOAT,
	duration_ms INT,
	time_signature INT,
    PRIMARY KEY (track_id, record_date),
	FOREIGN KEY (album_id) REFERENCES Albums(album_id),
	FOREIGN KEY (artist_id, record_date) REFERENCES Artists(artist_id, record_date)
);
