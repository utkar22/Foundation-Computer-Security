import requests
import warnings
import time

warnings.filterwarnings("ignore")

headers = {
	#"Cookie": "csrftoken=JqGDgzpgLGW9tspXhoYexka32wilyu8l; sessionid=cv3hv2l59wq64grsyv8lx82rio1dtury",
	"Content-Length": "58",
	#"Cache-Control": "max-age=0",
	"Sec-Ch-Ua": '"Not?A_Brand";v="8", "Chromium";v="108"',
	"Sec-Ch-Ua-Mobile": "?0",
	"Sec-Ch-Ua-Platform": "Windows",
	#"Upgrade-Insecure-Requests": "1",
	"Origin": "https://192.168.2.235",
	"Content-Type": "application/json",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.72 Safari/537.36",
	"Accept": "*/*",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "cors",
	#"Sec-Fetch-User": "?1",
	"Sec-Fetch-Dest": "empty",
	"Referer": "https://192.168.2.235/",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "en-US,en;q=0.9",
	"Connection": "close"
	}

#data = "csrfmiddlewaretoken=f50g4EavaI6oKsB8Idp6bbSdk50PsNGOOlwJa3pBLeSn3KQVPrdaylS6cr80Q7EZ&username=lepsemospe%40gufum.com&password=horseman"
data = '{"email":"nerdigatru@gufum.com","password":"Password123$"}'

i = 0
while (i<3500):
    #for j in range(20):
    r = requests.post("https://192.168.2.235/api/authToLogin",headers = headers, data=data, verify=False)
    print(f"{i} {r}")
    i+=1
    time.sleep(5.5)
