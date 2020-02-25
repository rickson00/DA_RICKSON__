# Use the Request library
import requests
# Set the target webpage
url = 'http://172.17.50.43/freebix'
r = requests.get(url)
# This will get the full page
print(r.text)

# This will just get just the headers
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
# This will modify the headers user-agent
headers = {
    'User-Agent' : 'mobile'
}
# Test it on an external site
url = 'http://172.17.50.43/freebix'
rh = requests.get(url2, headers=headers)
print(rh.text)
