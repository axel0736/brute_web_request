import requests 
lines = []

with open("raft-small-words.txt","r") as raft:
        lines = raft.readlines()

for i in lines:
        print(i.replace("\n",""))

r = requests.get('http://172.25.0.29/index.php')

web_headers = r.headers
print("Here are the headers returned")
print(web_headers)

web_html = r.text
print("Here is the html returned in the body of the webpage")
print (web_html)

web_status_code = r.status_code
print("Here is the HTTP status code returned")
print(web_status_code)

web_cookies = r.cookies
print("Here are the cookies returned from the page")
print(web_cookies)
