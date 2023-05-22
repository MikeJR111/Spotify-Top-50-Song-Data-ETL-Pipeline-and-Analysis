# Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis

As a student with a deep interest in data science, I'm eager to apply both my academic learnings and personal self-study to undertake a personal project.

### Objectives of this project:

1. **Data Extraction:** Efficiently extract relevant data from the Spotify API.
2. **Data Transformation:** Clean, normalize, and transform raw data into a suitable format for analysis, ensuring consistency and quality.
3. **Data Analysis:** Perform various analyses on the processed dataset to derive insights and actionable information.
4. **Data Visualization:** Create clear and concise visualizations to effectively communicate data analysis results.
5. **Data Storage:** Store processed and analyzed data in a suitable, scalable, secure, and maintainable storage solution.
6. **Automation and Scheduling:** Automate the ETL pipeline to run periodically, with error handling, logging, and monitoring mechanisms.





### High Level Diagram:

![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/cd5cab8e-ad4a-4c63-9bb6-edaf8d6ed563)

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

### About Extraction:

## Spotify API, Python library spotipy:

Spotipy is a lightweight Python library for the Spotify Web API. With Spotipy you get full access to all of the music data provided by the Spotify platform.

Register a Spotify for developers to get the **SPOTIPY_CLIENT_ID** and **SPOTIPY_CLIENT_SECRET** environment variables. Then you can interact with spotipy like this: 

```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
```

My objective is to extract countries' TOP 50 tracks playlist:
```python
# These countries were chosen based on their respective market shares in the Spotify platform.
countries = ["United States", "India", "Brazil", "Mexico", "United Kingdom", "Germany", "Sweden"]
sp.search(q=f'top 50 India', type='playlist')['playlists']
```
![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/b89e3d68-8601-47ac-bb30-7a29b28a3b98)

you can use this script to play with the spotify API [API_test.ipynb](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/blob/main/Data%20Governance/api_test.ipynb)

### Deploy Extraction Script on AWS Lambda

#### layer setting
![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/83c7a711-e925-4a62-aafa-7e1a8d911384)

#### Triggers setting
![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/4f770835-4349-4746-80b9-8ee6c3757ce4)

#### Scripts:
[Lambda_Spotify_data_extraction_and_transform.ipynb](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/blob/main/Data%20Governance/Lambda_Spotify_data_extraction.ipynb)

![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/871ae0a3-6c64-49c8-877a-2a7450078dc8)


### Data Extracted:
![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/c2a7a883-be24-4546-9bab-d133559020e7)

### Data Transformed:
![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/99d7e165-5a9f-4fe7-8ed0-eb91af541db6)

![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/7a33f064-26cb-4414-a802-249df0b4347a)


### Load into Redshift:

#### query to create database:



## Dashboard

<div class='tableauPlaceholder' id='viz1680359791067' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sp&#47;SpotifyTracks_16803596672260&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></no

  
  Link:https://public.tableau.com/views/SpotifyTracks_16803596672260/Dashboard1?:language=zh-CN&publish=yes&:display_count=n&:origin=viz_share_link
