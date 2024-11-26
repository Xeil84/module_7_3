import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
#print(r.status_code)
#print(r.headers['content-type'])
#print(r.encoding)
#print(r.text)
#print(r.json())

r = requests.get('https://api.github.com/events')
r.text
print(r.content)

