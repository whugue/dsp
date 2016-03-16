
#Read CSV data into nested list
import csv
import re
from collections import OrderedDict

faculty=list(csv.reader(open("faculty.csv")))


#Create faculty_dict dictionary
def create_dict_1(data):
	faculty_dict={}

	for i in range(1,len(data)): #Start at index 1 to skip over variable names
		name_list=re.split(" ",data[i][0],flags=re.I)
		last_name=name_list[len(name_list)-1]
		
		degree_type=data[i][1].strip()
		job_title=re.sub(" is "," of ",data[i][2],flags=re.I)
		job_title=re.split(" of",job_title,flags=re.I)[0]
		email=data[i][3]
		faculty_info=[degree_type, job_title, email]

		if last_name not in faculty_dict:
			faculty_dict[last_name]=[faculty_info]

		else:
			temp_list=[]
			for i in range(0,len(faculty_dict[last_name])):
				temp_list.append(faculty_dict[last_name][i])

			temp_list.append(faculty_info)

			faculty_dict[last_name]=temp_list

	return faculty_dict

faculty_dict=create_dict_1(faculty)

print faculty_dict.items()[0:3] #Print first three key-value pairs (as tuples) only


#Create professor_dict dictionary
def create_dict_2(data):
	professor_dict={}

	for i in range(1,len(data)): #replace with full range later
		name_list=re.split(" ",data[i][0],flags=re.I)
		first_name=name_list[0]
		last_name=name_list[len(name_list)-1]
		full_name=(first_name, last_name)

		degree_type=data[i][1].strip()
		job_title=re.sub(" is "," of ",data[i][2],flags=re.I)
		job_title=re.split(" of",job_title,flags=re.I)[0]
		email=data[i][3]
		faculty_info=[degree_type, job_title, email]

		if full_name not in professor_dict:
			professor_dict[full_name]=faculty_info
		else:
			print "Professor's Evil Twin FOUND"

	return professor_dict

professor_dict=create_dict_2(faculty)

print professor_dict.items()[0:3] #print first three key-value parings (as tuples) only


#Sort professor_dict dictonary
prof_dict_ordered=OrderedDict(sorted(professor_dict.items(), key=lambda x: x[0][1]))

print prof_dict_ordered.items()[0:3] #Print first three key-value pairs of ordered dictionary


