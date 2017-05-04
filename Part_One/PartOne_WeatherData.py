
import json

WEATHER_FILE_NAME = 'weather.json'
NOT_VAlID_NAME_MSG = 'Not valid name or integers for'
DAY_OUTPUT_MSG = 'The day number with the smallest temperature spread is'
NOT_VALID_ROW_MSG = 'There is not a valid row in the file'
EMPTY_STRING = ''


# The weather object
class WeatherObject(object):
    def __init__(self, day_number, maximum_temp, minimum_temp):
        self.m_day_number = day_number
        self.m_spread_temp = abs(maximum_temp - minimum_temp)


# JSON object decoding - decode a JSON object into a WeatherObject type.
def object_weather_decoder(obj):
    day = obj['Dy']
    max_t = obj['MxT']
    min_t = obj['MnT']
    if check_validity_of_the_object(obj, day, max_t, min_t):
        return WeatherObject(day, int(max_t), int(min_t))
    else:
        print("{} {}".format(NOT_VAlID_NAME_MSG, obj))
        return None


# Check if the 3 fields of the jason file are valid
def check_validity_of_the_object(obj, day, max_t, min_t):
    if 'Dy' in obj and day.isdigit() and 'MxT' in obj and max_t.isdigit() and 'MnT' in obj and min_t.isdigit():
        return True
    else:
        return False


# Iterate on the jason file and compare between the weather objects
def finds_the_day_with_the_smallest_spread(file_name):
    with open(file_name) as weatherDataFile:
        day_with_smallest_spread = None

        # finds the first occurrence of valid line in the file
        line = weatherDataFile.readline()
        while day_with_smallest_spread is None and line != EMPTY_STRING:
            # convert jason line to an weather object using object_weather_decoder func
            day_with_smallest_spread = json.loads(line, object_hook=object_weather_decoder)
            line = weatherDataFile.readline()

        # iterate and compare
        for line in weatherDataFile:
            weather_object_temporary = json.loads(line, object_hook=object_weather_decoder)
            # Compare the day's spread
            if weather_object_temporary is not None and weather_object_temporary.m_spread_temp <\
                    day_with_smallest_spread.m_spread_temp:
                day_with_smallest_spread = weather_object_temporary

        return day_with_smallest_spread


# Print the output - the day with the smallest spread
def print_result(day_with_smallest_temp_spread):
    if day_with_smallest_temp_spread is not None:
        print("{} {}".format(DAY_OUTPUT_MSG, day_with_smallest_temp_spread.m_day_number))
    else:
        print(NOT_VALID_ROW_MSG)


if __name__ == "__main__":
    # Print the result
    print_result(finds_the_day_with_the_smallest_spread(WEATHER_FILE_NAME))
