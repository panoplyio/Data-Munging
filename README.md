# Data Munging

## Part One: Weather Data
In `weather.json` you’ll find daily weather data for Morristown, NJ for June 2002. Download this text file, then write a program to output the day number (column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum the third column).

## Part Two: Soccer League Table
The file `football.csv` contains the results from the English Premier League for 2001/2. The columns labeled ‘F’ and ‘A’ contain the total number of goals scored for and against each team in that season (so Arsenal scored 79 goals against opponents, and had 36 goals scored against them). Write a program to print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

## Part Three: DRY Fusion
Take the two programs written previously and factor out as much common code as possible, leaving you with two smaller programs and some kind of shared functionality.
Important: The program should be able to read arbitrarily large files

## Development
Both files for the assignment as well as a copy of these instructions are available here:
[https://github.com/panoplyio/data-munging](https://github.com/panoplyio/data-munging)
We strongly advise you that you also add some tests if you want to make sure you don't break the code while you refactor. You could write some unit tests yourself, using the requirements to identify suitable test cases.

## Submission
The assignment should be completed in python. You may choose to use python 3 if you want (or python 2.7 otherwise). The assignment should be easily executable by either executing your main script (if its executable and has a proper [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)),  e.g. `./main.py`) or through the python interpreter like so: `python main.py`

Submission is done through [Github.com](https://github.com). Please open a new public repository under your username with separate directories for each part and send us the link.
