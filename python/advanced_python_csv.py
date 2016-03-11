
#Read In Data;
import csv
faculty=list(csv.reader(open("faculty.csv")))


#Write Out Emails to CSV Files
out=open("emails.csv", "w")

for i in range(0,len(faculty)):
	out.write(faculty[i][3] + "\n")

out.close()





