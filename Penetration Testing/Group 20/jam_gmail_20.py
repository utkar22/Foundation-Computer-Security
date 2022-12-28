import requests
import warnings

warnings.filterwarnings("ignore")

headers = {
	#"Cookie": "csrftoken=JqGDgzpgLGW9tspXhoYexka32wilyu8l; sessionid=cv3hv2l59wq64grsyv8lx82rio1dtury",
	"Content-Length": "37",
	#"Cache-Control": "max-age=0",
	"Sec-Ch-Ua": '"Not?A_Brand";v="8", "Chromium";v="108"',
	"Sec-Ch-Ua-Mobile": "?0",
	"Sec-Ch-Ua-Platform": "Windows",
	#"Upgrade-Insecure-Requests": "1",
	"Origin": "https://192.168.3.38",
	"Content-Type": "application/json",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.72 Safari/537.36",
	"Accept": "*/*",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "cors",
	#"Sec-Fetch-User": "?1",
	"Sec-Fetch-Dest": "empty",
	"Referer": "https://192.168.3.38/",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "en-US,en;q=0.9",
	"Connection": "close"
	}

#data = "csrfmiddlewaretoken=f50g4EavaI6oKsB8Idp6bbSdk50PsNGOOlwJa3pBLeSn3KQVPrdaylS6cr80Q7EZ&username=lepsemospe%40gufum.com&password=horseman"


i = 0
while True:
    i+=1
    data = '{"userEmail":"jordamulnb'+str(i)+'@gufum.com"}'
    r = requests.post("https://192.168.3.38:8000/api/user/generate_otp_registration",headers = headers, data=data, verify=False)
    print(f"{i} {r}")
