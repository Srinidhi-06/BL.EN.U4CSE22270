import requests

url = "http://20.244.56.144/evaluation-service/register"
data = {
    "email": "bl.en.u4cse22270@bl.students.amrita.edu",
    "name": "Srinidhi M",
    "mobileNo": "7899153468",
    "githubUsername": "Srinidhi-06",
    "rollNo": "BL.EN.U4CSE22270",
    "collegeName": "Amrita Vishwa Vidyapeetham",
    "accessCode": "SwuuKE"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("✅ Registration Successful:")
    print(response.json())
else:
    print("❌ Registration Failed:", response.status_code, response.text)
