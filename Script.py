import requests
url = 'http://172.17.50.43/freebix'
r = requests.get(url)
print(r.text)
print("Status code:")
print("\t *", r.status_code)
