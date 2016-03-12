
#Read In Data;
import csv
import re

faculty=list(csv.reader(open("faculty.csv")))


#Calculate Frequency of Each Degree Type
def degree_histogram(data):
	deg_type_hist={}

	for i in range(1,len(data)): #start at index 1 to skip over var names :)
		deg_types=re.split(" ",data[i][1],flags=re.I)

		for j in range(0,len(deg_types)):
			deg_type=re.sub("[.]","",deg_types[j])

			if deg_type != "" and deg_type != "0" and deg_type not in deg_type_hist:
				deg_type_hist[deg_type]=1
			elif deg_type !="" and deg_type != "0":
				deg_type_hist[deg_type]+=1

	return deg_type_hist

print degree_histogram(faculty)



#Calculate Frequency of Each Job Title:
def job_histogram(data):
	job_title_hist={}

	for i in range(1,len(data)):
		job_title=re.sub(" is "," of ",data[i][2],flags=re.I)
		job_title=re.split(" of",job_title,flags=re.I)[0]

		if job_title not in job_title_hist:
			job_title_hist[job_title]=1
		else:
			job_title_hist[job_title]+=1

	return job_title_hist

print job_histogram(faculty)



#Create a List of all Email Addresses
def list_email(data):
	l=[]

	for i in range(1,len(data)):
		l.append(data[i][3])

	return l

email_list=list_email(faculty)
print email_list


#Create a List of Unique Email Domains
def list_urls(emails):
	l=[]

	for email in emails:
		url=re.split("@",email,flags=re.I)[1]

		if url not in l:
			l.append(url)

	return l

print list_urls(email_list)












