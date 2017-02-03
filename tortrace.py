# Tor Trace 
# 
# By Avencei and Riddle

from random import randint
import requests

import requests
proxies = {
    'http': 'socks5://localhost:9050',
    'https': 'socks5://localhost:9050'
}
url = 'http://httpbin.org/ip'
r = requests.get(url, proxies=proxies)
print(r.text)

abc = "abcdefghijklmnopqrstuvwxyz1234567"
onion_address = ["http://3g2upl4pq6kufc4m.onion/"]
try:
    random_shit = int(input("How many URLs do you want to generate?\n> "))
except ValueError:
    print("You most likely entered a string")

def random_link():
    global onion_address
    for _ in range(random_shit):
        link = ""
        for _ in range(16):
            rand_char = abc[randint(2,32)]
            link  = link +  rand_char
        #onion_address.append("http://"+link+".onion")
        onion_address.append("http://ghfg.onion/")

random_link()

def check_url():
    for url in onion_address:
        r = requests.get(url, proxies , headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0"})
        if r.status_code != 500:
            print(url + "\t|\t" + str(r.status_code))

        


check_url()
