# Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis


### Objectives of this project:

1. **Data Extraction:** Efficiently extract relevant data from the Spotify API, ensuring scalability for large volumes of data.
2. **Data Transformation:** Clean, normalize, and transform raw data into a suitable format for analysis, ensuring consistency and quality.
3. **Data Integration:** Combine and integrate data from different Spotify API sources to create a comprehensive dataset.
4. **Data Analysis:** Perform various analyses on the processed dataset to derive insights and actionable information.
5. **Data Visualization:** Create clear and concise visualizations to effectively communicate data analysis results.
6. **Data Storage:** Store processed and analyzed data in a suitable, scalable, secure, and maintainable storage solution.
7. **Automation and Scheduling:** Automate the ETL pipeline to run periodically, with error handling, logging, and monitoring mechanisms.
8. **Performance Optimization:** Continuously optimize the ETL pipeline for improved efficiency, scalability, and performance.
9. **Documentation and Collaboration:** Document the ETL pipeline's design, implementation, and usage for easy understanding and maintenance.


### Tasks will be done: (Currently 70% done)

1. re-create the data model

2. change the database from RDS to redshift, and make the dashboard that automatically update once a day

3. re-structure the repository, make it more prefessional

### ETL pipeline problem encountered so far

1. spotify modified their api, so I have to re-write few lines of code

2. spotify removed some playlists, re-write the code using try except, so if the playlist is empty, continue the loop 




### ETL Pipeline flowchart:

![image](https://user-images.githubusercontent.com/93886913/230753090-02821699-2266-405f-84bf-8bf1b4a92c97.png)

### Data Extracted from Spotify API

| Column Name        | Description                     |
|--------------------|---------------------------------|
| track_id           | Unique identifier for the track |
| track_name         | Name of the track               |
| track_url          | URL to the track on Spotify     |
| track_popularity   | Popularity score of the track   |
| album_id           | Unique identifier for the album |
| album_name         | Name of the album               |
| countries          | Countries where album is available |
| album_url          | URL to the album on Spotify     |
| album_image        | Album cover image URL           |
| track_preview      | URL to a track preview          |
| artist_id          | Unique identifier for the artist |
| artist_name        | Name of the artist              |
| artist_url         | URL to the artist on Spotify    |
| artist_image       | Artist's profile image URL      |
| artist_genre       | Artist's genre(s)               |
| artist_followers   | Number of followers for the artist |
| artist_popularity  | Popularity score of the artist  |
| record_date        | Date when the data was recorded |
| Country            | Country associated with the track |
| danceability       | Danceability score of the track |
| energy             | Energy score of the track       |
| key                | Key of the track                |
| loudness           | Loudness of the track           |
| mode               | Mode of the track (major/minor) |
| speechiness        | Speechiness score of the track  |
| acousticness       | Acousticness score of the track |
| instrumentalness   | Instrumentalness score of the track |
| liveness           | Liveness score of the track     |
| valence            | Valence (mood) score of the track |
| tempo              | Tempo (BPM) of the track        |
| duration_ms        | Duration of the track in milliseconds |
| time_signature     | Time signature of the track     |

## Dashboard

<div class='tableauPlaceholder' id='viz1680359791067' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sp&#47;SpotifyTracks_16803596672260&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></no

  
  Link:https://public.tableau.com/views/SpotifyTracks_16803596672260/Dashboard1?:language=zh-CN&publish=yes&:display_count=n&:origin=viz_share_link
