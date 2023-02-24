import requests
from termcolor import colored as cl

urls = open('redirect.txt', 'r').read().split('\n')

def redirect(payload,dest):
    for url in urls:
        try:
            url_2 = str(url).replace("FUZZ", payload)
            req = requests.get(url_2).url
            if req == dest:
                print(cl(f"Check This ===> {url_2}", color='red'))
            else:
                pass
        except Exception as e:
            #print(e)
            continue

payload = input(cl("Enter Payload ===> ", color='blue'))
print(" ")
dest = input(cl("Enter Destenation ===> ", color='blue'))
print(" ")
redirect(payload,dest)
