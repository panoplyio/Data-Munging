
EMPTY_STRING = ''
NOT_VALID_ROW_MSG = 'There is not a valid row in the file'


# The object for both parts
class SharedObject(object):
    def __init__(self, name, maximum, minimum):
        self.name = name
        self.difference = abs(maximum - minimum)


# Iterate on the given file and compare between two objects each time
def finds_minimum_difference(file_name, object_decoder_func):
    with open(file_name) as DataFile:
        minimum_object = None

        # finds the first occurrence of valid row in the file
        line = DataFile.readline()
        while minimum_object is None and line != EMPTY_STRING:
            minimum_object = object_decoder_func(line)
            line = DataFile.readline()

        for line in DataFile:
            temporary_object = object_decoder_func(line)
            # Compare the day's spread
            minimum_object = compare_difference(temporary_object,minimum_object)

        return minimum_object


# Return the object with the smallest difference
def compare_difference(object_one, object_two):
    if object_one is not None and object_one.difference < object_two.difference:
        return object_one
    else:
        return object_two


# Print the output - the object with the smallest difference
def print_result(obj, string):
    if obj is not None:
        print("{} {}".format(string, obj.name))
    else:
        print(NOT_VALID_ROW_MSG)
