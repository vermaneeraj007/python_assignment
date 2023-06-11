


            #Python Answer ----- 6


import pandas as pd
import matplotlib.pyplot as plt

def analyze_pokemon_data(data):
    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Question 1: Get all Pokemons whose spawn rate is less than 5%
    spawn_rate_less_than_5 = df[df['spawn_chance'] < 5]
    print("Pokemons with spawn rate less than 5%:")
    print(spawn_rate_less_than_5)

    # Question 2: Get all Pokemons that have less than 4 weaknesses
    less_than_4_weaknesses = df[df['weakness'].apply(lambda weaknesses: len(weaknesses.split(','))) < 4]
    print("Pokemons with less than 4 weaknesses:")
    print(less_than_4_weaknesses)

    # Question 3: Get all Pokemons that have no multipliers at all
    no_multipliers = df[df['multipliers'] == '']
    print("Pokemons with no multipliers:")
    print(no_multipliers)

    # Question 4: Get all Pokemons that do not have more than 2 evolutions
    less_than_2_evolutions = df[df['next_evolution'].apply(lambda evolutions: len(evolutions.split(','))) < 2]
    print("Pokemons with less than 2 evolutions:")
    print(less_than_2_evolutions)

    # Question 5: Get all Pokemons whose spawn time is less than 300 seconds
    df['spawn_time'] = pd.to_datetime(df['spawn_time'], format='%M:%S')
    spawn_time_less_than_300 = df[df['spawn_time'].dt.total_seconds() < 300]
    print("Pokemons with spawn time less than 300 seconds:")
    print(spawn_time_less_than_300)

    # Question 6: Get all Pokemon who have more than two types of capabilities
    more_than_2_types = df[df['type'].apply(lambda types: len(types.split(','))) > 2]
    print("Pokemons with more than 2 types of capabilities:")
    print(more_than_2_types)

    # Plotting the analysis for visualizations
    # Bar plot for spawn rate less than 5%
    plt.figure(figsize=(8, 6))
    plt.bar(spawn_rate_less_than_5['name'], spawn_rate_less_than_5['spawn_chance'])
    plt.xlabel('Pokemon')
    plt.ylabel('Spawn Rate (%)')
    plt.title('Pokemons with Spawn Rate Less Than 5%')
    plt.xticks(rotation=90)
    plt.show()

    # Pie chart for number of weaknesses
    weakness_counts = df['weakness'].apply(lambda weaknesses: len(weaknesses.split(',')))
    weakness_counts.value_counts().plot.pie(autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('Number of Weaknesses for Pokemons')
    plt.show()

    # Bar plot for number of evolutions
    evolution_counts = df['next_evolution'].apply(lambda evolutions: len(evolutions.split(',')))
    evolution_counts.value_counts().sort_index().plot.bar()
    plt.xlabel('Number of Evolutions')
    plt.ylabel('Count')
    plt.title('Number of Evolutions for Pokemons')
    plt.show()

if __name__ == '__main__':
    # Provide the data for analysis (use the processed_data from previous code)
    data = processed_data
