import requests


class City:
    def __init__(self, name, lat, lon, your_token, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.your_token = your_token
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid={self.your_token}")

        except ConnectionError as c:
            print("There's no internet access")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        units_to_print = "°C"
        if self.units == "imperial":
            units_to_print = "°F"
        elif self.units == "standard":
            units_to_print = "K"

        print(f"In {self.name}, it is {self.temp} {units_to_print}")
        print(f"Today's high: {self.temp_max} {units_to_print}")
        print(f"Today's low: {self.temp_min} {units_to_print}")


my_city = City("Chicago", 41.881832, -87.623177, "addyour_token123")
my_city.temp_print()

vacation_city = City("New York", 40.730610, -73.935242, "addyour_token123")
vacation_city.temp_print()

