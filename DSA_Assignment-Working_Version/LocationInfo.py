class locationInfo():
    def __init__(self,temp,humidity,wind):
        self.temp = temp
        self.humidity = humidity
        self.wind = wind

    def getTemp(self):
        return self.temp
    
    def getHumidity(self):
        return self.humidity
    
    def getWind(self):
        return self.wind
    
    def __str__(self) -> str:
        return f"Temp: {self.temp}\u00B0C. Humidity: {self.humidity}%.  Wind: {self.wind} km/h"
    
    