import requests
import geopy
from geopy.distance import geodesic
from datetime import datetime
import pytz

# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# A little bit of scaffolding if you want to use it


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_lng() and get_nearest_station() might need to use this function.
    """
    response = requests.get(url)
    data = response.json()
    return data


def get_lat_lng(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    url = f"{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}"

    data = get_json(url)

    if "features" in data:  # if place is found/exists
        features = data["features"][0]
        lat = features["geometry"]["coordinates"][1]
        long = features["geometry"]["coordinates"][0]
    else:  # if place isn't found/doesn't exist
        return "Location not found."

    return lat, long


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    nearby_url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    nearby_data = get_json(nearby_url)
    nearest_station = ""  # initialize variables to store results
    nearest_dist = float("inf")

    for stations in nearby_data["data"]:
        lat = stations["attributes"].get("latitude")
        long = stations["attributes"].get("longitude")
        if lat and long:  # Only look at stations with location data
            station_loc = geopy.Point(float(lat), float(long))
            user_loc = geopy.Point(float(latitude), float(longitude))
            distance = geodesic(user_loc, station_loc).m
            if distance < nearest_dist:
                nearest_dist = distance
                nearest_station = stations

    if nearest_station:  # Check if nearest station exists
        name = nearest_station["attributes"]["name"]
        wheelchair = nearest_station["attributes"]["wheelchair_boarding"]
        station_id = nearest_station["id"]
        return name, wheelchair, station_id
    else:
        return "No nearby stations found."


def convert_legible_time(time: str) -> str:
    """
    Given an illegible datetime str, convert and return the date and time in a legible manner.
    """
    datetime_obj = datetime.fromisoformat(
        time
    )  # Convert the illegible time to a datetime object
    leg_date = datetime_obj.strftime(
        "%B %dth %Y"
    )  # Convert the datetime object to a legible time and date
    leg_time = datetime_obj.strftime("%I:%M %p")
    return f"{leg_date}, {leg_time}"


def show_time(station_id: int) -> str:
    """
    Given a station ID, return the time when the next train arrives.
    """
    url = f"https://api-v3.mbta.com/schedules/?api_key={MBTA_API_KEY}&filter[stop]={station_id}"
    time_data = get_json(url)
    schedule = time_data["data"]

    est = pytz.timezone("US/Eastern")
    current_time = est.localize(datetime.now()) #Localize current time to EST
    current_hour = datetime.now().hour

    for train in schedule: #Used gemini to help figure out how to filter by the hour and find the next train
        arrival_time_obj = datetime.fromisoformat(train["attributes"]["arrival_time"])
        if arrival_time_obj > current_time and arrival_time_obj.hour < current_hour + 1:
            return convert_legible_time(train["attributes"]["arrival_time"])

    return "No additional train scheduled within the next hour."


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    place_lat_long = get_lat_lng(place_name)
    location = get_nearest_station(place_lat_long[0], place_lat_long[1])

    return location


def main():
    """
    You should test all the above functions here
    """
    location = input("Enter a location within Boston: ")
    # lat, long = get_lat_lng(location)
    # station_name, wheelchair = get_nearest_station(lat, long)
    station = find_stop_near(location)
    next_train = show_time(station[2])
    print(f"The closest MBTA station to {location} is {station[0]}.")
    print(
        f"This station is {'wheelchair accessible' if station[1] == 1 else 'not wheelchair accessible'}."
    )
    print(f"Next arriving train: {next_train}.")


if __name__ == "__main__":
    main()