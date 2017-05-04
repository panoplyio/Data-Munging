
import csv

SOCCER_FILE_NAME = 'football.csv'
NOT_VAlID_NAME_MSG = 'Not valid name or integers for'
TEAM_OUTPUT_MSG = 'The team with the smallest difference in ‘for’ and ‘against’ goals is'
NOT_VALID_ROW_MSG = 'There is not a valid row in the file'
EMPTY_STRING = ''
TEAM = 'Team           '
FOR = 'F'
AGAINST = 'A'


# The soccerTeam object
class SoccerTeam(object):
    def __init__(self, team_name, for_goals, against_goals):
        self.m_team_name = team_name
        self.m_difference_in_goals = abs(for_goals - against_goals)


# Convert row to soccerTeam object
def create_soccer_team_object(row):
    name = row[TEAM]
    team_name = name.strip()
    for_goals = row[FOR]
    against_goals = row[AGAINST]
    if check_validity(for_goals, against_goals, team_name):
        return SoccerTeam(team_name, int(for_goals), int(against_goals))
    else:
        print("{} {}".format(NOT_VAlID_NAME_MSG, row))
    return None


# Check if the 3 members are valid (int, int and string not empty)
def check_validity(for_goals, against_goals, team_name):
    if for_goals.isdigit() and against_goals.isdigit() and team_name:
        if int(for_goals) >= 0 and int(against_goals) >= 0:
            return True
    return False


# Iterate on the csv file and compare between the soccer objects
def finds__soccer_team_with_smallest_difference(file_name):
    with open(file_name) as SoccerLeagueDataFile:
        reader = csv.DictReader(SoccerLeagueDataFile, skipinitialspace=True)

        soccer_league_team = None

        # finds the first occurrence of valid line in the file
        line = reader.__next__()
        while soccer_league_team is None and line != EMPTY_STRING:
            soccer_league_team = create_soccer_team_object(line)
            line = reader.__next__()

        # iterate and compare
        for row in reader:
            soccer_object_temporary = create_soccer_team_object(row)
            if soccer_object_temporary is not None and soccer_object_temporary.m_difference_in_goals < \
                    soccer_league_team.m_difference_in_goals:
                soccer_league_team = soccer_object_temporary
        return soccer_league_team


# Print the output - the soccer team with the smallest difference in goals
def print_result(soccer_league_team):
    if soccer_league_team is not None:
        print("{} {}".format(TEAM_OUTPUT_MSG, soccer_league_team.m_team_name))
    else:
        print(NOT_VALID_ROW_MSG)


if __name__ == "__main__":
    # Print the result
    print_result(finds__soccer_team_with_smallest_difference(SOCCER_FILE_NAME))
