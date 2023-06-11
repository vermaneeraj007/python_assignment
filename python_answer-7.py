



            #Python answer -------7



import pandas as pd
import matplotlib.pyplot as plt

def analyze_meteorite_data(data):
    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Convert the year column to datetime format
    df['year'] = pd.to_datetime(df['year'], format='%Y')

    # Question 1: Get all the Earth meteorites that fell before the year 2000
    meteorites_before_2000 = df[df['year'] < pd.to_datetime('2000', format='%Y')]
    print("Earth meteorites fell before the year 2000:")
    print(meteorites_before_2000)

    # Question 2: Get all the earth meteorites co-ordinates who fell before the year 1970
    meteorites_before_1970 = df[df['year'] < pd.to_datetime('1970', format='%Y')]
    coordinates_before_1970 = meteorites_before_1970[['reclat', 'reclong']]
    print("Coordinates of Earth meteorites fell before the year 1970:")
    print(coordinates_before_1970)

    # Question 3: Assuming that the mass of the earth meteorites was in kg, get all those whose mass was more than 10000kg
    mass_more_than_10000 = df[df['mass'] > 10000]
    print("Earth meteorites with mass more than 10000kg:")
    print(mass_more_than_10000)

    # Plotting the analysis for visualizations
    # Histogram for meteorites fell before the year 2000
    plt.figure(figsize=(8, 6))
    plt.hist(meteorites_before_2000['year'], bins=20)
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.title('Earth Meteorites Fell Before the Year 2000')
    plt.xticks(rotation=45)
    plt.show()

    # Scatter plot for coordinates of meteorites fell before the year 1970
    plt.figure(figsize=(8, 6))
    plt.scatter(coordinates_before_1970['reclong'], coordinates_before_1970['reclat'], alpha=0.5)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Coordinates of Earth Meteorites Fell Before the Year 1970')
    plt.show()

    # Bar plot for mass of meteorites more than 10000kg
    plt.figure(figsize=(8, 6))
    plt.bar(mass_more_than_10000['name'], mass_more_than_10000['mass'])
    plt.xlabel('Meteorite')
    plt.ylabel('Mass (kg)')
    plt.title('Earth Meteorites with Mass More Than 10000kg')
    plt.xticks(rotation=90)
    plt.show()

if __name__ == '__main__':
    # Provide the data for analysis (use the processed_data from previous code)
    data = processed_data

    # Analyze the meteorite data and generate insights
    analyze_meteorite_data(data)
