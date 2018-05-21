import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington).
    while True:

        try:
            city = input("Would you like to see data for Chicago, New York City, or Washington?\n")
        except Exception as e:
            print(e + " Please try again.")
            # return to the start of the the loop
            continue
        # ensure that the city input is valid
        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print(city + " is not a valid city. Please try again")
            continue
        else:
            #city was successfully parsed and ready to exit the loop
             break
    city = city.lower()

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Which month? Please choose either Jan, Feb, Mar, Apr, May, Jun, or all?\n")
        except Exception as e:
            print(e + " Please try again.")
            # return to the start of the the loop
            continue
        # ensure that the month input is valid
        if month.lower() not in ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all'):
            print(month + " is not a valid input. Please try again")
            continue
        else:
            # month was successfully parsed and ready to exit the loop
            break
    month = month.lower()

    # get user input for day (all, sunday, monday, ... , saturday)
    while True:
        try:
            day = input("Which day? Please choose either Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or all?\n")
        except Exception as e:
            print(e + " Please try again.")
            # Return to the start of the the loop
            continue
        # ensure that the day input is valid
        if day.lower() not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print(day + " is not a valid input. Please try again")
            continue
        else:
            # day was successfully parsed and ready to exit the loop
            break
    day = day

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = calendar.month_name[df['month'].value_counts().idxmax()]

    print("What is the most popular month for traveling?")
    print(common_month)
    # wait for 1 seconds
    time.sleep(1)

    # display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print("\nWhat is the most popular day for traveling?")
    print(common_day)
    # wait for 1 seconds
    time.sleep(1)

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("\nWhat is the most popular hour of the day to start your travels?")
    print(common_hour)
    # wait for 1 seconds
    time.sleep(1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Which station is the most popular to start your travel?")
    print(common_start_station)
    # wait for 1 seconds
    time.sleep(1)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("\nWhich  station is the most popular to end your travel?")
    print(common_end_station)
    # wait for 1 seconds
    time.sleep(1)

    # display most frequent combination of start station and end station trip
    print("\nWhat was the most popular trip from start to end?")
    start_and_end_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(start_and_end_station)
    # wait for 1 seconds
    time.sleep(1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def convert_seconds(seconds):
    """Convert seconds to days, hours, minutes and seconds."""

    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    return days, hours, minutes, seconds

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = int(df['Trip Duration'].sum())
    # display seconds in days, hours, minutes and seconds
    total_days, total_hrs, total_mins, total_seconds = convert_seconds(total_travel_time)
    print("What was the total traveling done for 2017 through {}?".format(calendar.month_name[df['month'].mode()[0]]))
    print(total_days, 'days', total_hrs, 'hours', total_mins, 'minutes', total_seconds, 'seconds')
    # wait for 1 seconds
    time.sleep(1)

    # display mean travel time
    mean_travel_time = int(df['Trip Duration'].mean())
    # display seconds in days, hours, minutes and seconds
    mean_days, mean_hrs, mean_mins, mean_seconds = convert_seconds(mean_travel_time)
    print("\nWhat was the average time spent on each trip?")
    print(mean_days, 'days', mean_hrs, 'hours', mean_mins, 'minutes', mean_seconds, 'seconds')
    # wait for 1 seconds
    time.sleep(1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts().to_csv(header=None,sep='\t')
    print("What is the breakdown of users?")
    print(user_types)
    # wait for 1 seconds
    time.sleep(1)

    # Display counts of gender
    print("What is the breakdown of gender?")
    try:
        gender_types = df['Gender'].value_counts().to_csv(header=None,sep='\t')
        print(gender_types)
    # print message when dataset does not have gender data
    except:
        print("Sorry, no gender data available for your selected city")
    # wait for 1 seconds
    time.sleep(1)

    # Display earliest, most recent, and most common year of birth
    print("\nWhat is the oldest, youngest, and most popular year of birth, respectively?")
    try:
        earliest_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode()[0])
        print('Oldest year:', earliest_birth)
        print('Youngest year:', recent_birth)
        print('Popular year:', common_birth)
    # print message when dataset does not have birth data
    except:
        print("Sorry, no birth data available for your selected city")
    # wait for 1 seconds
    time.sleep(1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def getFirstFive(df):

    '''
    Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.
    '''

    # check with user if they would like to display five lines of data
    while True:
        try:
            first_five = input('\nWould you like to view individual trip data? Enter \'yes\' or \'no\'.\n')
        except Exception as e:
            print(e + " Please try again.")
            # return to the start of the the loop
            continue
        # ensure that the month input is valid
        if first_five.lower() not in ('yes', 'no'):
            print(first_five + " is not a valid input. Please try again")
            continue
        else:
            # user input was successfully parsed and ready to exit the loop
            break

    x=0
    # display first five lines of data when user enter yes
    while(first_five.lower() == 'yes'):
        print("----------------------------------------")
        print(df[x:x+5])
        x += 5
        # display 'End of data' when reach end of dataset
        if x >= len(df.index):
            print("---------------End of data-------------------")
            break

        print("----------------------------------------")
        # check with user if interested to view five more individual trip data
        while True:
            try:
                first_five = input('\nWould you like to view five more individual trip data? Enter \'yes\' or \'no\'.\n')
            except Exception as e:
                print(e + " Please try again.")
                # return to the start of the the loop
                continue
            # ensure that the month input is valid
            if first_five.lower() not in ('yes', 'no'):
                print(first_five + " is not a valid input. Please try again")
                continue
            else:
                # user input was successfully parsed and ready to exit the loop
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        getFirstFive(df)

        restart = input('\nWould you like to restart? Enter \'yes\' or \'no\'.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
