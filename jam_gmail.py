import requests
import warnings

warnings.filterwarnings("ignore")

for i in range(2400):
    print(i)
    requests.get("https://192.168.3.50/homepage/ajax_generate_code/?luspizedra@gufum.com", verify=False)
