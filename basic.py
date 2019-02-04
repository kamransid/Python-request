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
payload = {'key1':'value1', 'key2':[1,2,3]}
r = requests.get('https://api.github.com/events', params= payload)
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




