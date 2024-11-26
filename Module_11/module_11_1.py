import requests
# можем посмотреть содержимое ответа сервера
r = requests.get('https://api.github.com/events')
r.text
print(r.text)

#можно узнать какую кодировку использует requests
r.encoding
print(r.encoding)

#можно изменить кодировку
r.encoding = 'ISO-8859-1'
print(r.encoding)

#в случае работы с json есть встроенный декодер под него
r = requests.get('https://api.github.com/events')
r.json()
print(r.json())

#можно отправить данные в форме кода, как в html, для этого надо передать словарь
# в качестве аргумента, словарь будет автоматически закодирован при отправке
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)

#если в ответе сть файлы куки, то к ним можно получить доступ
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
r.cookies
print(r.cookies)



