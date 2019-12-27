import requests
from bs4 import BeautifulSoup as BS

s = requests.Session()

auth_html = s.get('https://geekbrains.ru/login')
auth_bs = BS(auth_html.content, 'html.parser')
csrf = auth_bs.select('input[name=authenticity_token]')[0]['value']
print(csrf)
coding = auth_bs.select('input[name=utf8]')[0]['value']
print(coding)

payload = {
    'utf8': coding,
    'authenticity_token': csrf,
    'user[email]': 'axe-ska@bk.ru',
    'user[password]': '11011940',
    'user[remember_me]': 0
}

answ = s.post('https://geekbrains.ru/login', data=payload)
print(answ)


r = requests.get('https://geekbrains.ru/users/2266034')
html = BS(r.content, 'html.parser')
for el in html.select('.h2'):
    print(el)

# ans_bs = BS(answ.content, 'html.parser')
#
#
# print('Имя: ' + ans_bs.select('.input-lg')[0]['value'].text.strip())
