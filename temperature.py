import os
import csv
from collections import defaultdict

# Define folder containing temperature CSV files
TEMPERATURES_FOLDER = r'temperature_data'

# Define month to season mapping (Australian seasons)
SEASON_MAP = {
    'December': 'Summer',
    'January': 'Summer',
    'February': 'Summer',
    'March': 'Autumn',
    'April': 'Autumn',
    'May': 'Autumn',
    'June': 'Winter',
    'July': 'Winter',
    'August': 'Winter',
    'September': 'Spring',
    'October': 'Spring',
    'November': 'Spring',
}

def read_temperatures_files(folder_path):
    station_data = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    station_name = row['STATION_NAME']
                    if station_name not in station_data:
                        station_data[station_name] = {
                            'temps_by_month': defaultdict(list),
                            'all_temps': []
                        }
                    for month in SEASON_MAP.keys():
                        if month in row and row[month].strip():
                            try:
                                temp = float(row[month])
                                station_data[station_name]['temps_by_month'][month].append(temp)
                                station_data[station_name]['all_temps'].append(temp)
                            except ValueError:
                                continue  # Skip invalid temperature
    return station_data

def calculate_average_seasonal_temperatures(station_data):
    seasonal_totals = defaultdict(list)
    for station in station_data.values():
        for month, temps in station['temps_by_month'].items():
            season = SEASON_MAP[month]
            seasonal_totals[season].extend(temps)
    seasonal_averages = {
        season: sum(temps) / len(temps) if temps else 0
        for season, temps in seasonal_totals.items()
    }
    return seasonal_averages

def find_largest_temp_range_station(station_data):
    station_ranges = {}
    for name, data in station_data.items():
        temps = data['all_temps']
        if temps:
            station_ranges[name] = max(temps) - min(temps)
    max_range = max(station_ranges.values())
    return [name for name, range_ in station_ranges.items() if range_ == max_range]

def find_warmest_and_coolest_station(station_data):
    station_averages = {}
    for name, data in station_data.items():
        temps = data['all_temps']
        if temps:
            station_averages[name] = sum(temps) / len(temps)
    max_avg = max(station_averages.values())
    min_avg = min(station_averages.values())
    warmest = [name for name, avg in station_averages.items() if avg == max_avg]
    coolest = [name for name, avg in station_averages.items() if avg == min_avg]
    return warmest, coolest

def write_to_file(filename, data_lines):
    with open(filename, 'w') as file:
        for line in data_lines:
            file.write(line + '\n')

def main():
    station_data = read_temperatures_files(TEMPERATURES_FOLDER)

    # 1. Average temperatures for each season
    seasonal_averages = calculate_average_seasonal_temperatures(station_data)
    avg_lines = [f"{season}: {avg:.2f}°C" for season, avg in seasonal_averages.items()]
    write_to_file("average_temp.txt", avg_lines)

    # 2. Station(s) with the largest temperature range
    largest_range_stations = find_largest_temp_range_station(station_data)
    write_to_file("largest_temp_range_station.txt", largest_range_stations)

    # 3. Warmest and coolest station(s)
    warmest, coolest = find_warmest_and_coolest_station(station_data)
    result_lines = ["Warmest Station(s):"] + warmest + ["", "Coolest Station(s):"] + coolest
    write_to_file("warmest_and_coolest_station.txt", result_lines)

if __name__ == "__main__":
    main()
