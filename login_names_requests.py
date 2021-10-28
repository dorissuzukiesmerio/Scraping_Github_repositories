import urllib.request # 
import os # setting up the folder


if not os.path.exists("html_files"):
	os.mkdir("html_files")

f = open("html_files/login_names.html", "wb")
response = urllib.request.urlopen("http://45.79.253.243/index.html")
html = response.read()
f.write(html)
f.close()