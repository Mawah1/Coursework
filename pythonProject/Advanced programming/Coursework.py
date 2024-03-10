import requests
import pandas as pd
import json
#Display the whole dataframe to see the type of dataset (its attributes and entities) that is available
#the format belwo displays the data structure as a dictionary
#STEP 1
class DataPoint1:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://datapoint.metoffice.gov.uk/public/data/"
        self.data = None
    def get_data(self):
        url = f"{self.base_url}val/wxfcs/all/json/sitelist?key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            self.data = response.json()
            return self.data
api_key = "91d1d1e0-7ea0-4008-a2fc-130fcca7bbe2"
datapoint = DataPoint1(api_key)

# Get the data using the get_data method
site_data = datapoint.get_data()
#print(site_data)






#STEP 2
#Display in a tabular/column format
# class DataPoint:
#     def __init__(self, api_key):
#         self.api_key = api_key
#         self.base_url = "http://datapoint.metoffice.gov.uk/public/data/"
#         self.data = None
#     def get_data(self):
#         url = f"{self.base_url}val/wxfcs/all/json/sitelist?key={self.api_key}"
#         response = requests.get(url)
#         if response.status_code == 200:
#             self.data = response.json()
#             locations_list = self.data['Locations']['Location']
#             return pd.DataFrame(locations_list)
# api_key = "91d1d1e0-7ea0-4008-a2fc-130fcca7bbe2"
# datapoint = DataPoint(api_key)
#
# # Get the data using the get_data method
# site_data = datapoint.get_data()
# print(site_data)




#STEP 3
#Display the weather forecast Dictionary for liverpool
class Datapoint:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://datapoint.metoffice.gov.uk/public/data/"
        self.data = None
    def get_forecast(self, location_id, datatype= 'json'):
        url = f"{self.base_url}val/wxfcs/all/json/{location_id}?res=3hourly&key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            self.data = response.json()
            return self.data
api_key = "91d1d1e0-7ea0-4008-a2fc-130fcca7bbe2"
datapoint = Datapoint(api_key)
location_id = '310012'
# Get the data using the get_data method
site_data = datapoint.get_forecast(location_id)
#print(site_data)


#STEP 4: Task 1
class DataPoint:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://datapoint.metoffice.gov.uk/public/data/"

    def get_location_id(self, location_name):
        # Endpoint to get the list of location sites
        url = f"{self.base_url}val/wxfcs/all/json/sitelist?key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            sites = response.json()['Locations']['Location']
            # Find the location ID by matching the location name
            for site in sites:
                if site['name'].lower() == location_name.lower():
                    return site['id']
            raise ValueError(f"Location '{location_name}' not found.")
        else:
             print(f"Failed to retrieve data: {response.status_code}")
             return pd.DataFrame()  # Return an empty DataFrame on failure

    def fetch_location_ids(self):
            # Fetch the list of locations
        url = f"{self.base_url}val/wxfcs/all/json/sitelist?key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
           data = response.json()
                # Extract location IDs
           locations = data['Locations']['Location']
           location_ids = [location['id'] for location in locations]
           return location_ids
        else:
            print(f"Failed to retrieve locations: {response.status_code}")
            return []

    def get_forecast_data(self, location_ids):
        forecast_data_list = []  # Initialize the list to store DataFrames
        for location_id in location_ids:
                # Endpoint for 3-hourly forecasts
            url = f"{self.base_url}val/wxfcs/all/json/{location_id}?res=3hourly&key={self.api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()['SiteRep']['DV']['Location']['Period']
                    for period in data:
                        df = pd.DataFrame(period['Rep'])
                        df['date'] = period['value']
                        df['location_id'] = location_id  # Add the location ID to the DataFrame
                        forecast_data_list.append(df)
                except json.JSONDecodeError as e:
                    print(f"JSON decoding failed for location {location_id}: {e}")
            else:
                print(f"Failed to retrieve data for location {location_id}: {response.status_code}")
            # Concatenate all DataFrames in the list
        forecast_data = pd.concat(forecast_data_list, ignore_index=True) if forecast_data_list else pd.DataFrame()
        return forecast_data

    # Usage
api_key = "91d1d1e0-7ea0-4008-a2fc-130fcca7bbe2"
datapoint = DataPoint(api_key)
location_ids = datapoint.fetch_location_ids()

    # Fetching forecast data for the first 30 locations
forecast_data = datapoint.get_forecast_data(location_ids[:30])
# print(datapoint.get_location_id('Liverpool'))
# print(forecast_data)

#Task 2.1: save forecast data into a csv file
forecast_data.to_csv('forecast_data.csv', index=False)

#Task 2.2
forecast_data = pd.read_csv('forecast_data.csv')
#print(forecast_data.head())

#Task 2.3:
new_column_names = {'D': 'Wind Direction', 'F': 'Feels Like Temperature', 'G': 'Wind Gust', 'H': 'Screen Relative Humidity', 'Pp': 'Precipitation Probability', 'S': 'Wind Speed',
                    'T': 'Temperature', 'V': 'Visibility', 'W': 'Weather Type', 'U': 'Max UV Index'}
forecast_data.rename(columns=new_column_names, inplace=True)
#verify that this has been done
#print(forecast_data.head())

#Task 2.4
pd.set_option('display.max_columns', None)
del forecast_data['$']
#verify this has been done as number of columns should reduce from 13 to 12
#print(forecast_data.head())


#Task 2.5
#Create a sample weather_mapping dictionary
weather_mapping = {
    None: "Not available",
    -1: "Trace rain",
    0: "Clear",
    1: "Clear",
    2: "Partly cloudy",
    3: "Partly cloudy",
    4: "Not used",
    5: "Low visibility",
    6: "Low visibility",
    7: "Cloudy",
    8: "Cloudy",
    9: "Light rain",
    10: "Light rain",
    11: "Light rain",
    12: "Light rain",
    13: "Heavy rain",
    14: "Heavy rain",
    15: "Heavy rain",
    16: "Sleet",
    17: "Sleet",
    18: "Sleet",
    19: "Hail",
    20: "Hail",
    21: "Hail",
    22: "Light snow",
    23: "Light snow",
    24: "Light snow",
    25: "Heavy snow",
    26: "Heavy snow",
    27: "Heavy snow",
    28: "Thunder",
    29: "Thunder",
    30: "Thunder"
}

# Map the weather descriptions to broader categories
forecast_data['Weather Type'] = forecast_data['Weather Type'].map(weather_mapping)
pd.set_option('display.max_columns', None)
#print(forecast_data.head())


forecast_data.to_csv('C:\\Users\\atang\\OneDrive\\Documents\\Data Science MSc\\Advanced programming for data science\\data_processed.csv.csv', index=False)






