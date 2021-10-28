from bs4 import BeautifulSoup
import pandas
# print("Hello") # checking packages are correctly installed and I am at correct folder
import os 

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pandas.DataFrame()

file_name = "html_files/github_users.html"
f = open(file_name, "r")
soup = BeautifulSoup(f.read(), "html.parser")
f.close()

span = soup.find("span")
users = span.find_all("div",{"class":"userid"})

for user in users: 
	login_name = user['ghid']
	df = df.append({
		'login_name': login_name
		}, ignore_index = True)

df.to_csv("parsed_files/login_names.csv", index = False)