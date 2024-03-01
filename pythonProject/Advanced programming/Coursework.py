import requests
import pandas as pd
import json
#Display the whole dataframe to see the type of dataset (its attributes and entities) that is available
#the format belwo displays the data structure as a dictionary
#STEP 1
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
#             return self.data
# api_key = "91d1d1e0-7ea0-4008-a2fc-130fcca7bbe2"
# datapoint = DataPoint(api_key)
#
# # Get the data using the get_data method
# site_data = datapoint.get_data()
# print(site_data)



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
#Display the weather forecast Dictionary
class DataPoint:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://datapoint.metoffice.gov.uk/public/data/"
        self.data = None
    def get_forecast(self, location_id, datatype= 'json'):
        url = f"{self.base_url}val/wxfcs/all/json/{location_id}?res=3hourly&key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            self.data = response.json()
            #return self.data
api_key = "91d1d1e0-7ea0-4008-a2fc-130fcca7bbe2"
datapoint = DataPoint(api_key)
location_id = '310012'
# Get the data using the get_data method
site_data = datapoint.get_forecast(location_id)
#print(site_data)


#STEP 4
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

    def get_forecast_data(self, location_ids):
        # DataFrame to store all forecast data
        forecast_data = pd.DataFrame()
        for location_id in location_ids:
            # Endpoint for 3-hourly forecasts
            url = (f"{self.base_url}val/wxfcs/all/JSON/{location_id}"
                   f"?res=3hourly&key={self.api_key}")
            response = requests.get(url)
            if response.status_code == 200:
                # Parse the forecast data for the location and append to the DataFrame
                data = response.json()['SiteRep']['DV']['Location']['Period']
                for period in data:
                    df = pd.DataFrame(period['Rep'])
                    df['date'] = period['value']
                    forecast_data = forecast_data.append(df, ignore_index=True)
            else:
                response.raise_for_status()
        return forecast_data

api_key = "91d1d1e0-7ea0-4008-a2fc-130fcca7bbe2"  # Replace with your actual API key
datapoint = DataPoint(api_key)
        # Example usage:

print(datapoint.get_location_id('Liverpool'))
print("Forecast data for location IDs ['123', '456']:")
#print(datapoint.get_forecast_data('310012'))




#def get_forecast_data(self, location_ids):
#         """
#         Retrieve the three-hourly five-day forecast data for multiple locations.
#
#         :param location_ids: list of str, the location IDs to retrieve forecast data for
#         :return: DataFrame, the forecast data for the given locations
#         """
#         forecast_data = pd.DataFrame()
#
#         for location_id in location_ids:
#             url = f"{self.base_url}val/wxfcs/all/JSON/{location_id}?res=3hourly&key={self.api_key}"
#             try:
#                 response = requests.get(url)
#                 response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
#                 data = response.json()['SiteRep']['DV']['Location']['Period']
#
#                 # Process each period of forecasts
#                 for period in data:
#                     df = pd.DataFrame(period['Rep'])
#                     df['date'] = period['value']
#                     forecast_data = pd.concat([forecast_data, df], ignore_index=True)
#             except requests.RequestException as e:
#                 print(f"Request failed: {e}")
#         return forecast_data









