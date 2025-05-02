import xml.etree.ElementTree as ET
from datetime import datetime
import csv

# Function to load and parse the health XML file
def load_and_parse_health_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # List to hold heart rate records within the specified date range
    heart_rate_records = []
    
    # Define the start and end dates
    start_date = datetime.strptime("2023-07-01", "%Y-%m-%d").date()
    end_date = datetime.strptime("2023-12-31", "%Y-%m-%d").date()
    
    for record in root.findall('Record'):
        record_type = record.attrib['type']
        value = record.attrib['value']
        start_date_str = record.attrib['startDate']
        unit = record.attrib.get('unit', 'N/A')
        record_datetime = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S %z").date()
        
        # Check if the record is a heart rate record and within the specified date range
        if record_type == "HKQuantityTypeIdentifierHeartRate" and start_date <= record_datetime <= end_date:
            # Append the record to the heart rate records list
            heart_rate_records.append({
                'heart_rate': float(value),
                'startDate': start_date_str
            })
    
    return heart_rate_records

# Function to write the filtered heart rate records to a CSV file
def write_filtered_records_to_csv(records, output_file):
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['heart_rate', 'startDate'])
        writer.writeheader()
        for record in records:
            writer.writerow(record)

# XML file path
HEALTH_XML_FILE = r'C:\Users\lirda\OneDrive\Desktop\dataset\Vijay export\apple_health_export\export.xml'
OUTPUT_CSV_FILE = 'filtered_heart_rate_data.csv'

# Load and parse the health XML file
filtered_heart_rate_records = load_and_parse_health_xml(HEALTH_XML_FILE)

# Write the filtered heart rate records to a CSV file
write_filtered_records_to_csv(filtered_heart_rate_records, OUTPUT_CSV_FILE)