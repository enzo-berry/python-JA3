import requests 

for i in range(1,3):
    print(i,"Fetching JA3")
    res = requests.get('https://tls.peet.ws/api/all')
    json_obj = res.json()
    print(json_obj["tls"]["ja3_hash"] + '\n')
