#create database
artist_dim =("""
    CREATE TABLE IF NOT EXISTS artist_dim (
        artist_id VARCHAR(255),
        artist_name VARCHAR(255),
        artist_url VARCHAR(255),
        artist_image VARCHAR(255)
    );
""")

date_dim =("""
    CREATE TABLE IF NOT EXISTS date_dim (
        date_id varchar(255) SORTKEY,
        record_date varchar(255) 
    );
    """)

tracks_dim =("""
    CREATE TABLE IF NOT EXISTS tracks_dim (
        track_id VARCHAR(255) ,
        track_name VARCHAR(255),
        track_url VARCHAR(255),
        track_preview VARCHAR(255),
        genre VARCHAR(255),
        album_id VARCHAR(255),
        album_name VARCHAR(255),
        album_url VARCHAR(255),
        album_image VARCHAR(255),
        danceability DECIMAL(10, 8),
        energy DECIMAL(10,8),
        key INTEGER,
        loudness DECIMAL(10,8),
        mode INTEGER,
        speechiness DECIMAL(10,8),
        acousticness VARCHAR(255),
        instrumentalness VARCHAR(255),
        liveness DECIMAL(10,8),
        valence DECIMAL(10,8),
        tempo DECIMAL(10, 6),
        duration_ms INTEGER,
        time_signature INTEGER
    );
    """)
        
fact_playlist =("""
    CREATE TABLE IF NOT EXISTS fact_playlist (
        playlist_id VARCHAR(255),
        track_id VARCHAR(255),
        artist_id VARCHAR(255),
        date_id VARCHAR(255) SORTKEY ,
        country VARCHAR(255)
    );
    """)

track_popularity_dim = ("""
    CREATE TABLE IF NOT EXISTS track_popularity_dim (
        track_id VARCHAR(255),
        date_id VARCHAR(255) SORTKEY,
        track_popularity INTEGER
    );
    """)


artist_popularity_dim = ("""
    CREATE TABLE IF NOT EXISTS artist_popularity_dim (
        artist_id VARCHAR(255),
        date_id VARCHAR(255) SORTKEY,
        artist_popularity INTEGER,
        artist_followers INTEGER
    );
    """
)

#query list
table_list = [artist_dim, date_dim, tracks_dim, fact_playlist, track_popularity_dim, artist_popularity_dim]

staging_artist_dim = ("CREATE TABLE IF NOT EXISTS staging_artist_dim (LIKE artist_dim);")
staging_date_dim = ("CREATE TABLE IF NOT EXISTS staging_date_dim (LIKE date_dim);")
staging_tracks_dim = ("CREATE TABLE IF NOT EXISTS staging_tracks_dim (LIKE tracks_dim);")
staging_fact_playlist = ("CREATE TABLE IF NOT EXISTS staging_fact_playlist (LIKE fact_playlist);")
staging_track_popularity_dim = ("CREATE TABLE IF NOT EXISTS staging_track_popularity_dim (LIKE track_popularity_dim);")
staging_artist_popularity_dim = ("CREATE TABLE IF NOT EXISTS staging_artist_popularity_dim (LIKE artist_popularity_dim);")

# staging table query list
staging_table_list = [staging_artist_dim, staging_date_dim, staging_tracks_dim, 
                      staging_fact_playlist, staging_track_popularity_dim, staging_artist_popularity_dim]

### with primary key and foreign key:
#create database
# artist_dim =("""
#     CREATE TABLE IF NOT EXISTS artist_dim (
#         artist_id VARCHAR(255) PRIMARY KEY,
#         artist_name VARCHAR(255),
#         artist_url VARCHAR(255),
#         artist_image VARCHAR(255)
#     );
# """)

# date_dim =("""
#     CREATE TABLE IF NOT EXISTS date_dim (
#         date_id varchar(255) PRIMARY KEY,
#         record_date varchar(255) 
#     );
#     """)

# tracks_dim =("""
#     CREATE TABLE IF NOT EXISTS tracks_dim (
#         track_id VARCHAR(255) PRIMARY KEY,
#         track_name VARCHAR(255),
#         track_url VARCHAR(255),
#         track_preview VARCHAR(255),
#         genre VARCHAR(255),
#         album_id VARCHAR(255),
#         album_name VARCHAR(255),
#         album_url VARCHAR(255),
#         album_image VARCHAR(255),
#         danceability DECIMAL(10, 8),
#         energy DECIMAL(10,8),
#         key INTEGER,
#         loudness DECIMAL(10,8),
#         mode INTEGER,
#         speechiness DECIMAL(10,8),
#         acousticness VARCHAR(255),
#         instrumentalness VARCHAR(255),
#         liveness DECIMAL(10,8),
#         valence DECIMAL(10,8),
#         tempo DECIMAL(10, 6),
#         duration_ms INTEGER,
#         time_signature INTEGER
#     );
#     """)
        
# fact_playlist =("""
#     CREATE TABLE IF NOT EXISTS fact_playlist (
#         playlist_id VARCHAR(255),
#         track_id VARCHAR(255),
#         artist_id VARCHAR(255),
#         date_id VARCHAR(255),
#         country VARCHAR(255),
#         PRIMARY KEY (playlist_id, track_id, artist_id, date_id),
#         FOREIGN KEY (track_id) REFERENCES tracks_dim(track_id),
#         FOREIGN KEY (artist_id) REFERENCES artist_dim(artist_id),
#         FOREIGN KEY (date_id) REFERENCES date_dim(date_id)
#     );
#     """)

# track_popularity_dim = ("""
#     CREATE TABLE IF NOT EXISTS track_popularity_dim (
#         track_id VARCHAR(255),
#         date_id VARCHAR,
#         track_popularity INTEGER,
#         PRIMARY KEY (track_id, date_id),
#         FOREIGN KEY (track_id) REFERENCES tracks_dim(track_id),
#         FOREIGN KEY (date_id) REFERENCES date_dim(date_id)
#     );
#     """)


# artist_popularity_dim = ("""
#     CREATE TABLE IF NOT EXISTS artist_popularity_dim (
#         artist_id VarChar(255),
#         date_id varchar(255),
#         artist_popularity INTEGER,
#         artist_followers INTEGER,
#         PRIMARY KEY (artist_id, date_id),
#         FOREIGN KEY (artist_id) REFERENCES artist_dim(artist_id),
#         FOREIGN KEY (date_id) REFERENCES date_dim(date_id)
#     );
#     """
# )