import time
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
    # get user input for city (Chicago, New York, Washington). HINT: Use a while loop to handle invalid inputs
    while(True):
        try:
            city = input("Choose from (Chicago, New York City, Washington): ")
            city = city.lower().strip()
        except:
            print("Invaild input try again\n")
        else:
            if city == "chicago" or city == "new york city" or city == "washington":
                break
            else:
                print("Make sure you wrote the city properly\n")    
    # get user input for month (all, january, february, ... , june)
    months_list = ["january", "february", "march", "april", "may", "june", "all"]
    while(True):
        try:
            month = input("Choose month filter from (Januray, February, March, April, May, June, or All): ")
            month = month.lower().strip()
        except:
            print("Invaild input try again\n")
        else:
            if month in months_list:
                break
            else:
                print("Make sure you wrote the month properly\n")    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while(True):
        try:
            print("Choose day from")
            day = input("Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All: ")
            day = day.lower().strip()
        except:
            print("Invaild input try again\n")
        else:
            if day in days_list:
                break
            else:
                print("Make sure you wrote the day properly\n")
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
    cl = city.lower()
    df = pd.read_csv(CITY_DATA[cl])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Days of Week'] = df['Start Time'].dt.day_name()
    months_list = ["january", "february", "march", "april", "may", "june"]
   
    if month != "all":
        month = months_list.index(month)+1
        df = df[df['Month'] == month]
    if day != "all":
        df = df[df['Days of Week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month: ",df["Month"].mode()[0])

    # display the most common day of week
    print("The most common day of week: ",df["Days of Week"].mode()[0])

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df["Hours"] = df["Start Time"].dt.hour
    print("The most common Hour: ", df["Hours"].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station: ",df['Start Station'].mode()[0])
    # display most commonly used end station
    print("The most commonly used end station: ", df['End Station'].mode()[0])
    # display most frequent combination of start station and end station trip
    fre_com = (df['Start Station'] + " || " +df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station: ",fre_com)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time: ",df['Trip Duration'].sum())

    # display mean travel time
    print("mean travel time: ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    temp = df['User Type'].value_counts()
    print("Counts of user types:")
    print(temp.index[0], " = ", temp[0])
    print(temp.index[1], " = ", temp[1])
    # Display counts of gender
    if city != 'washington':
        temp = df['Gender'].value_counts()
        print("\nCounts of gender: ")
        print(temp.index[0], " = ", temp[0])
        print(temp.index[1], " = ", temp[1])
        # Display earliest, most recent, and most common year of birth
        print("\nEarliest year of birth: ",int(df['Birth Year'].min()))
        print("Most recent year of birth: ",int(df['Birth Year'].max()))
        print("Most common year of birth: ",int(df['Birth Year'].mode()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_matrial(df):
    n = 0
    while (True):
        try:
            x = input("Do you want to see 5 raw matrial(yes,no): ")
            x = x.lower().strip()
        except:
            print("invaild input")
        else:
            if x == 'yes':
                print(df[n:(n+5)])
                n+=5
            elif x == 'no':
                break
            else:
                print("Please enter \'yes\' or \'no\' only")
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_matrial(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        restart.strip()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
