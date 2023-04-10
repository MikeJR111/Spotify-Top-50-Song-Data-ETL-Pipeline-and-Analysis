### Step1: identify entities:
 
 ![image](https://user-images.githubusercontent.com/93886913/230839464-95202044-5a40-4d6e-8e1a-0967aae0d6c1.png)

### Step2: identify key attribute/s for each entity.
 
 ![image](https://user-images.githubusercontent.com/93886913/230839480-c1433ae9-9195-4a8b-893b-e2c8b0314cd5.png)


### Step 3: draw the relationships.
According to the missing value check, a track will always be assigned to an album 
 
![image](https://user-images.githubusercontent.com/93886913/230839504-00fb51a1-db2e-4e08-9dd1-e8ae4480d32f.png)

And this part of code shows that a track belongs to one album only, an album belongs to one artist only.
 
 ![image](https://user-images.githubusercontent.com/93886913/230839518-a49aff59-54e6-47da-bd48-193bd70725ed.png)
 
So the relationships:

![image](https://user-images.githubusercontent.com/93886913/230839588-f519dd3f-a337-4a83-8d6b-ce7ac2c19c0a.png)


### Step 4: add non-key attributes:

Record_date -> multivalued attribute
Popularity -> multivalued attribute
Artist popularity -> multivalued attribute
 
 ![image](https://user-images.githubusercontent.com/93886913/230839614-12380f96-cce9-4ad2-95fd-77b39eec219f.png)

### Step 5: remove multivalued attribute and create a new entity

![image](https://user-images.githubusercontent.com/93886913/230839638-8d904461-a0b7-4e99-af04-ba31b5cf900e.png)

### Step 6: Drawing Logical Model, Identify Primary Key and Foreign Key
 
![image](https://user-images.githubusercontent.com/93886913/230839659-b0237273-f41f-4c16-b1ad-a89f8b1274c0.png)

### Step7: Set constraint and add new entity based on case study

case: spotify has top songs playlist for country, all of these tracks are found from those playlists

Action: add playlist entity

![image](https://user-images.githubusercontent.com/93886913/230876226-268317ca-b376-4709-9f0e-434eb0720570.png)

A playlist contains one or more tracks, and a track can belong to one or more playlist, now it is a composite entity. Therefore, I will create a bridge entity: Playlist_track_id\

![image](https://user-images.githubusercontent.com/93886913/230897569-c9ad980f-8686-4e49-918c-34211393e4e7.png)
