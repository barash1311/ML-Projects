'''
https://python.langchain.com/docs/introduction/
https://python.langchain.com/docs/concepts/
https://python.langchain.com/docs/tutorials/
'''
import threading
import requests
from bs4 import BeautifulSoup


url=[
"https://python.langchain.com/docs/introduction/"
,"https://python.langchain.com/docs/concepts/",
"https://python.langchain.com/docs/tutorials/"
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"html.parser")
    print(f"Fetched {len(soup.text)} characters from {url}")

threads=[]
for ur in url:
    thread=threading.Thread(target=fetch_content,args=(ur,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()

print("printed")