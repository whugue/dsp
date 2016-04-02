
#Read CSV data into nested list
import csv
import re
from collections import OrderedDict, defaultdict

faculty=list(csv.reader(open("faculty.csv")))


#Create faculty_dict and professor_dicts
faculty_dict=defaultdict(list)
professor_dict=defaultdict(list)

for i in range(1,len(faculty)): #Start at index 1 to skip over variable names
	name_list=re.split(" ",faculty[i][0],flags=re.I)
	last_name=name_list[-1]
	first_name=name_list[0]
		
	degree_type=faculty[i][1].strip()
	job_title=re.sub(" is "," of ",faculty[i][2],flags=re.I)
	job_title=re.split(" of",job_title,flags=re.I)[0]
	email=faculty[i][3]
		
	faculty_dict[last_name].append([degree_type, job_title, email])
	professor_dict[(first_name, last_name)].append([degree_type, job_title, email])

#print faculty_dict["Bellamy"]
#print faculty_dict["Ellenberg"]
#print faculty_dict["Li"]
#print professor_dict[("Jinbo","Chen")]

print faculty_dict.items()[0:3] #Print first three key-value pairs (as tuples) only
print professor_dict.items()[0:3] #Print first three key-value pairs (as tuples) only 

#Sort professor_dict dictonary
prof_dict_ordered=OrderedDict(sorted(professor_dict.items(), key=lambda x: x[0][1]))

print prof_dict_ordered.items()[0:3] #Print first three key-value pairs of ordered dictionary


