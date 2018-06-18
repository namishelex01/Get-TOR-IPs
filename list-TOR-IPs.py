import requests
import re

def extractAllIPs():
    url = 'https://check.torproject.org/exit-addresses'
    resp = requests.get(url=url)
    resp.encoding = 'ISO-8859-1'
    with open('IP-list.txt','w') as file:
        file.write(resp.text)

def dumpAllIPs():
    ips = []
    with open('IP-list.txt','r') as file:
        aa = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", file.read())
    print aa

if __name__ == '__main__':
    extractAllIPs()
    dumpAllIPs()
