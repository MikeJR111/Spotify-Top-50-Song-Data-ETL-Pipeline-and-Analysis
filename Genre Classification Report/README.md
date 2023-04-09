# Genre Classification Report

### Objectives:

Select Feature from the dataset and predict genre


### Columns:
| Feature | Description |
| --- | --- |
| genre | The genre of the track (e.g., rock, pop, hip-hop) |
| danceability | The suitability of the track for dancing, based on a combination of musical elements including tempo, rhythm stability, and beat strength |
| energy | The perceived intensity and activity level of the track, based on features such as loudness, dynamic range, and timbre |
| key | The key in which the track is performed, representing a group of pitches that are related to each other and create a sense of tonality |
| loudness | The average volume of the track, measured in decibels (dB) |
| mode | The modality (major or minor) of the track, which can influence the emotional character of the music |
| speechiness | The presence of spoken words or vocal fragments in the track, measured as a ratio of speech-like sounds to musical sounds |
| acousticness | The likelihood that the track was recorded using acoustic instruments or without electronic amplification or processing |
| instrumentalness | The degree to which the track contains no vocals, measured as a ratio of instrumental sounds to vocal sounds |
| liveness | The perceived presence of an audience in the recording, measured as a ratio of audience sounds to non-audience sounds |
| valence | The positivity or negativity of the emotional content of the track, based on musical features such as chord progressions, timbre, and rhythm |
| tempo | The speed or pace of the track, measured in beats per minute (BPM) |
| duration_ms | The length of the track, measured in milliseconds (ms) |
| time_signature | The meter or rhythm of the track, represented as a fraction of beats per bar |
| track_popularity | The popularity of the track, as determined by the number of streams or listens on a particular platform or service |

Numberof rows: 3563

Snippet of Data:

![image](https://user-images.githubusercontent.com/93886913/230718076-c6162ab0-5ba5-44aa-8b9b-888a83ba37f7.png)

### Step1: remove duplicate rows by track name

![image](https://user-images.githubusercontent.com/93886913/230718243-3666eace-501b-4e0d-8684-16b298c5b896.png)

before drop:  3563 ; 
after drop:  949

### Step2: Select Features and change data type:

![image](https://user-images.githubusercontent.com/93886913/230718301-6f517849-5687-4dcb-9f81-512c16d1108d.png)

 shows the top genres only to maintain a readable aesthetic. It is clear that the majority of the songs in the dataset belong to the rock and pop category
 
 ![image](https://user-images.githubusercontent.com/93886913/230718345-f47561a8-baff-437e-b350-f123a545da2c.png)

### Step3 Check multicollinearity;

I used LabelEncoder to convert label to numeric value,  This will help me identify which features have a strong positive or negative correlation with the target variable. and also a good practice to check for multicollinearity, for now everything looks cool, because there is no correlation greater than 0.80

![image](https://user-images.githubusercontent.com/93886913/230718401-df3c2da0-2f3b-4620-ab6c-8571d8dd89ee.png)

### Step4 Check distrubution and outlies;

![image](https://user-images.githubusercontent.com/93886913/230718431-4753ded1-0403-4dae-a645-d3f2a41b1977.png)

The histograms above show that features are skewed, the reason for this skew could be outliers. and according to the boxplot below, there are outliers and features are not on the same scale, for now it is hard visualize them on the same chart. If we are going to use KNN or other machine learning model that relies on distance measures or optimization techniques. Then we should consider scaling our data, scaling ensures that each feature has a similar range of values and contributes equally to the analysis or model

![image](https://user-images.githubusercontent.com/93886913/230718492-dad83305-bb0f-4e6c-92ee-c1eae36b6fdd.png)

### Step4 Remove Outliers:

Use duration_ms as an example. According to these boxplots, we can see different genre has different IQR. Clearly a track at rock genre up quarter range is an outlier to rap genre. To remove the outlier, we should remove it genre by genre 

![image](https://user-images.githubusercontent.com/93886913/230720005-847b96b6-a532-4065-94c5-719d0bc99ee0.png)

![image](https://user-images.githubusercontent.com/93886913/230720172-278a250c-d02e-488d-8a69-0f659b75ce43.png)

### Step5 Transformation:

for feature 'key','time_signature'and 'mode'.

I will use time_signature as an example,  it is a convention in Western musical notation to specify how many of a particular note value are contained in each measure. So these features are categorical 

So I will apply one hot encoding to these features:

![image](https://user-images.githubusercontent.com/93886913/230720224-dcac6960-9cc7-4999-aaf5-61160ea0fe75.png)

I also changed duration_ms to duration_minutes

One of the disadvantage of one-hot encoding is that it produces multicollinearity among the various variables, lowering the model's accuracy. Hence lets check the correlation again. Found two features and removed from dataframe

![image](https://user-images.githubusercontent.com/93886913/230720268-4bec68dd-7da3-4fbb-86a8-f5400a337af6.png)

### Step6 choose the model and make prediction:

I will use RandomForestClassifier and LogisticRegression to predict genre.

1.RandomForestClassifier is an ensemble model that combines multiple decision trees to make predictions. It is particularly effective when there are complex interactions between the features and the target variable, and can handle both categorical and numerical features. 

2.LogisticRegression is a linear model that estimates the probability of a binary or categorical outcome based on the values of the input features. It is fast and simple to implement, and can handle large datasets with many features. 

![image](https://user-images.githubusercontent.com/93886913/230721295-0b07d450-7e6d-4bf7-8b2a-34886adc3a62.png)

The accuracy score was lower when the selected model was applied to the test data,  this could indicate that the model is overfitting the training data.

### Possible Solutions:

1. Collect more data: Having more data can help the model learn the underlying patterns better and reduce the impact of noise. In the dataset, many genre has no more than 5 tracks
2. Simplify the model: Using a simpler model with fewer features or fewer parameters can reduce the risk of overfitting. I can also use regularization techniques, such as L1 or L2 regularization
3. Use cross-validation

