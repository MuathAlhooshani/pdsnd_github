#!/usr/bin/env python
# coding: utf-8

# In[3]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Would you like to see data for Chicago, New York, or Washington?")
    city=city.title()
    while city!="Chicago" and city!="New York" and city!="Washington":
        print("wrong input: please enter one of the given cities")
        city=input("Would you like to see data for Chicago, New York, or Washington?")
        city=city.title()

    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    filters=input("Would you like to filter the data by month, day, both or not at all? Type 'none' for not at all")
    filters=filters.lower()
    while filters!="month" and filters!="day" and filters!="both" and filters!="none":
        print("wrong input: please enter one of the given options")
        filters=input("Would you like to filter the data by month, day, both or not at all? Type 'none' for not at all")
        filters=filters.lower()
    if filters=='none':
        month="all"
        day="all"
    if filters=="month":
        month=input("which month? 'january', 'february', 'march', 'april', 'may' or 'june'? please type out the full month name")
        month=month.lower()
        day="all"
        monthss = ['january', 'february', 'march', 'april', 'may', 'june']
        while month not in monthss:
            print("wrong input: please enter one of the given options")
            month=input("which month? 'january', 'february', 'march', 'april', 'may' or 'june'? please type out the full month name")
            month=month.lower()
            day="all"
    if filters=="day":
        day=input("which day? 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' or 'Sunday'? please type the full day name")
        day=day.title()
        month="all"
        dayss= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' , 'Sunday']
        while day not in dayss:
            print("wrong input: please enter one of the given options")
            day=input("which day? 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' or 'Sunday'? please type the full day name")
            day=day.title()
            month="all"
    if filters=="both":
        #month
        month=input("which month? 'january', 'february', 'march', 'april', 'may' or 'june'? please type out the full month name")
        month=month.lower()
        monthss = ['january', 'february', 'march', 'april', 'may', 'june']
        while month not in monthss:
            print("wrong input: please enter one of the given options")
            month=input("which month? 'january', 'february', 'march', 'april', 'may' or 'june'? please type out the full month name")
            month=month.lower()
        #day
        day=input("which day? 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' or 'Sunday'? please type the full day name")
        day=day.title()
        dayss= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' , 'Sunday']
        while day not in dayss:
            print("wrong input: please enter one of the given options")
            day=input("which day? 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' or 'Sunday'? please type the full day name")
            day=day.title()
        
        
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
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("most common month is: ",df["month"].mode()[0])

    # display the most common day of week
    print("most common day of the week is: ",df["day_of_week"].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('Most common start hour:', df['hour'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("most common start station is: ", df["Start Station"].mode()[0])
    
    # display most commonly used end station
    print("most common end station is: ", df["End Station"].mode()[0])

    # display most frequent combination of start station and end station trip
    df["combination"]="From: "+df["Start Station"]+" to: "+df["End Station"]
    print("most frequent combination of start station and end station trip is: ", df["combination"].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("total travel time in seconds is: ",df["Trip Duration"].sum())

    # display mean travel time
    print("the mean travel time in seconds is: ",df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)
    
    if city=="New York" or city=="Chicago":
        # Display counts of gender
        gender_types = df['Gender'].value_counts()

        print(gender_types)

        # Display earliest, most recent, and most common year of birth
        print("the most earliest year of birth is: ",df["Birth Year"].min())
        print("the most recent year of birth is: ",df["Birth Year"].max())
        print("the most common year of birth is: ",df["Birth Year"].mode()[0])
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data of 5 rows upon request under iteration"""
    choice=input("Do you want to see 5 lines of raw data? Enter yes or no")
    choice=choice.lower()
    x=0
    while choice=="yes":
        print(df[x:x+5])
        choice=input("Do you want to see next 5 lines of raw data? Enter yes or no")
        choice=choice.lower()
        x=x+5
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:




