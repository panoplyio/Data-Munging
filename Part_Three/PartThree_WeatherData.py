
from PartThree_Shared_Functionality import finds_minimum_difference
from PartThree_Shared_Functionality import print_result
from PartThree_Shared_Functionality import SharedObject

import json

WEATHER_FILE_NAME = 'weather.json'
STRING_TO_PRINT = 'The day number with the smallest temperature spread is'
NOT_VALID_OBJ_MSG = 'Not valid name or integers for'


# Object decoding using object_weather_decoder func
def object_decoder(line_from_file):
    return json.loads(line_from_file, object_hook=object_weather_decoder)


# JSON object decoding - decode a JSON object into a WeatherObject type.
def object_weather_decoder(obj):
    day = obj['Dy']
    max_t = obj['MxT']
    min_t = obj['MnT']
    if check_validity_of_the_object(obj, day, max_t, min_t):
        return SharedObject(day, int(max_t), int(min_t))
    else:
        print("{} {}".format(NOT_VALID_OBJ_MSG, obj))
        return None


# Check if the 3 fields of the jason file are valid
def check_validity_of_the_object(obj, day, max_t, min_t):
    if 'Dy' in obj and day.isdigit() and 'MxT' in obj and max_t.isdigit() and 'MnT' in obj and min_t.isdigit():
        if int(day) >= 0:
            return True
    return False


if __name__ == "__main__":
    # Finds_minimum_difference and output the result
    min_weather_data_obj = finds_minimum_difference(WEATHER_FILE_NAME, object_decoder)
    print_result(min_weather_data_obj, STRING_TO_PRINT)
