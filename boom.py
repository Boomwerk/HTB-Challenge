import requests
from bs4 import BeautifulSoup
import hashlib

print(EXPLOIT HTB CHALLENGE BY BOOMWERK ! n)

url = input(Enter url )

if len(url)  0
    session = requests.session()
    response = session.get(url)
    if response.ok
        print([+] Access to url successfuling)
        soup = BeautifulSoup(response.text, 'lxml')
        str = soup.find(h3)
        print([+] Getting the string of the website  + str.text)
        crypt = hashlib.md5(str.text.encode('utf-8')).hexdigest()
        print([+] Convert the string to md5 hash  + crypt)
        post = session.post(url,data = {hash crypt})

        postsoup = BeautifulSoup(post.text, 'lxml')
        flag = postsoup.find(p)

        print(n[++++++++++++BOOOOOOM+++++++++++++++] n)
        print(FLAG  + flag.text + n)
        print([+++++++++++++++++++++++++++++++++++])
    else
        print([x] Error 404)

else
    print ([x] Please enter an URL example  httphackthebox.eu32507)
    exit()