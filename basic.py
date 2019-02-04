import json
import requests
r = requests.get('https://api.github.com/events')
print(r.status_code)
print(r.__str__)
print(r.apparent_encoding)
print(r.headers)
v = 0
content = r.content
print(type(content))
for line in content:
    if(v > 5):
        break
    print(str(line))
    v += 1

r = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(r.status_code)
print(r.headers)

r = requests.put('https://httpbin.org/put', data={'arjun': 'bhag'})
print(r.status_code)

r = requests.delete('https://httpbin.org/delete')
print(r.status_code)
r = requests.head('https://httpbin.org/get')
print(r.status_code)
r = requests.options('https://httpbin.org/get')
print(r.status_code)
print(r.text)
r = requests.get('https://api.github.com/events')
print(r.text)
print(r.encoding)
print(r.url)
payload = {'key1': 'value1', 'key2': [1, 2, 3]}
r = requests.get('https://api.github.com/events', params=payload)
print(r.url)

#r.encoding = 'ISO-8859-1'
print(type(r.text))
p = r.text.split(',')
v = 0
for line in p:
    print(line)
    v += 1
    if v > 5:
        break


print(r.json())


print(r.raise_for_status())
print(r.status_code)

r = requests.get('https://api.github.com/events', stream=True)

print(r.raw.read(5))

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, data=json.dumps(payload))
print(r.status_code)  # 404

url = 'https://httpbin.org/post'
files = {'file': open('basic.py', 'rb')}
r = requests.post(url, files=files)
print(type(r.content))
print(r.text)
if r.status_code == requests.codes.ok:
    print('Hi hello bol k ')
print(requests.codes.ok)
print(requests)

url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)

print(r.text)



