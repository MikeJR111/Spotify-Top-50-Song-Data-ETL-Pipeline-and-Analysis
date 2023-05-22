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

### layer setting
![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/83c7a711-e925-4a62-aafa-7e1a8d911384)

### Triggers setting
![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/4f770835-4349-4746-80b9-8ee6c3757ce4)

### Scripts:
[Lambda_Spotify_data_extraction_and_transform.ipynb](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/blob/main/Data%20Governance/Lambda_Spotify_data_extraction.ipynb)

![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/871ae0a3-6c64-49c8-877a-2a7450078dc8)


### Data Extracted:
![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/c2a7a883-be24-4546-9bab-d133559020e7)

### Data Transformed:
![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/99d7e165-5a9f-4fe7-8ed0-eb91af541db6)

![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/7a33f064-26cb-4414-a802-249df0b4347a)


## About Database:

### Relational database schema:

How this relational databse is designed [click](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/tree/update/Data%20Governance/Data%20Model%20Design)

![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/727ba521-bfbd-4f74-8647-a3a84ea0a786)

### Star Schema
![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/78c1addb-2ffe-4ec6-b94d-02eff5db0ac3)

### Query to create the star schema database:
[sql_queries.py](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/blob/update/Data%20Governance/sql_queries.py)

Create database code
```python
import sys
sys.path.insert(0, 'E:\\StuDY\\Keys')
from db_credentials import *
import redshift_connector
from sql_queries import table_list, staging_table_list

conn = redshift_connector.connect(
    host = spotify_redshift_host, 
    database = spotify_redshift_db,
    user = spotify_redshift_user,
    password = spotify_redshift_password

)

cursor = redshift_connector.Cursor = conn.cursor()

#create tables
for query in table_list:
    cursor.execute(query)
    print('Table created.') 
conn.commit()   

#create staging tables
for query in staging_table_list:
    cursor.execute(query)
    print('Table created.') 
conn.commit()  

```

### Load into redshift:
SQL Code Example:

```SQL
COPY artist_dim
FROM 's3://spotify-project-jr/transformed_data/artist/'
IAM_ROLE 'YOUR IAM ROLE'
DATEFORMAT 'auto'
DELIMITER ','
IGNOREHEADER 1
REGION 'ap-southeast-2';
```
**Problem**: This loading is not automated, I am still working on this part. My objective is to use lambda function to automate this process. I will modify the SQL code as well, use left join to filter duplicate rows before insert data.

## About Monitoring:
I use AWS cloudwatch to monitor my ETL pipeline, if any part is failed, I will recevie an E-mail from AWS notification:
![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/a93bcd46-bb34-4f39-81f9-6c871728a877)
![image](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/assets/93886913/0f90ae2d-0be6-4ad9-8bcb-03982ed81c0b)


### Classification:
[classification report](https://github.com/MikeJR111/Spotify-Top-50-Song-Data-ETL-Pipeline-and-Analysis/tree/update/Genre%20Classification%20Report)

### Data Analysis：
### Dashboard

<div class='tableauPlaceholder' id='viz1680359791067' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sp&#47;SpotifyTracks_16803596672260&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></no

  
Link:https://public.tableau.com/views/SpotifyTracks_16803596672260/Dashboard1?:language=zh-CN&publish=yes&:display_count=n&:origin=viz_share_link
    
    

### My other projects:
    
### PySpark Project: 
    
**Analyzing Trip Data:**
    
implement various solutions based on RDDs, SQL and Data Frames in PySpark for the given queries related to trip data analysis.
    
[Github Link](https://github.com/MikeJR111/pyspark-projects/tree/main/Analysing%20Trip%20Data)
    
### Data Wrangling Project: 
    
**Semi-Structured-Data-Manipulation:**

Use Python to extract the data from the text file and transform the data into a required XML format.
    
[Github Link](https://github.com/MikeJR111/Data-Wrangling/tree/main/Semi-Structured-Data-Manipulation)
    
**Data Cleansing :**
   
write Python code to analyze dataset, find and fix the problems (dirty, missing and outlier) in the data.
    
[Github Link](https://github.com/MikeJR111/Data-Wrangling/tree/main/Data-Cleansing)
    
**Data Integration and Reshaping:**
    
Write Python code to integrate several datasets into one single schema and find and fix possible problems in the data.
Enriching Datasets with Web Scarping.
    
[Github Link](https://github.com/MikeJR111/Data-Wrangling/tree/main/Semi-Structured-Data-Manipulation)

### Data Modelling Project:
    
Create a conceptual model based on a case study

[Github Link](https://github.com/MikeJR111/Data-Modelling-/tree/main/conceptual_model)

Based on a case study, create a 3nf normalization form and build a logical data model

[Github Link](https://github.com/MikeJR111/Data-Modelling-/tree/main/Normalisation%20and%20Logical%20Database%20Design)
    
Based on a case study and a given data model, use SQL query to manipulate the database:

[Github Link](https://github.com/MikeJR111/Data-Modelling-/tree/main/Creating%2C%20Populating%20and%20Manipulating%20Database)    

    
### Docker Project:
Build a web-based system. It will allow end-users to send an image to a web service hosted by Docker containers and receive a list of objects detected in their uploaded image. Then deploy the web service on Oracle Cloud instances. Modify the VPC that allows my local machine to send data using the client.

[Github Link](https://github.com/MikeJR111/First-Docker-Practice)
