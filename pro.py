from bs4 import BeautifulSoup
import requests

def crawling():
	proxy = []
	link = "https://www.sslproxies.org/"
	req= requests.get(link)
	ba = BeautifulSoup(req.text, "html.parser")

	for x in ba.find_all("tr")[:30]:
		if x.find_all("td"):
			data = x.find_all("td")
			address = data[0].text
			port = data[1].text
			ip = data[4].text
			prox = ip+":"+port
			proxy.append({"https":prox})
            print(data)
	return proxy
	
proxy = crawling()
print(proxy)