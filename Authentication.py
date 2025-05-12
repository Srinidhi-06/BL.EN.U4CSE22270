import requests

email = "bl.en.u4cse22270@bl.students.amrita.edu"
name = "srinidhi m"
roll_no = "bl.en.u4cse22270"
access_code = "SwuuKE"
client_id = "e3441a3f-a5e1-421c-8ffd-e130dd558860"
client_secret = "gejhtSHvsvtdZRan"



url = "http://20.244.56.144/evaluation-service/auth"

payload = {
    "email": email,
    "name": name,
    "rollNo": roll_no,
    "accessCode": access_code,
    "clientID": client_id,
    "clientSecret": client_secret
}

response = requests.post(url, json=payload)

if response.status_code in (200, 201):
    token_data = response.json()
    access_token = token_data["access_token"]
    print("Access Token:", access_token)
else:
    print("Failed to get token. Status code:", response.status_code)
    print("Response:", response.text)
