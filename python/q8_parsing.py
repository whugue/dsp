"""
#The football.csv file contains the results from the English Premier League. 
# The columns labeled Goals and Goals Allowed contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in for and against goals.
# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.
"""

#Read In CSV Data as a Nested List
import csv

def read_data(data):
    return list(csv.reader(open(data)))

football=read_data("football.csv")



#Compute the difference between G and GA for each team. Return a dict with the team name as key & diff as value
def calc_score_diff(parsed_data):
    d={}

    for i in range(1,len(parsed_data)): #start at index 1 to skip over variable names :)
        d[parsed_data[i][0]]=abs(float(parsed_data[i][5])-float(parsed_data[i][6]))

    return d

difference=calc_score_diff(football)



#Return the Team Name (dictionary key) with the minimum difference between G and GA
def get_team(d):
    min_value=1000

    for key in d:
        if d[key] < min_value:
            min_value_team=key
            min_value=d[key]

    return min_value_team

#Print Team Name
print get_team(difference)