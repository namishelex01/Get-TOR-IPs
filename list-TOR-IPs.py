import requests
import re

def extractAllIPs():
    try:
        url = 'https://check.torproject.org/exit-addresses'
        resp = requests.get(url=url)
        resp.encoding = 'ISO-8859-1'
        with open('IP-list.txt','w') as file:
            file.write(resp.text)
    except Exception as e:
        print(e)
            
def dumpAllIPs():
    try:
        ips = []
        with open('IP-list.txt','r') as file:
            aa = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", file.read())
        print aa
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    extractAllIPs()
    dumpAllIPs()
