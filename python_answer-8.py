



            #python answer ------ 8


import pandas as pd
import matplotlib.pyplot as plt

def analyze_tv_show_data(data):
    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Convert the airdate column to datetime format
    df['airdate'] = pd.to_datetime(df['airdate'], format='%Y-%m-%d')

    # Question 1: Get all the overall ratings for each season and compare the ratings using plots
    season_ratings = df.groupby('season')['average_rating'].mean()
    print("Overall ratings for each season:")
    print(season_ratings)

    # Plotting the analysis for visualizations
    # Line plot for ratings of each season
    plt.figure(figsize=(8, 6))
    plt.plot(season_ratings.index, season_ratings.values, marker='o')
    plt.xlabel('Season')
    plt.ylabel('Average Rating')
    plt.title('Ratings for Each Season')
    plt.xticks(rotation=45)
    plt.show()

    # Question 2: Get all the episode names, whose average rating is more than 8 for every season
    high_rated_episodes = df[df['average_rating'] > 8]
    print("Episode names with average rating more than 8 for every season:")
    print(high_rated_episodes['name'])

    # Question 3: Get all the episode names that aired before May 2019
    episodes_before_may_2019 = df[df['airdate'] < pd.to_datetime('2019-05-01', format='%Y-%m-%d')]
    print("Episode names that aired before May 2019:")
    print(episodes_before_may_2019['name'])

    # Question 4: Get the episode name from each season with the highest and lowest rating
    highest_rated_episodes = df.groupby('season')['average_rating'].idxmax()
    lowest_rated_episodes = df.groupby('season')['average_rating'].idxmin()
    print("Episode names with the highest rating in each season:")
    print(df.loc[highest_rated_episodes, ['season', 'name']])
    print("Episode names with the lowest rating in each season:")
    print(df.loc[lowest_rated_episodes, ['season', 'name']])

    # Question 5: Get the summary for the most popular (highest ratings) episode in every season
    most_popular_episodes = df.groupby('season')['average_rating'].idxmax()
    print("Summary for the most popular episode in each season:")
    print(df.loc[most_popular_episodes, ['season', 'name', 'summary']])

if __name__ == '__main__':
    # Provide the data for analysis (use the processed_data from previous code)
    data = processed_data

    # Analyze the TV show data and generate insights
    analyze_tv_show_data(data)
