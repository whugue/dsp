
#Read CSV data into nested list
import csv
import re

faculty=list(csv.reader(open("faculty.csv")))

#Create faculty_dict dictionary
def create_dict_1(data):
	faculty_dict={}

	for i in range(1,len(data)):
		names=re.split(" ",data[i][0],flags=re.I)
		last_name=names[len(names)]

		degree_type=data[i][1]
		job_title=re.sub(" is "," of ",data[i][2],flags=re.I)
		job_title=re.split(" of",job_title,flags=re.I)[0]
		email=data[i][3]

		faculty_info=[degree_type, job_title, email]

		if last_name not in faculty_dict:
			faculty_dict[last_name]=faculty_info
		else:
			faculty_dict[last_name]=faculty_dict[last_name].append(faculty_info) #will this work?

	return faculty_dict

print create_dict_1(faculty)


#Create professor_dict dictionary
def create_dict_2(data):
	professor_dict={}

	for i in range(1,len(data)):
		name_list=re.split(" ",data[i][0],flags=re.I)
		first_name=name_list[0]
		last_name=name_list[len(name_list)]
		full_name=(first_name, last_name)

		degree_type=data[i][1]
		job_title=re.sub(" is "," of ",data[i][2],flags=re.I)
		job_title=re.split(" of",job_title,flags=re.I)[0]
		email=data[i][3]
		faculty_info=[degree_type, job_title, email]

		if full_name not in professor_dict:
			professor_dict[full_name]=faculty_info
		else:
			print "Professor's Evil Twin FOUND"

	return professor_dict

print create_dict_2(faculty)








