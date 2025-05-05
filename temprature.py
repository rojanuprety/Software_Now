import os  # For accessing file directories
import csv  # For reading CSV files
from collections import defaultdict  # For handling grouped temperature data

# Function to determine season from a month
def get_season(month):
    if month in [12, 1, 2]:
        return 'Summer'
    elif month in [3, 4, 5]:
        return 'Autumn'
    elif month in [6, 7, 8]:
        return 'Winter'
    else:
        return 'Spring'

# Initialize dictionaries to store seasonal and station data
season_data = defaultdict(list)
station_temps = defaultdict(list)

# Folder path containing CSV files
folder_path = "temperatures"

# Loop through each file in the temperatures folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):  # Only process CSV files
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    station = row['Station']
                    temp = float(row['Temperature'])
                    month = int(row['Month'])
                    season = get_season(month)

                    # Collect temperatures by season and by station
                    season_data[season].append(temp)
                    station_temps[station].append(temp)
                except (ValueError, KeyError):
                    continue  # Skip rows with missing or invalid data

# Save average seasonal temperatures
with open("average_temp.txt", "w") as f:
    for season, temps in season_data.items():
        if temps:
            avg = sum(temps) / len(temps)
            f.write(f"{season}: {avg:.2f}°C\n")

# Find station(s) with largest temperature range
max_range = 0
largest_range_stations = []

for station, temps in station_temps.items():
    if temps:
        temp_range = max(temps) - min(temps)
        if temp_range > max_range:
            max_range = temp_range
            largest_range_stations = [station]
        elif temp_range == max_range:
            largest_range_stations.append(station)

with open("largest_temp_range_station.txt", "w") as f:
    f.write(f"Largest Temp Range: {max_range:.2f}°C\n")
    for station in largest_range_stations:
        f.write(f"{station}\n")

# Find warmest and coolest stations (by average temperature)
station_avg = {station: sum(temps)/len(temps) for station, temps in station_temps.items() if temps}
if station_avg:
    max_temp = max(station_avg.values())
    min_temp = min(station_avg.values())

    warmest = [station for station, avg in station_avg.items() if avg == max_temp]
    coolest = [station for station, avg in station_avg.items() if avg == min_temp]

    with open("warmest_and_coolest_station.txt", "w") as f:
        f.write(f"Warmest Station(s) - Avg Temp: {max_temp:.2f}°C\n")
        for station in warmest:
            f.write(f"{station}\n")
        f.write(f"\nCoolest Station(s) - Avg Temp: {min_temp:.2f}°C\n")
        for station in coolest:
            f.write(f"{station}\n")
