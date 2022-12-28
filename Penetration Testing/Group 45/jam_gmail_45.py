import requests
import warnings
import time

warnings.filterwarnings("ignore")

headers = {
	"Cookie": "csrftoken=7rxja5p0YBV01t12MI4NvaXtbEHT5Kfg",
	"Content-Length": "168",
	"Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
	#"Sec-Ch-Ua": '"Not?A_Brand";v="8", "Chromium";v="108"',
	#"Sec-Ch-Ua-Mobile": "?0",
	#"Sec-Ch-Ua-Platform": "Windows",
	#"Upgrade-Insecure-Requests": "1",
	"Origin": "http://192.168.3.114",
	"Content-Type": "application/x-www-form-urlencoded",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.72 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	#"Sec-Fetch-Site": "same-origin",
	#"Sec-Fetch-Mode": "cors",
	#"Sec-Fetch-User": "?1",
	#"Sec-Fetch-Dest": "empty",
	"Referer": "http://192.168.3.114/signup1/",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "en-US,en;q=0.9",
	"Connection": "close"
	}

data = "csrfmiddlewaretoken=t1rG3qq94n8ZiamYBKRgMxvnZAwzfn9SqiOP3lFZSOTP9tdQdiLT7xiG043iaXeY&loginUser=yerdofadre%40gufum.com&loginPassword=Juster123%24&rePassword=Juster123%24"

#data = "csrfmiddlewaretoken=f50g4EavaI6oKsB8Idp6bbSdk50PsNGOOlwJa3pBLeSn3KQVPrdaylS6cr80Q7EZ&username=lepsemospe%40gufum.com&password=horseman"



for i in range(2000):
    #data = '{"name":"fall guys'+str(i)+'","email":"kuspecolti'+str(i)+'@gufum.com","address":"geqrhuqrfh","username":"humano'+str(i)+'","type":"user","password":"Password123","description":"uwviurfuewh"}'
    r = requests.post("http://192.168.3.114/signup1/signup2/",headers = headers, data=data, verify=False)
    print(f"{i} {r}")
    #time.sleep(7)
