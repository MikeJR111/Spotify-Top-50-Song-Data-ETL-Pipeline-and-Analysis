CREATE DATABASE country_playist ;
USE country_playist; 

CREATE TABLE Album (
  album_id VARCHAR(255) NOT NULL PRIMARY KEY,
  album_name VARCHAR(255),
  album_type VARCHAR(255),
  album_tracks INT,
  album_url VARCHAR(255),
  album_release_date DATE
);

CREATE TABLE Artist (
  artist_id VARCHAR(255) NOT NULL ,
  artist_name VARCHAR(255),
  artist_url VARCHAR(255),
  artist_genre VARCHAR(255),
  PRIMARY KEY (artist_id)
);


CREATE TABLE Track (
	track_id VARCHAR(255)  NOT NULL,
	album_id VARCHAR(255) NOT NULL,
	artist_id VARCHAR(255) NOT NULL,
	record_date DATE NOT NULL,
	track_url VARCHAR(255),
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
    track_preview VARCHAR(255),
	time_signature INT,
    PRIMARY KEY (track_id),
	FOREIGN KEY (album_id) REFERENCES Album(album_id),
	FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
);

CREATE TABLE Track_Popularity (
	record_date DATE,
	track_id VARCHAR(255)  NOT NULL,
    track_popularity INT,
    PRIMARY KEY (track_id, record_date),
	FOREIGN KEY (track_id) REFERENCES Track(track_id)
);

CREATE TABLE artist_tracking (
	record_date DATE,
	artist_id VARCHAR(255)  NOT NULL,
    artist_popularity INT,
    artist_followers INT,
    PRIMARY KEY (artist_id, record_date),
	FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
);

CREATE TABLE Playlist (
	playlist_id VARCHAR(255) NOT NULL,
    country_code VARCHAR(255) NOT NULL,
    country_name VARCHAR(255) ,
    PRIMARY KEY (playlist_id)
);

CREATE TABLE Playlist_Tracks (
	playlist_track_id VARCHAR(255) NOT NULL,
    playlist_id VARCHAR(255) NOT NULL,
    track_id VARCHAR(255) ,
    record_date DATE,
    PRIMARY KEY (playlist_id),
    FOREIGN KEY (playlist_id) REFERENCES Playlist(playlist_id),
    FOREIGN KEY (track_id) REFERENCES Track(track_id)
);
