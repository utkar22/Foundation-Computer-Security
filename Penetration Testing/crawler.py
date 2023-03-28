import requests
import sqlite3

#Connecting to the database
conn = sqlite3.connect("crawl.db")
c = conn.cursor()

def replacement(data):
    data = data.replace("'","\'")
    data = data.replace('"',"\'")
    return data

for i in range(1,256):
    print(i)
    ip_addr = f"192.168.3.{i}"

    data = ""

    try:
        data = requests.get(url = f"https://{ip_addr}/",verify=False).text
    except:
        pass

    c.execute("INSERT INTO ip_blob VALUES (?,?)",(ip_addr,replacement(data)))

conn.commit()
