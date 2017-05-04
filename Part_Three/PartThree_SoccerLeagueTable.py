
from PartThree_Shared_Functionality import finds_minimum_difference
from PartThree_Shared_Functionality import print_result
from PartThree_Shared_Functionality import SharedObject

SOCCER_FILE_NAME = 'football.csv'
TEAM_NAME = 0
FOR_GOALS = 5
AGAINST_GOALS = 6
VALID_LIST_SIZE = 7
STRING_TO_PRINT = 'The team with the smallest difference in ‘for’ and ‘against’ goals is'
NOT_VAlID_NAME_MSG = 'Not valid name or integers for'
TEAM = 'Team'


# Convert each line to soccerTeam object if the line is valid
def object_decoder(line_from_file):
    soccer_team = None

    # clean the line from whitespaces and create a list from it
    line_from_file = line_from_file.replace(" ", "").replace(",", " ")
    line_to_list = line_from_file.split()

    team_name = line_to_list[TEAM_NAME]
    team_for_goals = line_to_list[FOR_GOALS]
    team_against_goals = line_to_list[AGAINST_GOALS]

    if check_validity_of_the_object(team_for_goals, team_against_goals, team_name) and\
                    len(line_to_list) > VALID_LIST_SIZE:
        soccer_team =  SharedObject(team_name, int(team_for_goals), int(team_against_goals))
    elif team_name == TEAM:
        soccer_team = None
    else:
        print("{} {}".format(NOT_VAlID_NAME_MSG, line_from_file))

    return soccer_team


# Check if the 3 members are valid (int, int and string not empty)
def check_validity_of_the_object(for_goals, against_goals, team_name):
    if for_goals.isdigit() and against_goals.isdigit() and team_name:
        if int(for_goals) >= 0 and int(against_goals) >= 0:
            return True
    return False


if __name__ == "__main__":
    # Finds_minimum_difference and output the result
    soccer_league_team_obj = finds_minimum_difference(SOCCER_FILE_NAME, object_decoder)
    print_result(soccer_league_team_obj, STRING_TO_PRINT)
