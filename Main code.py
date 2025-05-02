import xml.etree.ElementTree as ET  # For parsing XML 
import csv  # For handling CSV files 
from datetime import datetime, timezone 
import matplotlib.pyplot as plt  # For plotting graphs 
# File paths for health data (XML) and weather data (CSV) 
HEALTH_XML_FILE = 'aditya.xml' 
WEATHER_CSV_FILE = r'C:\Users\lirda\python automation 
project\hyderabad_weather_jul_dec_2023.csv' 
# Date range for the health data to be considered 
START_DATE = '2023-07-01' 
END_DATE = '2023-12-31' 
# Convert the start and end dates to datetime objects with timezone info 
start_date = datetime.strptime(START_DATE, "%Y-%m-%d").replace(tzinfo=timezone.utc) 
end_date = datetime.strptime(END_DATE, "%Y-%m-%d").replace(tzinfo=timezone.utc) 
# Function to load weather data from the CSV file 
def load_weather_data_from_csv(csv_file): 
weather_data = {} 
with open(csv_file, mode='r') as file: 
csv_reader = csv.reader(file) 
next(csv_reader)  # Skip header 
   
 
   
 
        for row in csv_reader: 
            if len(row) == 3: 
                date_str, time_str, temp = row 
                # Create a combined date-time key using only the date and hour 
                date_time_key = f"{date_str} {time_str[:2]}:00"  # Take only the hour part (HH:00) 
                weather_data[date_time_key] = { 
                    'temperature': float(temp), 
                } 
    return weather_data 
  
# Function to fetch weather data for a specific date and time 
def get_weather_for_date_time(date_time_str, weather_data): 
    try: 
        dt_obj = datetime.strptime(date_time_str, 
"%Y-%m-%d %H:%M:%S %z").replace(tzinfo=None) 
        date_str = dt_obj.strftime("%Y-%m-%d") 
        hour_str = dt_obj.strftime("%H:00")  # Match only by the hour 
        date_time_key = f"{date_str} {hour_str}" 
        if date_time_key in weather_data: 
            return weather_data[date_time_key] 
        else: 
            print(f"No weather data for {date_time_key}") 
            return None 
    except Exception as e: 
        print(f"Error fetching weather data for {date_time_str}: {e}") 
        return None 
   
 
   
 
  
# Load the weather data from the CSV 
weather_data = load_weather_data_from_csv(WEATHER_CSV_FILE) 
  
# Load and parse the health XML file 
tree = ET.parse(HEALTH_XML_FILE) 
root = tree.getroot() 
  
# Extract health records and organize by date 
health_data_by_day = {} 
  
for record in root.findall('Record'): 
    record_type = record.attrib['type'] 
    value = record.attrib['value'] 
    start_date_str = record.attrib['startDate'] 
    unit = record.attrib.get('unit', 'N/A') 
  
    record_datetime = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S %z") 
  
    if start_date <= record_datetime <= end_date: 
        weather_info = get_weather_for_date_time(start_date_str, weather_data) 
        temperature = weather_info['temperature'] if weather_info else 'N/A' 
  
        if record_type == "HKQuantityTypeIdentifierHeartRate" and temperature != 'N/A': 
            date_str = record_datetime.strftime("%Y-%m-%d") 
  
   
 
   
 
            if date_str not in health_data_by_day: 
                health_data_by_day[date_str] = [] 
  
            health_data_by_day[date_str].append({ 
                'heart_rate': float(value), 
                'temperature': temperature, 
                'time': record_datetime 
            }) 
  
# Select one day from each month (July to December) 
selected_days = [] 
for month in range(7, 13):  # Months July (7) to December (12) 
    for date_str in health_data_by_day: 
        date_obj = datetime.strptime(date_str, "%Y-%m-%d") 
        if date_obj.month == month: 
            selected_days.append(date_str) 
            break 
  
# Create a graph for each selected day 
for day in selected_days: 
    heart_rates = [entry['heart_rate'] for entry in health_data_by_day[day]] 
    temperatures = [entry['temperature'] for entry in health_data_by_day[day]] 
  
    plt.figure() 
    plt.scatter(heart_rates, temperatures, color='blue') 
    plt.title(f"Heart Rate vs Temperature on {day}") 
plt.xlabel("Heart Rate (count/min)") 
plt.ylabel("Temperature (°C)") 
plt.grid(True) 
plt.savefig(f"heart_rate_vs_temperature_{day}.png") 
plt.show()