# Udacity DAND Project2 - Explore US Bikeshare Data
Udacity Data Analyst Nanodegree Project 02 - Explore US Bikeshare Data using Python

## Description
This project make use of Python to explore the data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. The script takes in raw input to create an interactive experience in the terminal and answer interesting questions about it by computing descriptive statistics.

### The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

Start Time (e.g., 2017-01-01 00:07:57) End Time (e.g., 2017-01-01 00:20:53) Trip Duration (in seconds - e.g., 776) Start Station (e.g., Broadway & Barry Ave) End Station (e.g., Sedgwick St & North Ave) User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

Gender Birth Year

### Statistics Computed
Learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics:

#### 1. Popular times of travel (i.e., occurs most often in the start time)

- most common day of week
- most common hour of day

#### 2. Popular stations and trip

- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

#### 3. Trip duration

- total travel time
- average travel time

#### 4. User info

- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Files
1. ```chicago.csv``` contains bike share systems data for United States - Chicago.
2. ```new_york_city.csv``` contains bike share systems data for United States - New York.
3. ```washington.csv``` contains bike share systems data for United States - Washington.
4. ```understand_Dataset.ipynb``` uses pandas to better understand the bike share dataset.
5. ```bikeshare.py``` contains Python code to import US bike share data and answer interesting questions about it by computing descriptive statistics.
6. ```bikeshare.ipynb``` is the Jupyter Notebook version of bikeshare.py.  
