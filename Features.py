from enum import Enum

class FeatureColumns(Enum):
    DayOfWeek = 'DayOfWeek'
    PdDistrict = 'PdDistrict'
    X = 'X'
    Y = 'Y'
    Min_TemperatureF = 'Min.TemperatureF'
    Mean_TemperatureF = 'Mean.TemperatureF'
    Max_TemperatureF = 'Max.TemperatureF'
    Mean_Humidity = 'Mean.Humidity'
    Events = 'Events'
    Season = 'season'